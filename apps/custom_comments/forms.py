# -*- coding: utf-8 -*-
from django import forms
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
from django.utils.crypto import constant_time_compare
from django.utils.encoding import force_text
from django.utils.text import get_text_list
from django.utils.translation import ugettext, ungettext
from django_comments.forms import COMMENT_MAX_LENGTH, CommentDetailsForm
import time
from apps.custom_comments.models import CustomComment, RATING_CHOICES
from apps.services.models import ServiceCategory


class CustomCommentForm(CommentDetailsForm):
    comment = forms.CharField(label=u'', widget=forms.Textarea(attrs={'placeholder': u'Напишите комментарий', 'rows':u'3'}), max_length=COMMENT_MAX_LENGTH)

    def get_comment_object(self):
        if not self.is_valid():
            raise ValueError("get_comment_object may only be called on valid forms")

        CommentModel = self.get_comment_model()
        new = CommentModel(**self.get_comment_create_data())
        new = self.check_for_duplicate_comment(new)

        return new

    def get_comment_model(self):
        """
        Get the comment model to create with this form. Subclasses in custom
        comment apps should override this, get_comment_create_data, and perhaps
        check_for_duplicate_comment to provide custom comment models.
        """
        return CustomComment

    def get_comment_create_data(self):
        """
        Returns the dict of data to be used to create a comment. Subclasses in
        custom comment apps that override get_comment_model can override this
        method to add extra fields onto a custom comment model.
        """
        return dict(
            content_type=ContentType.objects.get_for_model(self.target_object),
            object_pk=force_text(self.target_object._get_pk_val()),
            user_name=u'',
            user_email=u'',
            user_url=u'',
            comment=self.cleaned_data['comment'],
            submit_date=timezone.now(),
            site_id=settings.SITE_ID,
            is_public=True,
            is_removed=False,
        )

    def check_for_duplicate_comment(self, new):
        """
        Check that a submitted comment isn't a duplicate. This might be caused
        by someone posting a comment twice. If it is a dup, silently return the *previous* comment.
        """
        possible_duplicates = self.get_comment_model()._default_manager.using(
            self.target_object._state.db
        ).filter(
            content_type=new.content_type,
            object_pk=new.object_pk,
            user_name=new.user_name,
            user_email=new.user_email,
            user_url=new.user_url,
        )
        for old in possible_duplicates:
            if old.submit_date.date() == new.submit_date.date() and old.comment == new.comment:
                return old

        return new

    def clean_comment(self):
        """
        If COMMENTS_ALLOW_PROFANITIES is False, check that the comment doesn't
        contain anything in PROFANITIES_LIST.
        """
        comment = self.cleaned_data["comment"]
        if not settings.COMMENTS_ALLOW_PROFANITIES:
            bad_words = [w for w in settings.PROFANITIES_LIST if w in comment.lower()]
            if bad_words:
                raise forms.ValidationError(ungettext(
                    "Watch your mouth! The word %s is not allowed here.",
                    "Watch your mouth! The words %s are not allowed here.",
                    len(bad_words)) % get_text_list(
                        ['"%s%s%s"' % (i[0], '-'*(len(i)-2), i[-1])
                         for i in bad_words], ugettext('and')))
        return comment


class ServiceCommentForm(CustomCommentForm):
    comment = forms.CharField(label=u'Общее впечатление', widget=forms.Textarea(attrs={'placeholder': u'Общее впечатление', 'rows':u'3'}), max_length=COMMENT_MAX_LENGTH)
    object_pk = forms.ModelChoiceField(queryset=ServiceCategory.objects.all().order_by('title'), widget=forms.Select(), label=u'Услуга', empty_label=u'Не имеет значения')
    rating = forms.ChoiceField(widget=forms.RadioSelect(), choices=[], initial='1', label=u'Оценка')
    photo = forms.CharField(label=u'Фото', widget=forms.TextInput(attrs={'style': u'display:none;'}), required=False)
    name = forms.CharField(label=u'Представьтесь', widget=forms.TextInput(attrs={'placeholder': u'Имя'}))
    url = forms.URLField(label=u'Ваша страница в социальной сети', required=False)

    def __init__(self, *args, **kwargs):
        self.target_model = ServiceCategory
        super(ServiceCommentForm, self).__init__(None, *args,**kwargs)
        self.fields['rating'].choices = [[item[0], u''] for item in RATING_CHOICES]
        self.excluded_fields = ['comment', 'object_pk', 'rating', 'email', 'name', 'photo', 'url']

    def clean_security_hash(self):
        """Check the security hash."""
        security_hash_dict = {
            'content_type': self.data.get("content_type", ""),
            'object_pk': '',
            'timestamp': self.data.get("timestamp", ""),
        }
        expected_hash = self.generate_security_hash(**security_hash_dict)
        actual_hash = self.cleaned_data["security_hash"]
        if not constant_time_compare(expected_hash, actual_hash):
            raise forms.ValidationError("Security hash check failed.")
        return actual_hash

    def generate_security_data(self):
        timestamp = int(time.time())
        security_dict = {
            'content_type': u'%d' % ContentType.objects.get_for_model(self.target_model).id,
            'object_pk': u'',
            'timestamp': str(timestamp),
            'security_hash': self.initial_security_hash(timestamp),
        }
        return security_dict

    def initial_security_hash(self, timestamp):
        """
        Generate the initial security hash from self.content_object
        and a (unix) timestamp.
        """

        initial_security_dict = {
            'content_type': u'%d' % ContentType.objects.get_for_model(self.target_model).id,
            'object_pk': '',
            'timestamp': str(timestamp),
        }
        return self.generate_security_hash(**initial_security_dict)