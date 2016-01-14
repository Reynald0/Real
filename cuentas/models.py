from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone

class Alumno(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    no_control = models.IntegerField()
    nombre = models.CharField(max_length=51)
    apellido = models.CharField(max_length=80)
    edad = models.IntegerField()
    carrera = models.CharField(max_length=90)
    semestre = models.IntegerField()
    promedio = models.FloatField()

    def __str__(self):
        return str(self.no_control)

class Noticia(models.Model):
    titulo = models.CharField(max_length=50)
    texto = models.TextField()
    fecha_publicacion = models.DateTimeField(default = timezone.now ,blank=True, null = True)

    def __str__(self):
        return self.titulo
