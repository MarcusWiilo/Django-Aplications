# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(max_length=30, unique=True, verbose_name='Nome do Usuário')),
                ('email', models.EmailField(max_length=75, unique=True, verbose_name='E-mail')),
                ('name', models.CharField(blank=True, max_length=100, verbose_name='Nome')),
                ('is_active', models.BooleanField(default=True, verbose_name='Está ativo?')),
                ('is_staff', models.BooleanField(default=False, verbose_name='É da equipe?')),
                ('date_joined', models.DateTimeField(verbose_name='Data de Entrada', auto_now_add=True)),
                ('groups', models.ManyToManyField(related_name='user_set', to='auth.Group', related_query_name='user', verbose_name='groups', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of his/her group.')),
                ('user_permissions', models.ManyToManyField(related_name='user_set', to='auth.Permission', related_query_name='user', verbose_name='user permissions', blank=True, help_text='Specific permissions for this user.')),
            ],
            options={
                'verbose_name_plural': 'Usuários',
                'verbose_name': 'Usuário',
            },
            bases=(models.Model,),
        ),
    ]
