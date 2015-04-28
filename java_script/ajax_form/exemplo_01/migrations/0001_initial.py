# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('telefone', models.CharField(blank=True, max_length=15, verbose_name='Telefone')),
                ('email', models.EmailField(max_length=200, verbose_name='E-mail')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
