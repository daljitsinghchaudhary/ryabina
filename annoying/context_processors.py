# -*- coding: utf-8 -*-
from django.conf import settings
from django.contrib.sites.models import Site
from apps.questions.forms import CallbackForm, QuestionForm, VisitForm


def site_constants(request):
    current_site = Site.objects.get_current()
    return {
        'SITE_TITLE': settings.SITE_TITLE,
        'DOMAIN': current_site.domain,
        'DEBUG': settings.DEBUG
    }


def questions_forms(request):
    return {
        'question_form': QuestionForm(request.POST or None),
        'visit_form': VisitForm(request.POST or None),
        'callback_form': CallbackForm(request.POST or None),
    }