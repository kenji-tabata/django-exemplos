# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('local_flavor_form_validacao', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='cnpj',
            field=models.CharField(max_length=18),
            preserve_default=True,
        ),
    ]
