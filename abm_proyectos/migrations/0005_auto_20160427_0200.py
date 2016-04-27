# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-27 02:00
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('abm_clientes', '0002_auto_20160427_0200'),
        ('abm_proyectos', '0004_auto_20160427_0058'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto',
            name='cliente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='abm_clientes.Cliente'),
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='fechaCreacion',
            field=models.DateField(default=datetime.datetime(2016, 4, 27, 2, 0, 1, 958135, tzinfo=utc)),
        ),
    ]