# -*- coding: utf-8 -*-
from apps.custom_comments.forms import CustomCommentForm
from apps.custom_comments.models import CustomComment


def get_form():
    return CustomCommentForm

def get_model():
    return CustomComment