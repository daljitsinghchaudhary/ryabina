# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from bootstrap3.forms import render_field
from django import template

register = template.Library()

@register.simple_tag
def bootstrap_inline_checkbox_stars_field(*args, **kwargs):
    kwargs.update({
        'form_group_class': 'form-group stars',
        'show_label': True,
    })
    return render_field(*args, **kwargs).replace('<div class="radio">', '<div class="radio-inline">').replace('class="" id="id_rating_', 'class="glyphicon glyphicon-star-empty" id="id_rating_')