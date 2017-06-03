# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_announcement_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('description', models.TextField(blank=True, verbose_name='Descrição')),
                ('number', models.IntegerField(blank=True, default=0, verbose_name='Número (ordem)')),
                ('release_date', models.DateField(blank=True, verbose_name='Data de Liberação', null=True)),
                ('created_at', models.DateTimeField(verbose_name='Criado em', auto_now_add=True)),
                ('updated_at', models.DateTimeField(verbose_name='Atualizado em', auto_now=True)),
                ('course', models.ForeignKey(related_name='lessons', verbose_name='Curso', to='courses.Course')),
            ],
            options={
                'verbose_name': 'Aula',
                'verbose_name_plural': 'Aulas',
                'ordering': ['number'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('embedded', models.TextField(blank=True, verbose_name='Vídeo embedded')),
                ('file', models.FileField(upload_to='lessons/materials', blank=True, null=True)),
                ('lesson', models.ForeignKey(related_name='materials', verbose_name='Aula', to='courses.Lesson')),
            ],
            options={
                'verbose_name': 'Matérial',
                'verbose_name_plural': 'Materiais',
            },
            bases=(models.Model,),
        ),
    ]
