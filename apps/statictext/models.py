# coding=utf-8
from django.contrib.sites.models import Site
from django.db import models
from tinymce.models import HTMLField


class StaticText(models.Model):
    key = models.CharField(u'ключ', max_length=70, unique=True, help_text=u'Это значение используется в темплейте, не трогать!')
    text = HTMLField(u'значение', blank=True, null=True)
    comment = models.CharField(u'комментарий', max_length=255, blank=True, null=True)
    sites = models.ManyToManyField(Site, verbose_name=u'сайты')

    def __unicode__(self):
        return unicode(self.comment)

    class Meta:
        verbose_name = u'статический текст'
        verbose_name_plural = u'статические тексты'

    def sites_changelist(self):
        return ', '.join(self.sites.all().values_list('name', flat=True))
    sites_changelist.short_description = u'Сайты'