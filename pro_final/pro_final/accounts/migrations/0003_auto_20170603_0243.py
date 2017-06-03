# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20170515_2022'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='E-mail', unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', to='auth.Group', verbose_name='groups', blank=True, related_query_name='user'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_login',
            field=models.DateTimeField(verbose_name='last login', blank=True, null=True),
        ),
    ]
