# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-14 11:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cuentas', '0009_auto_20160113_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True),
        ),
    ]