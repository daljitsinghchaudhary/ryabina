# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_auto_20160806_0017'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicecourse',
            name='description',
            field=models.TextField(null=True, verbose_name='\u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True),
        ),
    ]
