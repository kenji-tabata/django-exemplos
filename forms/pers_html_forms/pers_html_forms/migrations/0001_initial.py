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
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('nome', models.CharField(max_length=200)),
                ('cpf', models.CharField(max_length=14)),
                ('preenchido', models.DateTimeField(verbose_name='Data do Preenchimento', default=datetime.datetime(2015, 4, 7, 12, 24, 53, 678092, tzinfo=utc))),
                ('nasc', models.DateField(verbose_name='Data de Nascimento')),
                ('sexo', models.CharField(max_length=4)),
                ('email', models.EmailField(verbose_name='E-mail', max_length=100)),
                ('ddd', models.CharField(verbose_name='DDD', max_length=2)),
                ('telefone', models.CharField(max_length=10)),
                ('end', models.CharField(verbose_name='Endereço', max_length=200)),
                ('bairro', models.CharField(max_length=100)),
                ('cidade', models.CharField(max_length=100)),
                ('estado', models.CharField(max_length=2)),
                ('cep', models.CharField(verbose_name='CEP', max_length=9)),
                ('resp', models.CharField(verbose_name='Resposta', max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
