# coding=utf-8
from django.conf.urls import url
from apps.pages.views import MainView, FaviconView, ServicesView, ContactsView

urlpatterns =[
    url(r'^favicon.ico$', FaviconView.as_view(), name='favicon'),
    url(r'^$', MainView.as_view(), name='main'),
    url(r'^services/$', ServicesView.as_view(), name='services'),
    url(r'^services/(?P<category_id>[1234567890]+)/$', ServicesView.as_view(), name='service_category'),
    url(r'^contacts/$', ContactsView.as_view(), name='contacts'),
]