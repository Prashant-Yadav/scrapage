# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fetch_data', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScrapWebpage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=70)),
                ('page_url', models.URLField()),
            ],
        ),
        migrations.RemoveField(
            model_name='webpage',
            name='name',
        ),
    ]
