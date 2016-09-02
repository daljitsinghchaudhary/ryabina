# -*- coding: utf-8 -*-
from django import template
from apps.custom_comments.models import RATING_CHOICES
from apps.services.models import Service, ServiceCategory

register = template.Library()

@register.assignment_tag
def get_course_services(course):
    return Service.objects.filter(depth=1, course=course)

@register.assignment_tag
def get_services_annotated_list(service):
    return Service.get_annotated_list(parent=service)

@register.simple_tag
def get_rating(comment):
    result = u''
    if comment.content_type:
        red_item = True
        for item in RATING_CHOICES:
            if red_item:
                result += u'<span class="glyphicon glyphicon-star red"></span>'
            else:
                result += u'<span class="glyphicon glyphicon-star-empty"></span>'
            if item[0] == comment.rating:
                red_item = False
        result = u'<div class="rating">%s</div>' % result
    return result


@register.simple_tag
def get_comment_object(comment):
    result = u''
    if comment.content_type:
        result = u'Все %s' % comment.content_type.model_class()._meta.verbose_name_plural
        if comment.object_pk:
            content_object = comment.content_type.get_object_for_this_type(pk=comment.object_pk)
            if isinstance(content_object, ServiceCategory):
                result = u'%s' % content_object.title
    return result