# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('d18_django_forms_checkbox_multi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkbox',
            name='tipo',
            field=models.CharField(max_length=100),
            preserve_default=True,
        ),
    ]
