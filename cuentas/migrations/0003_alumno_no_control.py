# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-12 12:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuentas', '0002_auto_20160112_0651'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumno',
            name='no_control',
            field=models.IntegerField(default=0),
        ),
    ]
