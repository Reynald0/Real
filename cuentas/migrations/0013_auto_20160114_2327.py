# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-15 05:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuentas', '0012_auto_20160114_2320'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumno',
            name='carrera',
            field=models.CharField(default='', max_length=90),
        ),
        migrations.AddField(
            model_name='alumno',
            name='promedio',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='alumno',
            name='semestre',
            field=models.IntegerField(default=0),
        ),
    ]