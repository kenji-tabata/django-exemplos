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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carro', models.CharField(blank=True, null=True, max_length=50)),
                ('moto', models.CharField(blank=True, null=True, max_length=50)),
                ('onibus', models.CharField(blank=True, null=True, max_length=50)),
                ('bicicleta', models.CharField(blank=True, null=True, max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
