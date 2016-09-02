# -*- coding: utf-8 -*-
import os
import random
import string


def create_dir(dir_path):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

def id_generator(size=10, chars=string.ascii_uppercase + string.digits):
    return u''.join(random.choice(chars) for x in range(size))

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip