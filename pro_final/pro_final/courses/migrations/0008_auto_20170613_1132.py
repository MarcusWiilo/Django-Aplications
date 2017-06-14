# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_lesson_material'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['created_at'], 'verbose_name_plural': 'Lista de Cursos Para Aprovar', 'verbose_name': 'Comentário'},
        ),
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ['name'], 'verbose_name_plural': 'Criar Cursos', 'verbose_name': 'Curso'},
        ),
        migrations.AlterModelOptions(
            name='enrollment',
            options={'verbose_name_plural': 'Lista de Plano de Ensino Para Aprovar', 'verbose_name': 'Inscrição'},
        ),
        migrations.AlterModelOptions(
            name='lesson',
            options={'ordering': ['number'], 'verbose_name_plural': 'Lista de Temas de Curso Para Aprovar', 'verbose_name': 'Aula'},
        ),
        migrations.AlterModelOptions(
            name='material',
            options={'verbose_name_plural': 'Lista de Conteudo Para Aprovar', 'verbose_name': 'Matérial'},
        ),
    ]
