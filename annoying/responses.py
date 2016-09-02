# -*- coding: utf-8 -*-
from json import dumps
from django.http import HttpResponse


class JSONResponse(HttpResponse):
    def __init__(self, data):
        super(JSONResponse, self).__init__(dumps(data), content_type='application/json')