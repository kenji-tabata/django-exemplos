# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Formulario',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('nome', models.CharField(max_length=200)),
                ('cpf', models.CharField(max_length=11)),
                ('preenchido', models.DateTimeField(verbose_name='Data do Preenchimento', default=datetime.datetime(2015, 3, 11, 15, 19, 51, 386190, tzinfo=utc))),
                ('nasc', models.DateField(verbose_name='Data de Nascimento')),
                ('sexo', models.CharField(max_length=4)),
                ('email', models.EmailField(max_length=100, verbose_name='E-mail')),
                ('ddd', models.CharField(max_length=2, verbose_name='DDD')),
                ('telefone', models.CharField(max_length=10)),
                ('end', models.CharField(max_length=200, verbose_name='Endereço')),
                ('bairro', models.CharField(max_length=100)),
                ('cidade', models.CharField(max_length=100)),
                ('estado', models.CharField(max_length=2)),
                ('cep', models.CharField(max_length=9, verbose_name='CEP')),
                ('resp', models.CharField(max_length=100, verbose_name='Resposta')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
