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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('data', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Publicado')),
                ('email', models.EmailField(verbose_name='E-mail', max_length=250)),
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
