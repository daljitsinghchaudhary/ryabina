# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('slideshow', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'img/contacts', verbose_name='\u0440\u0438\u0441\u0443\u043d\u043e\u043a')),
                ('title', models.CharField(max_length=255, null=True, verbose_name='\u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a', blank=True)),
            ],
            options={
                'verbose_name': '\u043a\u0430\u0440\u0442\u0438\u043d\u043a\u0430',
                'verbose_name_plural': '\u043a\u043e\u043d\u0442\u0430\u043a\u0442\u044b',
            },
        ),
        migrations.AlterField(
            model_name='rotatingimage',
            name='content',
            field=tinymce.models.HTMLField(null=True, verbose_name='\u0441\u043e\u0434\u0435\u0440\u0436\u0438\u043c\u043e\u0435', blank=True),
        ),
    ]
