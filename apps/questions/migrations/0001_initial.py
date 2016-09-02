# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Callback',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, null=True, verbose_name='\u0438\u043c\u044f', blank=True)),
                ('phone', models.CharField(max_length=255, verbose_name='\u0442\u0435\u043b\u0435\u0444\u043e\u043d\u043d\u044b\u0439 \u043d\u043e\u043c\u0435\u0440')),
                ('callback_delta', models.IntegerField(default=0, null=True, verbose_name='\u0432\u0440\u0435\u043c\u044f', blank=True, choices=[[0, '\u0441\u0435\u0439\u0447\u0430\u0441'], [300, '\u0447\u0435\u0440\u0435\u0437 5 \u043c\u0438\u043d\u0443\u0442'], [600, '\u0447\u0435\u0440\u0435\u0437 10 \u043c\u0438\u043d\u0443\u0442'], [900, '\u0447\u0435\u0440\u0435\u0437 15 \u043c\u0438\u043d\u0443\u0442'], [1800, '\u0447\u0435\u0440\u0435\u0437 30 \u043c\u0438\u043d\u0443\u0442'], [3600, '\u0447\u0435\u0440\u0435\u0437 60 \u043c\u0438\u043d\u0443\u0442']])),
                ('callback_time', models.DateTimeField(null=True, verbose_name='\u0432\u0440\u0435\u043c\u044f \u0437\u0432\u043e\u043d\u043a\u0430', blank=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u0434\u0430\u0442\u0430 \u043d\u0430\u0447\u0430\u043b\u0430')),
                ('processed_at', models.DateTimeField(null=True, verbose_name='\u043e\u0431\u0440\u0430\u0431\u043e\u0442\u0430\u043d\u043e', blank=True)),
            ],
            options={
                'verbose_name': '\u043e\u0431\u0440\u0430\u0442\u043d\u044b\u0439 \u0437\u0432\u043e\u043d\u043e\u043a',
                'verbose_name_plural': '\u043e\u0431\u0440\u0430\u0442\u043d\u044b\u0435 \u0437\u0432\u043e\u043d\u043a\u0438',
            },
        ),
    ]
