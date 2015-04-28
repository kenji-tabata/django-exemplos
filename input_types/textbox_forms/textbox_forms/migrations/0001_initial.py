# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TextBox',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('nome', models.CharField(max_length=200)),
                ('email', models.EmailField(verbose_name='E-mail', max_length=250)),
                ('url', models.URLField(verbose_name='Site')),
                ('data', models.DateTimeField(verbose_name='Data publicada')),
                ('valor', models.DecimalField(max_digits=9, verbose_name='Valor R$', decimal_places=2)),
                ('numero', models.IntegerField(verbose_name='Número')),
                ('mensagem', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
