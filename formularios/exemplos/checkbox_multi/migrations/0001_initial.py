# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transportes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('opcoes_transp', models.CharField(blank=True, null=True, max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
