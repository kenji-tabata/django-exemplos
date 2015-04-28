# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('nome', models.CharField(max_length=200)),
                ('cep', models.CharField(max_length=9)),
                ('tel', models.CharField(max_length=13)),
                ('cpf', models.CharField(max_length=14)),
                ('cnpj', models.CharField(max_length=14)),
                ('estados', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
