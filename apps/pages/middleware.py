# -*- coding: utf-8 -*-
from django.http import Http404
from django.conf import settings

from apps.pages.views import FlatpageView


class FlatpageFallbackMiddleware(object):
    def process_response(self, request, response):
        if response.status_code != 404:
            return response
        try:
            return FlatpageView.as_view()(request, request.path)
        except Http404:
            return response
        except:
            if settings.DEBUG:
                raise
            return response

