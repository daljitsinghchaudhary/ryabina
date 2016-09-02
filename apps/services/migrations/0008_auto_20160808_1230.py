# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0007_auto_20160807_2025'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='servicecategory',
            options={'ordering': ('title',), 'verbose_name': '\u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f', 'verbose_name_plural': '\u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438 \u0443\u0441\u043b\u0443\u0433'},
        ),
        migrations.AlterModelOptions(
            name='servicecourse',
            options={'ordering': ('title',), 'verbose_name': '\u043d\u0430\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435', 'verbose_name_plural': '\u043d\u0430\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u044f \u0443\u0441\u043b\u0443\u0433'},
        ),
        migrations.AddField(
            model_name='servicecategory',
            name='description',
            field=models.TextField(null=True, verbose_name='\u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True),
        ),
        migrations.AddField(
            model_name='servicecourse',
            name='button',
            field=models.CharField(max_length=255, null=True, verbose_name='\u043d\u0430\u0434\u043f\u0438\u0441\u044c \u043d\u0430 \u043a\u043d\u043e\u043f\u043a\u0435', blank=True),
        ),
        migrations.AddField(
            model_name='servicecourse',
            name='url',
            field=models.CharField(max_length=255, null=True, verbose_name='\u0441\u0441\u044b\u043b\u043a\u0430 \u043d\u0430 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0443', blank=True),
        ),
    ]
