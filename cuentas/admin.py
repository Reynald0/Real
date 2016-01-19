from django.contrib import admin
from .models import Alumno, Noticia

class AlumnoAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'no_control', 'nombre', 'apellido', 'edad', 'carrera', 'promedio', 'semestre')

admin.site.register(Alumno, AlumnoAdmin)
admin.site.register(Noticia)
