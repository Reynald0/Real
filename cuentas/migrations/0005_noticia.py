# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-13 12:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cuentas', '0004_auto_20160112_1026'),
    ]

    operations = [
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('texto', models.TextField()),
                ('fecha_publicacion', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
            ],
        ),
    ]