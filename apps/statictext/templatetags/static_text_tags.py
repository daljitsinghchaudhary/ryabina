# -*- coding: utf-8 -*-
from django import template
from django.conf import settings
from django.template import Context, Template
from apps.statictext.models import StaticText


register = template.Library()

@register.simple_tag(takes_context=True)
def render_static_text(context, key):
    """
    Returns static text from db for the required key
    """
    try:
        statictext = StaticText.objects.get(key=key)
    except StaticText.DoesNotExist:
        if settings.DEBUG:
            raise
        else:
            return u''
    else:
        return Template(statictext.text).render(Context(context))