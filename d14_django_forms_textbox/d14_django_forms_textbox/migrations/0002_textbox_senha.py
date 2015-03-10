# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('d14_django_forms_textbox', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='textbox',
            name='senha',
            field=models.CharField(default=datetime.datetime(2015, 3, 10, 19, 52, 38, 333673, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
    ]
