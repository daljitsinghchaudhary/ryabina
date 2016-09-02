# coding=utf-8
from django.conf import settings
from django.db.models import CASCADE
import datetime
from django_comments.abstracts import CommentAbstractModel, COMMENT_MAX_LENGTH
from django.db import models
from django.utils import timezone
from annoying.functions import id_generator


RATING_CHOICES = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
)


class CommentPhoto(models.Model):
    temp = models.CharField(u'временный идентификатор', max_length=255, blank=True)
    photo = models.ImageField(u'фото', upload_to=u'images/comment/', blank=True)
    created_at = models.DateTimeField(u'дата начала', default=timezone.now)

    class Meta:
        ordering = ('-created_at',)
        verbose_name = u'фото'
        verbose_name_plural = u'фото'

    def __unicode__(self):
        return self.temp

    def save(self, *args, **kwargs):
        if not self.pk and not self.temp:
            self.temp = id_generator()
        super(CommentPhoto, self).save(*args, **kwargs)

    def is_for_delete(self):
        return self.created_at+datetime.timedelta(seconds=settings.COMMENTS_PHOTO_DELETE_TIMEOUT) < timezone.now() and not CustomComment.objects.filter(photo_id=self.pk).count()

    def is_for_delete_changelist(self):
        return self.is_for_delete()
    is_for_delete_changelist.short_description = u'На удаление'
    is_for_delete_changelist.boolean = True


class CustomComment(CommentAbstractModel):
    rating = models.CharField(u'рейтинг', max_length=20, choices=RATING_CHOICES, blank=True, null=True)
    photo = models.ForeignKey(CommentPhoto, verbose_name=u'фото', blank=True, null=True, on_delete=CASCADE)

    def __init__(self, *args, **kwargs):
        super(CommentAbstractModel, self).__init__(*args, **kwargs)
        for field in self._meta.fields:
            if field.name == 'object_pk':
                field.blank=True
                field.null=True

    class Meta(CommentAbstractModel.Meta):
        db_table = 'django_comments'
        app_label = 'django_comments'
