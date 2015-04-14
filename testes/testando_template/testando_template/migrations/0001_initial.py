# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=250, verbose_name='E-mail')),
                ('data', models.DateTimeField(default=datetime.datetime(2015, 4, 2, 11, 41, 31, 130956, tzinfo=utc))),
                ('mensagem', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
