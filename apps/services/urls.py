# coding=utf-8
from django.conf.urls import url
from apps.services.views import PriceView, ViewQRCode

urlpatterns =[
    url(r'^price/$', PriceView.as_view(), name='price'),
    url(r'^qrCode/', ViewQRCode.as_view(), name='qr_code'),
]