# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_servicecourse_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='servicecourse',
            options={'ordering': ['title'], 'verbose_name': '\u043d\u0430\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435', 'verbose_name_plural': '\u043d\u0430\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u044f'},
        ),
        migrations.AddField(
            model_name='servicecourse',
            name='short_title',
            field=models.CharField(max_length=255, null=True, verbose_name='\u043a\u043e\u0440\u043e\u0442\u043a\u0438\u0439 \u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a', blank=True),
        ),
    ]
