# coding=utf-8
from django.conf.urls import url
from apps.questions.views import CallbackView, QuestionView, VisitView


urlpatterns =[
    url(r'^callback/$', CallbackView.as_view(), name='callback'),
    url(r'^question/$', QuestionView.as_view(), name='question'),
    url(r'^visit/$', VisitView.as_view(), name='visit')
]