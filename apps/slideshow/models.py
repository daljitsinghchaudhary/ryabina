# coding=utf-8

from django.db import models
from tinymce.models import HTMLField


class RotatingImage(models.Model):
    image = models.ImageField(u'рисунок', upload_to='img/slideshow')
    title = models.CharField(u'заголовок', max_length=255, blank=True, null=True)
    content = HTMLField(u'содержимое', blank=True, null=True)
    url = models.CharField(u'ссылка на страницу', max_length=255, blank=True, null=True)
    button = models.CharField(u'надпись на кнопке', max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = u'картинка'
        verbose_name_plural = u'слайдшоу'

    def __unicode__(self):
        return self.title


class ParallaxImage(models.Model):
    image = models.ImageField(u'рисунок', upload_to='img/parallax')
    title = models.CharField(u'заголовок', max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = u'картинка'
        verbose_name_plural = u'паралакс'

    def __unicode__(self):
        return self.title


class ContactsImagesType(models.Model):
    title = models.CharField(u'наименование', max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = u'тип картинки'
        verbose_name_plural = u'типы картинок'

    def __unicode__(self):
        return self.title


class ContactsImage(models.Model):
    image = models.ImageField(u'рисунок', upload_to='img/contacts')
    title = models.CharField(u'заголовок', max_length=255, blank=True, null=True)
    image_type = models.ForeignKey(ContactsImagesType, verbose_name='тип', blank=True, null=True)

    class Meta:
        verbose_name = u'картинка'
        verbose_name_plural = u'контакты'

    def __unicode__(self):
        return self.title