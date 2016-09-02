# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ParallaxImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'img/parallax', verbose_name='\u0440\u0438\u0441\u0443\u043d\u043e\u043a')),
                ('title', models.CharField(max_length=255, null=True, verbose_name='\u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a', blank=True)),
            ],
            options={
                'verbose_name': '\u043a\u0430\u0440\u0442\u0438\u043d\u043a\u0430',
                'verbose_name_plural': '\u043f\u0430\u0440\u0430\u043b\u0430\u043a\u0441',
            },
        ),
        migrations.CreateModel(
            name='RotatingImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'img/slideshow', verbose_name='\u0440\u0438\u0441\u0443\u043d\u043e\u043a')),
                ('title', models.CharField(max_length=255, null=True, verbose_name='\u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a', blank=True)),
                ('content', models.TextField(null=True, verbose_name='\u0441\u043e\u0434\u0435\u0440\u0436\u0438\u043c\u043e\u0435', blank=True)),
                ('url', models.CharField(max_length=255, null=True, verbose_name='\u0441\u0441\u044b\u043b\u043a\u0430 \u043d\u0430 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0443', blank=True)),
                ('button', models.CharField(max_length=255, null=True, verbose_name='\u043d\u0430\u0434\u043f\u0438\u0441\u044c \u043d\u0430 \u043a\u043d\u043e\u043f\u043a\u0435', blank=True)),
            ],
            options={
                'verbose_name': '\u043a\u0430\u0440\u0442\u0438\u043d\u043a\u0430',
                'verbose_name_plural': '\u0441\u043b\u0430\u0439\u0434\u0448\u043e\u0443',
            },
        ),
    ]
