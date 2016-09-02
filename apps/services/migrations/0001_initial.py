# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('path', models.CharField(unique=True, max_length=255)),
                ('depth', models.PositiveIntegerField()),
                ('numchild', models.PositiveIntegerField(default=0)),
                ('title', models.CharField(max_length=255, verbose_name='\u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a')),
                ('description', models.TextField(null=True, verbose_name='\u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True)),
                ('min_price', models.IntegerField(null=True, verbose_name='\u043c\u0438\u043d\u0438\u043c\u0430\u043b\u044c\u043d\u0430\u044f \u0446\u0435\u043d\u0430', blank=True)),
                ('max_price', models.IntegerField(null=True, verbose_name='\u043c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u0430\u044f \u0446\u0435\u043d\u0430', blank=True)),
                ('url', models.CharField(max_length=255, null=True, verbose_name='\u0441\u0441\u044b\u043b\u043a\u0430 \u043d\u0430 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0443', blank=True)),
                ('button', models.CharField(max_length=255, null=True, verbose_name='\u043d\u0430\u0434\u043f\u0438\u0441\u044c \u043d\u0430 \u043a\u043d\u043e\u043f\u043a\u0435', blank=True)),
                ('on_main_page', models.BooleanField(default=False, verbose_name='\u043d\u0430 \u0433\u043b\u0430\u0432\u043d\u043e\u0439 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0435')),
            ],
            options={
                'verbose_name': '\u0443\u0441\u043b\u0443\u0433\u0430',
                'verbose_name_plural': '\u0443\u0441\u043b\u0443\u0433\u0438',
            },
        ),
        migrations.CreateModel(
            name='ServiceIcon',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.FileField(upload_to=b'img/courses', verbose_name='\u0440\u0438\u0441\u0443\u043d\u043e\u043a')),
                ('title', models.CharField(max_length=255, null=True, verbose_name='\u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a', blank=True)),
            ],
            options={
                'verbose_name': '\u0438\u043a\u043e\u043d\u043a\u0430',
                'verbose_name_plural': '\u0438\u043a\u043e\u043d\u043a\u0438 \u0443\u0441\u043b\u0443\u0433',
            },
        ),
        migrations.AddField(
            model_name='service',
            name='icon',
            field=models.ForeignKey(verbose_name=b'\xd0\xb8\xd0\xba\xd0\xbe\xd0\xbd\xd0\xba\xd0\xb0', blank=True, to='services.ServiceIcon', null=True),
        ),
    ]
