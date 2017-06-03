# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0005_auto_20170517_1553'),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('title', models.CharField(verbose_name='Título', max_length=100)),
                ('content', models.TextField(verbose_name='Conteúdo')),
                ('created_at', models.DateTimeField(verbose_name='Criado em', auto_now_add=True)),
                ('updated_at', models.DateTimeField(verbose_name='Atualizado em', auto_now=True)),
                ('course', models.ForeignKey(verbose_name='Curso', to='courses.Course', related_name='announcements')),
            ],
            options={
                'verbose_name': 'Anúncio',
                'verbose_name_plural': 'Anúncios',
                'ordering': ['-created_at'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('comment', models.TextField(verbose_name='Comentário')),
                ('created_at', models.DateTimeField(verbose_name='Criado em', auto_now_add=True)),
                ('updated_at', models.DateTimeField(verbose_name='Atualizado em', auto_now=True)),
                ('announcement', models.ForeignKey(verbose_name='Anúncio', to='courses.Announcement', related_name='comments')),
                ('user', models.ForeignKey(verbose_name='usuário', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Comentário',
                'verbose_name_plural': 'Comentários',
                'ordering': ['created_at'],
            },
            bases=(models.Model,),
        ),
    ]
