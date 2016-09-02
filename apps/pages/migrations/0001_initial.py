# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import apps.pages.models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FlatPage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='\u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a')),
                ('url', models.CharField(verbose_name=b'URL-\xd0\xb0\xd0\xb4\xd1\x80\xd0\xb5\xd1\x81', unique=True, max_length=255, editable=False)),
                ('slug', models.SlugField(verbose_name='\u043f\u0443\u0442\u044c')),
                ('meta_title', models.CharField(max_length=255, verbose_name='title', blank=True)),
                ('meta_keywords', models.TextField(verbose_name='keywords', blank=True)),
                ('meta_description', models.TextField(verbose_name='description', blank=True)),
                ('content', models.TextField(verbose_name='\u0442\u0435\u043a\u0441\u0442')),
                ('is_published', models.BooleanField(default=True, verbose_name='\u043e\u043f\u0443\u0431\u043b\u0438\u043a\u043e\u0432\u0430\u043d\u043e')),
                ('enable_comments', models.BooleanField(default=False, verbose_name='\u0440\u0430\u0437\u0440\u0435\u0448\u0438\u0442\u044c \u043a\u043e\u043c\u043c\u0435\u043d\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='\u0434\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f')),
                ('template_name', models.CharField(default='default.html', verbose_name='\u0448\u0430\u0431\u043b\u043e\u043d', max_length=100, editable=False)),
                ('order', models.IntegerField(null=True, verbose_name='\u043f\u043e\u0440\u044f\u0434\u043e\u043a', blank=True)),
                ('parent', models.ForeignKey(related_name='children', on_delete=django.db.models.deletion.SET_NULL, verbose_name='\u0440\u043e\u0434\u0438\u0442\u0435\u043b\u044c\u0441\u043a\u0430\u044f \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0430', blank=True, to='pages.FlatPage', null=True)),
                ('sites', models.ManyToManyField(to='sites.Site')),
            ],
            options={
                'ordering': ['order', 'url'],
                'verbose_name': '\u0432\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u044f\u044f \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0430',
                'verbose_name_plural': '\u0432\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u044b',
            },
        ),
        migrations.CreateModel(
            name='FlatPageDoc',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=250, verbose_name='\u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('doc', models.FileField(upload_to=apps.pages.models.get_doc_path, verbose_name='\u0444\u0430\u0439\u043b')),
                ('size', models.IntegerField(default=0, verbose_name='\u0440\u0430\u0437\u043c\u0435\u0440', editable=False)),
                ('order', models.PositiveIntegerField(verbose_name='\u043f\u043e\u0440\u044f\u0434\u043a\u043e\u0432\u044b\u0439 \u043d\u043e\u043c\u0435\u0440')),
                ('page', models.ForeignKey(verbose_name='\u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0430', to='pages.FlatPage')),
            ],
            options={
                'ordering': ['order'],
                'verbose_name': '\u0444\u0430\u0439\u043b \u0432\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0435\u0439 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u044b',
                'verbose_name_plural': '\u0444\u0430\u0439\u043b\u044b \u0432\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0435\u0439 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u044b',
            },
        ),
        migrations.AlterUniqueTogether(
            name='flatpage',
            unique_together=set([('slug',)]),
        ),
    ]
