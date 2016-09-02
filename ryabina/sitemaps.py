# coding=utf-8
from django.contrib.sitemaps import Sitemap
from django.core.urlresolvers import reverse


class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['pages:main', 'pages:contacts', 'pages:services']

    def location(self, item):
        return reverse(item)