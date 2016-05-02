# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-02 04:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('activo', models.BooleanField(default=True)),
            ],
            options={
                'permissions': (('can_view', 'Puede ver cliente'),),
            },
        ),
    ]
