# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_auto_20160728_1707'),
    ]

    operations = [
        migrations.CreateModel(
            name='VisitPurpose',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, null=True, verbose_name='\u043d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435', blank=True)),
            ],
            options={
                'verbose_name': '\u043d\u0430\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435',
                'verbose_name_plural': '\u043d\u0430\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u044f \u0437\u0430\u043f\u0438\u0441\u0438',
            },
        ),
        migrations.AlterModelOptions(
            name='callback',
            options={'verbose_name': '\u043e\u0431\u0440\u0430\u0442\u043d\u044b\u0439 \u0437\u0432\u043e\u043d\u043e\u043a', 'verbose_name_plural': '\u043e\u0431\u0440\u0430\u0442\u043d\u044b\u0439 \u0437\u0432\u043e\u043d\u043e\u043a'},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'verbose_name': '\u0432\u043e\u043f\u0440\u043e\u0441', 'verbose_name_plural': '\u0437\u0430\u0434\u0430\u0442\u044c \u0432\u043e\u043f\u0440\u043e\u0441'},
        ),
        migrations.AlterField(
            model_name='emailrecipient',
            name='recipient_email',
            field=models.EmailField(max_length=254, verbose_name='e-mail \u043f\u043e\u043b\u0443\u0447\u0430\u0442\u0435\u043b\u044f'),
        ),
        migrations.AlterField(
            model_name='question',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='e-mail'),
        ),
        migrations.AlterField(
            model_name='question',
            name='is_published',
            field=models.BooleanField(default=False, verbose_name='\u043e\u043f\u0443\u0431\u043b\u0438\u043a\u043e\u0432\u0430\u043d\u043e'),
        ),
        migrations.AlterField(
            model_name='visit',
            name='email',
            field=models.EmailField(max_length=254, null=True, verbose_name='e-mail', blank=True),
        ),
        migrations.AddField(
            model_name='visit',
            name='purpose',
            field=models.ForeignKey(verbose_name=b'\xd0\xbd\xd0\xb0\xd0\xbf\xd1\x80\xd0\xb0\xd0\xb2\xd0\xbb\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5', blank=True, to='questions.VisitPurpose', null=True),
        ),
    ]
