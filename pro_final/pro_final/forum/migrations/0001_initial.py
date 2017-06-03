# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taggit', '0002_auto_20150616_2121'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('reply', models.TextField(verbose_name='Resposta')),
                ('correct', models.BooleanField(default=False, verbose_name='Correta?')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='replies', verbose_name='Autor')),
            ],
            options={
                'ordering': ['-correct', 'created'],
                'verbose_name': 'Resposta',
                'verbose_name_plural': 'Respostas',
            },
        ),
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(verbose_name='Título', max_length=100)),
                ('body', models.TextField(verbose_name='Mensagem')),
                ('views', models.IntegerField(default=0, verbose_name='Visualizações', blank=True)),
                ('answers', models.IntegerField(default=0, verbose_name='Respostas', blank=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='threads', verbose_name='Autor')),
                ('tags', taggit.managers.TaggableManager(verbose_name='Tags', through='taggit.TaggedItem', to='taggit.Tag', help_text='A comma-separated list of tags.')),
            ],
            options={
                'ordering': ['-modified'],
                'verbose_name': 'Tópico',
                'verbose_name_plural': 'Tópicos',
            },
        ),
        migrations.AddField(
            model_name='reply',
            name='thread',
            field=models.ForeignKey(to='forum.Thread', related_name='replies', verbose_name='Tópico'),
        ),
    ]
