# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-27 21:37
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto', '0002_auto_20160514_1929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='lider_proyecto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lider', to=settings.AUTH_USER_MODEL),
        ),
    ]
