# coding=utf-8
import os
from django.contrib.sites.models import Site
from django.db import models
from pytils.translit import translify


def get_doc_path(instance, filename):
    return os.path.join(instance.get_upload_path(filename), instance.get_upload_filename(filename))

class BaseDoc(models.Model):
    title = models.CharField(u'название', max_length=250)
    doc = models.FileField(u'файл', upload_to=get_doc_path)
    size = models.IntegerField(u'размер', editable=False, default=0)

    class Meta:
        abstract = True

    def save(self, **kwargs):
        self.title = self.title.strip()
        self.size = self._get_file_size()
        super(BaseDoc, self).save(**kwargs)

    def _get_file_size(self):
        try:
            return self.doc.size
        except Exception:
            pass
        return 0

    def get_upload_path(self, filename):
        raise NotImplementedError

    def get_upload_filename(self, filename):
        return translify(filename)

    @property
    def ext(self):
        try:
            return os.path.splitext(self.filename_with_ext)[1][1:].lower()
        except Exception:
            pass
        return u''

    @property
    def filetype(self):
        ext = self.ext
        file_type = 'doc'
        if ext == 'pdf':
            file_type = 'pdf'
        if ext in ['jpg', 'jpeg']:
            file_type = 'jpg'
        if ext == 'ppt':
            file_type = 'ppt'
        if ext == 'xls':
            file_type = 'xls'
        if ext == 'zip':
            file_type = 'zip'
        return file_type

    @property
    def filename(self):
        try:
            return os.path.splitext(self.filename_with_ext)[0]
        except Exception:
            pass
        return u''

    @property
    def filename_with_ext(self):
        try:
            return os.path.basename(self.doc.name)
        except (TypeError, AttributeError):
            pass
        return u''


class FlatPage(models.Model):
    title = models.CharField(u'заголовок', max_length=255)
    url = models.CharField('URL-адрес', max_length=255, editable=False, unique=True)
    slug = models.SlugField(u'путь', max_length=50)
    parent = models.ForeignKey('self', verbose_name=u'родительская страница', related_name='children', blank=True, null=True, on_delete=models.SET_NULL)
    meta_title = models.CharField(u'title', blank=True, max_length=255)
    meta_keywords = models.TextField(u'keywords', blank=True)
    meta_description = models.TextField(u'description', blank=True)
    content = models.TextField(u'текст')
    is_published = models.BooleanField(u'опубликовано', default=True)
    sites = models.ManyToManyField(Site)
    enable_comments = models.BooleanField(u'разрешить комментировать', default=False)
    created_at = models.DateField(u'дата создания', editable=False, auto_now_add=True)
    template_name = models.CharField(u'шаблон', max_length=100, editable=False, default=u'default.html')
    order = models.IntegerField(u'порядок', blank=True, null=True)

    def get_absolute_url(self):
        return '/%s/' % self.url

    class Meta:
        ordering = ['order', 'url']
        verbose_name = u'внутренняя страница'
        verbose_name_plural = u'внутренние страницы'
        unique_together = ('slug',)

    def __unicode__(self):
        return u'%s (%s)' % (self.title, self.get_absolute_url())

    def save(self, **kwargs):
        self.title = self.title.strip()
        self.meta_title = self.meta_title.strip()
        super(FlatPage, self).save(**kwargs)


class FlatPageDoc(BaseDoc):
    page = models.ForeignKey(FlatPage, verbose_name=u'страница')
    order = models.PositiveIntegerField(u'порядковый номер')

    class Meta:
        ordering = ['order', ]
        verbose_name = u'файл внутренней страницы'
        verbose_name_plural = u'файлы внутренней страницы'

    def __unicode__(self):
        return u'%s' % self.title

    def get_upload_path(self, filename):
        return 'files/pages/%s' % self.page.pk