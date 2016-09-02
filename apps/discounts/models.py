# coding=utf-8

from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField
from apps.services.models import Service


class Discount(models.Model):
    title = models.CharField(u'заголовок', max_length=255)
    image = models.ImageField(upload_to='img/discount', verbose_name=u'рисунок')
    content = HTMLField(u'содержимое', blank=True, null=True)
    url = models.CharField(u'ссылка на страницу', max_length=255, blank=True, null=True)
    button = models.CharField(u'надпись на кнопке', max_length=255, blank=True, null=True)
    current_price = models.IntegerField(u'текущая цена', blank=True, null=True)
    old_price = models.IntegerField(u'старая цена', blank=True, null=True)
    percent = models.IntegerField(u'скидка в процентах', blank=True, null=True, help_text=u'если указаны проценты, то в объявлении показываются проценты')
    created_at = models.DateTimeField(u'дата начала', default=timezone.now)
    close_at = models.DateTimeField(u'дата закрытия', blank=True, null=True, help_text=u'дата автоматического снятия с показа')
    is_published = models.BooleanField(u'опубликовано', default=True)
    services = models.ManyToManyField(Service, verbose_name=u'связанные услуги', blank=True)

    class Meta:
        ordering = ('-created_at',)
        verbose_name = u'акция'
        verbose_name_plural = u'акции'

    def __unicode__(self):
        return self.title

    def get_discount(self):
        if self.percent:
            return u'-%%%s' % self.percent
        else:
            if self.current_price:
                return u'%s' % self.current_price
            else:
                return u'бесплатно'