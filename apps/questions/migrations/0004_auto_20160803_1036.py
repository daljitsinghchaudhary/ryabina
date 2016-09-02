# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0003_auto_20160730_1257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='callback',
            name='callback_delta',
            field=models.IntegerField(default=0, null=True, verbose_name='\u043f\u0435\u0440\u0435\u0437\u0432\u043e\u043d\u0438\u0442\u044c', blank=True, choices=[[0, '\u0441\u0435\u0439\u0447\u0430\u0441'], [300, '\u0447\u0435\u0440\u0435\u0437 5 \u043c\u0438\u043d\u0443\u0442'], [600, '\u0447\u0435\u0440\u0435\u0437 10 \u043c\u0438\u043d\u0443\u0442'], [900, '\u0447\u0435\u0440\u0435\u0437 15 \u043c\u0438\u043d\u0443\u0442'], [1800, '\u0447\u0435\u0440\u0435\u0437 30 \u043c\u0438\u043d\u0443\u0442'], [3600, '\u0447\u0435\u0440\u0435\u0437 60 \u043c\u0438\u043d\u0443\u0442']]),
        ),
    ]
