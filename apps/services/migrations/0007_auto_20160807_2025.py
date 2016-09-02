# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0006_auto_20160807_1810'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='button',
        ),
        migrations.RemoveField(
            model_name='service',
            name='description',
        ),
        migrations.RemoveField(
            model_name='service',
            name='on_main_page',
        ),
        migrations.RemoveField(
            model_name='service',
            name='short_title',
        ),
        migrations.RemoveField(
            model_name='service',
            name='url',
        ),
        migrations.RemoveField(
            model_name='servicecategory',
            name='depth',
        ),
        migrations.RemoveField(
            model_name='servicecategory',
            name='numchild',
        ),
        migrations.RemoveField(
            model_name='servicecategory',
            name='path',
        ),
        migrations.AddField(
            model_name='service',
            name='category',
            field=models.ManyToManyField(to='services.ServiceCategory', verbose_name=b'\xd0\xba\xd0\xb0\xd1\x82\xd0\xb5\xd0\xb3\xd0\xbe\xd1\x80\xd0\xb8\xd1\x8f', blank=True),
        ),
    ]
