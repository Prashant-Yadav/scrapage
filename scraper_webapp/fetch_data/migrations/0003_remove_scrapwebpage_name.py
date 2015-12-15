# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fetch_data', '0002_auto_20151203_1320'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scrapwebpage',
            name='name',
        ),
    ]
