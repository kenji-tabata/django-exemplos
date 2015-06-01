# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ajax_csrf', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('assunto', models.CharField(max_length=200)),
                ('data', models.DateTimeField(default=django.utils.timezone.now)),
                ('msg', models.TextField(verbose_name='Mensagem')),
                ('usuario', models.ForeignKey(to='ajax_csrf.Usuario')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
