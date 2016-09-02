# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_service_short_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceCourse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, null=True, verbose_name='\u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a', blank=True)),
                ('on_main_page', models.BooleanField(default=False, verbose_name='\u043d\u0430 \u0433\u043b\u0430\u0432\u043d\u043e\u0439 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0435')),
                ('icon', models.ForeignKey(verbose_name=b'\xd0\xb8\xd0\xba\xd0\xbe\xd0\xbd\xd0\xba\xd0\xb0', blank=True, to='services.ServiceIcon', null=True)),
            ],
            options={
                'verbose_name': '\u043d\u0430\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435',
                'verbose_name_plural': '\u043d\u0430\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u044f',
            },
        ),
        migrations.RemoveField(
            model_name='service',
            name='icon',
        ),
        migrations.AddField(
            model_name='service',
            name='course',
            field=models.ForeignKey(verbose_name=b'\xd0\xbd\xd0\xb0\xd0\xbf\xd1\x80\xd0\xb0\xd0\xb2\xd0\xbb\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5', blank=True, to='services.ServiceCourse', null=True),
        ),
    ]
