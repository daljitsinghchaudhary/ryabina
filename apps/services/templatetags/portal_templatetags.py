# -*- coding: utf-8 -*-
from django.conf import settings
from django import template
import urllib
from django.core.urlresolvers import reverse

register = template.Library()

@register.simple_tag
def static_dir():
    return u'%s/' % getattr(settings, 'STATIC_ROOT', '')

@register.simple_tag
def media_dir():
    return u'%s/' % getattr(settings, 'MEDIA_ROOT', '')

@register.simple_tag
def base_dir():
    return u'%s' % getattr(settings, 'BASE_DIR', '')

@register.simple_tag
def qr_code(host, size, info=None):
    return u'<img src="http://%(host)s%(url)s?size=%(size)s&qr_pass_phrase=%(pass)s&info=%(info)s" border="0" hspace="0" vspace="0" width="%(size)spx" hight="%(size)spx"/>' % {
        'host': host,
        'url': reverse('services:qr_code'),
        'size': size,
        'pass': settings.QR_PASS_PHRASE,
        'info': urllib.quote(info) if info else u''
    }