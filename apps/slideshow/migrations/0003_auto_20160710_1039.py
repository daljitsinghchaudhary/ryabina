# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slideshow', '0002_auto_20160710_0943'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ContactImage',
            new_name='ContactsImage',
        ),
    ]
