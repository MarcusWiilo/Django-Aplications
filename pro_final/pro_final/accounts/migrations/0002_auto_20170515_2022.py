# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.core.validators
import re


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PasswordReset',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('key', models.CharField(verbose_name='Chave', max_length=100, unique=True)),
                ('created_at', models.DateTimeField(verbose_name='Criado em', auto_now_add=True)),
                ('confirmed', models.BooleanField(verbose_name='Confirmado?', default=False)),
                ('user', models.ForeignKey(verbose_name='Usuario', related_name='resets', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Nova Senha',
                'ordering': ['-created_at'],
                'verbose_name_plural': 'Novas Senhas',
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(verbose_name='Nome do Usuário', validators=[django.core.validators.RegexValidator(re.compile('^[\\w.@+-]+$', 32), 'O nome de usuário só pode conter lestras, digitos ou os seguintes caracteres: @/./+/-/_', 'invalid')], max_length=30, unique=True),
        ),
    ]
