# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Webpage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=70)),
                ('url', models.URLField()),
                ('paragraphs', models.TextField()),
                ('links', models.URLField()),
                ('headings', models.CharField(max_length=200)),
            ],
        ),
    ]
