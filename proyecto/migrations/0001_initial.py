# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-16 00:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cliente', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('fecha_creacion', models.DateField(auto_now=True)),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('descripcion', models.TextField(help_text=b'Introduzca una breve rese\xc3\xb1a del proyecto', max_length=140, null=True)),
                ('estado', models.CharField(choices=[(b'PEN', b'Pendiente'), (b'ANU', b'Anulado'), (b'ACT', b'Activo'), (b'FIN', b'Finalizado')], default=b'PEN', help_text=b'Estado del proyecto', max_length=3)),
                ('observaciones', models.TextField(default=b'No hay observaciones', max_length=140, null=True)),
                ('activo', models.BooleanField(default=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='cliente.Cliente')),
                ('lider_proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lider', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (('view_proyecto', 'Puede ver proyecto'), ('change_estado', 'Puede cambiar el estado del proyecto')),
            },
        ),
    ]
