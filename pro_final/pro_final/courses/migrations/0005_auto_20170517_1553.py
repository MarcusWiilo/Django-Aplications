# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0004_auto_20170509_1940'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('status', models.IntegerField(blank=True, verbose_name='Situação', default=1, choices=[(0, 'Pendente'), (1, 'Aprovado'), (2, 'Cancelado')])),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(verbose_name='Atualizado em', auto_now=True)),
                ('course', models.ForeignKey(related_name='enrollments', to='courses.Course', verbose_name='Curso')),
                ('user', models.ForeignKey(related_name='enrollments', to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'verbose_name_plural': 'Inscrições',
                'verbose_name': 'Inscrição',
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='enrollment',
            unique_together=set([('user', 'course')]),
        ),
    ]
