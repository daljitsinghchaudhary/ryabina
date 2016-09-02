# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0005_auto_20160806_2102'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('path', models.CharField(unique=True, max_length=255)),
                ('depth', models.PositiveIntegerField()),
                ('numchild', models.PositiveIntegerField(default=0)),
                ('title', models.CharField(max_length=255, verbose_name='\u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a')),
            ],
            options={
                'verbose_name': '\u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f',
                'verbose_name_plural': '\u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438 \u0443\u0441\u043b\u0443\u0433',
            },
        ),
        migrations.AlterModelOptions(
            name='servicecourse',
            options={'ordering': ['title'], 'verbose_name': '\u043d\u0430\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435', 'verbose_name_plural': '\u043d\u0430\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u044f \u0443\u0441\u043b\u0443\u0433'},
        ),
    ]
