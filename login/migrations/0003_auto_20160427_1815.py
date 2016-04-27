# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-27 18:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('abm_clientes', '0002_auto_20160427_0200'),
        ('login', '0002_auto_20160427_0200'),
    ]

    operations = [
        migrations.RenameField(
            model_name='telefono',
            old_name='valor',
            new_name='numero',
        ),
        migrations.AddField(
            model_name='telefono',
            name='cliente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='abm_clientes.Cliente'),
        ),
        migrations.AddField(
            model_name='telefono',
            name='usuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='login.Usuario'),
        ),
    ]