# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CheckBox',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('email', models.EmailField(max_length=75, verbose_name='E-mail')),
                ('assinar', models.CharField(max_length=10, blank=True, verbose_name='Assinar')),
                ('count', models.IntegerField(verbose_name='Contador')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
