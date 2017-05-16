# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-16 15:23
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_control', models.IntegerField()),
                ('nombre', models.CharField(max_length=50)),
                ('apellido_paterno', models.CharField(max_length=80)),
                ('apellido_materno', models.CharField(max_length=80)),
                ('fecha_nac', models.DateField(blank=True)),
                ('semestre', models.IntegerField()),
                ('promedio', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Carrera',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('carrera', models.CharField(max_length=90)),
            ],
        ),
        migrations.AddField(
            model_name='alumno',
            name='carrera',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cuentas.Carrera'),
        ),
        migrations.AddField(
            model_name='alumno',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
