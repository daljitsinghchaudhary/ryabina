# coding=utf-8

from django.utils import timezone
from django.db import models
from tinymce.models import HTMLField


class News(models.Model):
    title = models.CharField(u'заголовок', max_length=255)
    announce = HTMLField(u'анонс')
    content = HTMLField(u'описание', blank=True, null=True)
    on_main_page = models.BooleanField(u'показывать на главной', default=True)
    is_published = models.BooleanField(u'опубликовано', default=True)
    image = models.ImageField('изображение', upload_to=u'images/news/', blank=True)
    created_at = models.DateTimeField(u'дата начала', default=timezone.now)
    close_at = models.DateTimeField(u'дата закрытия', blank=True, null=True, help_text=u'дата автоматического снятия с показа')

    class Meta:
        ordering = ('-created_at',)
        verbose_name = u'новость'
        verbose_name_plural = u'новости'
        get_latest_by = 'date_add'

    def __unicode__(self):
        return self.title
