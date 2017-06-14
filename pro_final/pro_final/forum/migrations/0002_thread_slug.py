# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='thread',
            name='slug',
            field=models.SlugField(unique=True, null=True, max_length=100, verbose_name='Identificador', blank=True),
        ),
    ]
