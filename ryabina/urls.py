# coding=utf-8
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from filebrowser.sites import site as fb_site
from ryabina.sitemaps import StaticViewSitemap


sitemaps = {
    'static': StaticViewSitemap
}

urlpatterns = [
    url(r'^admin/filebrowser/', include(fb_site.urls)),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^', include('apps.pages.urls', namespace='pages')),
    url(r'^services/', include('apps.services.urls', namespace='services')),
    url(r'^questions/', include('apps.questions.urls', namespace='questions')),
    url(r'^comments/', include('apps.custom_comments.urls', namespace='custom_comments')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^newsletter/', include('newsletter.urls')),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
