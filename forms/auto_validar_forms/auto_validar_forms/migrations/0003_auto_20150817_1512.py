# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('auto_validar_forms', '0002_auto_20150313_1514'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('formulario', models.ForeignKey(to='auto_validar_forms.Formulario')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('dado', models.CharField(max_length=200)),
                ('grupos', models.ManyToManyField(to='auto_validar_forms.Formulario', through='auto_validar_forms.Grupo')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='grupo',
            name='pessoa',
            field=models.ForeignKey(to='auto_validar_forms.Pessoa'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='formulario',
            name='preenchido',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 17, 15, 12, 29, 13164, tzinfo=utc), verbose_name='Data do Preenchimento'),
            preserve_default=True,
        ),
    ]
