# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('data', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Publicado')),
                ('conteudo', models.TextField(verbose_name='Conteúdo')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
