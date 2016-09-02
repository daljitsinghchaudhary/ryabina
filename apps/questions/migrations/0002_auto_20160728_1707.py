# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailRecipient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email_type', models.SmallIntegerField(verbose_name='\u0442\u0438\u043f \u043e\u043f\u043e\u0432\u0435\u0449\u0435\u043d\u0438\u044f', choices=[(0, '\u0424\u043e\u0440\u043c\u0430 \u043e\u0431\u0440\u0430\u0442\u043d\u043e\u0439 \u0441\u0432\u044f\u0437\u0438'), (1, '\u041e\u0431\u0440\u0430\u0442\u043d\u044b\u0439 \u0437\u0432\u043e\u043d\u043e\u043a'), (2, '\u0417\u0430\u043f\u0438\u0441\u044c \u043d\u0430 \u043f\u0440\u0438\u0451\u043c'), (3, '\u0417\u0430\u0434\u0430\u0442\u044c \u0432\u043e\u043f\u0440\u043e\u0441')])),
                ('recipient_email', models.EmailField(max_length=254, verbose_name='email \u043f\u043e\u043b\u0443\u0447\u0430\u0442\u0435\u043b\u044f')),
                ('description', models.TextField(null=True, verbose_name='\u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True)),
            ],
            options={
                'verbose_name': '\u043f\u043e\u043b\u0443\u0447\u0430\u0442\u0435\u043b\u044c',
                'verbose_name_plural': '\u043f\u043e\u043b\u0443\u0447\u0430\u0442\u0435\u043b\u0438 \u0443\u0432\u0435\u0434\u043e\u043c\u043b\u0435\u043d\u0438\u0439',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, null=True, verbose_name='\u0438\u043c\u044f', blank=True)),
                ('question', models.TextField(verbose_name='\u0432\u043e\u043f\u0440\u043e\u0441')),
                ('answer', models.TextField(null=True, verbose_name='\u043e\u0442\u0432\u0435\u0442', blank=True)),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u0441\u043e\u0437\u0434\u0430\u043d\u043e')),
                ('processed_at', models.DateTimeField(null=True, verbose_name='\u043e\u0431\u0440\u0430\u0431\u043e\u0442\u0430\u043d\u043e', blank=True)),
                ('is_published', models.BooleanField(default=True, verbose_name='\u043e\u043f\u0443\u0431\u043b\u0438\u043a\u043e\u0432\u0430\u043d\u043e')),
            ],
            options={
                'verbose_name': '\u0432\u043e\u043f\u0440\u043e\u0441',
                'verbose_name_plural': '\u0432\u043e\u043f\u0440\u043e\u0441\u044b',
            },
        ),
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, null=True, verbose_name='\u0438\u043c\u044f', blank=True)),
                ('phone', models.CharField(max_length=255, verbose_name='\u0442\u0435\u043b\u0435\u0444\u043e\u043d\u043d\u044b\u0439 \u043d\u043e\u043c\u0435\u0440')),
                ('email', models.EmailField(max_length=254, null=True, verbose_name='email', blank=True)),
                ('procedure', models.SmallIntegerField(verbose_name='\u0432\u0438\u0434 \u043f\u0440\u043e\u0446\u0435\u0434\u0443\u0440\u044b', choices=[(0, '\u041d\u0435 \u0438\u043c\u0435\u0435\u0442 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f'), (1, '\u041f\u0435\u0440\u0432\u0438\u0447\u043d\u0430\u044f \u043a\u043e\u043d\u0441\u0443\u043b\u044c\u0442\u0430\u0446\u0438\u044f'), (2, '\u041f\u043e\u0432\u0442\u043e\u0440\u043d\u044b\u0439 \u043f\u0440\u0438\u0451\u043c')])),
                ('visit_date', models.DateField(verbose_name='\u0434\u0430\u0442\u0430 \u043f\u0440\u0438\u0451\u043c\u0430')),
                ('visit_time', models.TimeField(verbose_name='\u0432\u0440\u0435\u043c\u044f \u043f\u0440\u0438\u0451\u043c\u0430')),
                ('description', models.TextField(null=True, verbose_name='\u043f\u043e\u0436\u0435\u043b\u0430\u043d\u0438\u044f', blank=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u0441\u043e\u0437\u0434\u0430\u043d\u043e')),
                ('processed_at', models.DateTimeField(null=True, verbose_name='\u043e\u0431\u0440\u0430\u0431\u043e\u0442\u0430\u043d\u043e', blank=True)),
            ],
            options={
                'verbose_name': '\u0437\u0430\u043f\u0438\u0441\u044c',
                'verbose_name_plural': '\u0437\u0430\u043f\u0438\u0441\u044c \u043d\u0430 \u043f\u0440\u0438\u0451\u043c',
            },
        ),
        migrations.AlterField(
            model_name='callback',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u0441\u043e\u0437\u0434\u0430\u043d\u043e'),
        ),
    ]
