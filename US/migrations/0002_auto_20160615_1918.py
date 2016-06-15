# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-15 23:18
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sprint', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('US', '0001_initial'),
        ('proyecto', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='us',
            name='proyecto',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='uss', to='proyecto.Proyecto'),
        ),
        migrations.AddField(
            model_name='us',
            name='sprint',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='uss', to='sprint.Sprint'),
        ),
        migrations.AddField(
            model_name='us',
            name='tipoUS',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='uss', to='US.TipoUS'),
        ),
        migrations.AddField(
            model_name='us',
            name='usuario_asignado',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='actividades',
            name='tipoUS',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='actividades', to='US.TipoUS'),
        ),
    ]