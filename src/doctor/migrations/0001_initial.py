# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-28 22:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('rut', models.CharField(max_length=10, unique=True, verbose_name='RUT')),
                ('direccion', models.CharField(max_length=100)),
                ('fecha_nacimiento', models.DateField(verbose_name='Fecha de Nacimiento')),
                ('fecha_ingreso_clinica', models.DateField(auto_now_add=True, verbose_name='Fecha de ingreso a la clínica')),
                ('edad', models.PositiveSmallIntegerField(verbose_name='Edad del doctor')),
            ],
        ),
    ]
