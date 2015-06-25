# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('local_flavor_estados', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='combobox',
            name='cep',
        ),
    ]
