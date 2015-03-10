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
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('tipo', models.CharField(max_length=10, choices=[('i1', 'Item 01'), ('i2', 'Item 02'), ('i3', 'Item 03')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
