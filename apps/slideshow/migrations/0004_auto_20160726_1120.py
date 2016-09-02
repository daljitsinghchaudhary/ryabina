# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slideshow', '0003_auto_20160710_1039'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactsImagesType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, null=True, verbose_name='\u043d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435', blank=True)),
            ],
            options={
                'verbose_name': '\u0442\u0438\u043f \u043a\u0430\u0440\u0442\u0438\u043d\u043a\u0438',
                'verbose_name_plural': '\u0442\u0438\u043f\u044b \u043a\u0430\u0440\u0442\u0438\u043d\u043e\u043a',
            },
        ),
        migrations.AddField(
            model_name='contactsimage',
            name='image_type',
            field=models.ForeignKey(verbose_name=b'\xd1\x82\xd0\xb8\xd0\xbf', blank=True, to='slideshow.ContactsImagesType', null=True),
        ),
    ]
