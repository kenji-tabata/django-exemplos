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
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('email', models.EmailField(max_length=75, verbose_name='E-mail')),
                ('assinar', models.CharField(max_length=30, blank=True, verbose_name='Desejo receber os e-mails')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
