# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Combobox',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('tipo', models.CharField(max_length=10, choices=[('Grupo 01', (('i1', 'Item 01'), ('i2', 'Item 02'), ('i3', 'Item 03'))), ('Grupo 02', (('i4', 'Item 04'), ('i5', 'Item 05'), ('i6', 'Item 06'))), ('i7', 'Item 07'), ('i8', 'Item 08'), ('i9', 'Item 09')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
