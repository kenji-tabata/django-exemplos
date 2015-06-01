# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('assunto', models.CharField(max_length=200)),
                ('data', models.DateTimeField(default=django.utils.timezone.now)),
                ('msg', models.TextField(verbose_name='Mensagem')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('nome', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=150)),
                ('data', models.DateTimeField(verbose_name='Criado em', default=django.utils.timezone.now)),
                ('status', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ('-id',),
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='comentario',
            name='usuario',
            field=models.ForeignKey(to='lista_filtro.Usuario'),
            preserve_default=True,
        ),
    ]
