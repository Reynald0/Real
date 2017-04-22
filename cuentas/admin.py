from django.contrib import admin
from .models import Alumno

class AlumnoAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'no_control', 'nombre', 'apellido', 'fecha_nac', 'carrera', 'promedio', 'semestre')

admin.site.register(Alumno, AlumnoAdmin)
