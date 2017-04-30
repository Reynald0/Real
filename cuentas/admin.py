# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import Alumno

class AlumnoAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'no_control', 'nombre', 'apellido_paterno', 'apellido_materno', 'fecha_nac', 'carrera',
                    'promedio', 'semestre')

admin.site.register(Alumno, AlumnoAdmin)

admin.site.site_header = "SISTEMA REAL"