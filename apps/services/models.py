# coding=utf-8

from django.db import models
from treebeard.mp_tree import MP_Node


class ServiceIcon(models.Model):
    image = models.FileField(u'рисунок', upload_to='img/courses')
    title = models.CharField(u'заголовок', max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = u'иконка'
        verbose_name_plural = u'иконки услуг'

    def __unicode__(self):
        return self.title


class ServiceCourse(models.Model):
    title = models.CharField(u'заголовок', max_length=255, blank=True, null=True)
    short_title = models.CharField(u'короткий заголовок', max_length=255, blank=True, null=True)
    icon = models.ForeignKey(ServiceIcon, verbose_name='иконка', blank=True, null=True)
    on_main_page = models.BooleanField(u'на главной странице', default=False)
    description = models.TextField(u'описание', blank=True, null=True)
    url = models.CharField(u'ссылка на страницу', max_length=255, blank=True, null=True)
    button = models.CharField(u'надпись на кнопке', max_length=255, blank=True, null=True)

    class Meta:
        ordering = ('title',)
        verbose_name = u'направление'
        verbose_name_plural = u'направления услуг'

    def __unicode__(self):
        return self.get_short_title()

    def get_short_title(self):
        return u'%s' % self.short_title if self.short_title else self.title

    # def get_services(self):
    #     return Service.objects.filter(course=self)


class ServiceCategory(models.Model):
    title = models.CharField(u'заголовок', max_length=255)
    description = models.TextField(u'описание', blank=True, null=True)

    class Meta:
        ordering = ('title',)
        verbose_name = u'категория'
        verbose_name_plural = u'категории услуг'

    def __unicode__(self):
        return self.title

    def get_services_count(self):
        return self.service_set.all().count()
    get_services_count.short_description = u'Услуг'


class Service(MP_Node):
    title = models.CharField(u'заголовок', max_length=255)
    min_price = models.IntegerField(u'минимальная цена', blank=True, null=True)
    max_price = models.IntegerField(u'максимальная цена', blank=True, null=True)
    course = models.ForeignKey(ServiceCourse, verbose_name='направление', blank=True, null=True)
    category = models.ManyToManyField(ServiceCategory, verbose_name='категория', blank=True)

    node_order_by = ['course', 'title']

    class Meta:
        verbose_name = u'услуга'
        verbose_name_plural = u'услуги'

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.min_price > self.max_price:
            self.min_price, self.max_price = self.max_price, self.min_price
        super(Service, self).save(*args, **kwargs)

    def get_price(self):
        if self.min_price and self.max_price:
            if self.min_price==self.max_price:
                return u'%d' % self.min_price
            else:
                return u'от %d до %d' % (self.min_price, self.max_price)
        elif self.min_price and not self.max_price:
            return u'от %d' % self.min_price
        elif self.max_price and not self.min_price:
            return u'до %d' % self.max_price
        else:
            return None

    def get_categories(self):
        return self.category.all()

    def get_categories_changelist(self):
        return u'<br>'.join(self.get_categories().values_list('title', flat=True))
    get_categories_changelist.short_description = u'Категории'
    get_categories_changelist.allow_tags = True

    def get_price_changelist(self):
        return self.get_price()
    get_price_changelist.short_description = u'Стоимость'