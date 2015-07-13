# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('testando_model', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contato',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 2, 14, 51, 40, 430955, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
