# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-02 03:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cliente',
            options={'permissions': (('view_cliente', 'Puede ver cliente'),)},
        ),
    ]
