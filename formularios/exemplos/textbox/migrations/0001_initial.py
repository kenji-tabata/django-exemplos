# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Postagens',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('titulo', models.CharField(max_length=200)),
                ('data', models.DateTimeField(verbose_name='Publicado', default=django.utils.timezone.now)),
                ('email', models.EmailField(max_length=250, verbose_name='E-mail')),
                ('url', models.URLField(verbose_name='Site')),
                ('rating', models.DecimalField(max_digits=9, decimal_places=1)),
                ('like', models.IntegerField()),
                ('conteudo', models.TextField(verbose_name='Conteúdo')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
