# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('editar_reg_forms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formulario',
            name='preenchido',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 13, 15, 14, 46, 528675, tzinfo=utc), verbose_name='Data do Preenchimento'),
            preserve_default=True,
        ),
    ]
