# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-27 19:37
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto', '0010_auto_20160427_1935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='fecha_creacion',
            field=models.DateField(default=datetime.datetime(2016, 4, 27, 19, 37, 13, 197984, tzinfo=utc)),
        ),
    ]