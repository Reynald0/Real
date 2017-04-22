from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone

class Carrera(models.Model):
    id = models.AutoField(primary_key=True) #Atributo id es tipo INT y es auto incrementable
    carrera = models.CharField(max_length=90) #Atributo carrera es tipo de dato Char y su tamanio maximo es 90

    def __str__(self):
        return str(self.carrera)


class Alumno(models.Model): #Se crea el objeto Alumno, en la base de datos es una tabla
    user = models.OneToOneField(User, on_delete=models.CASCADE) #Atributo user que es una llave foranea, relacion 1 a 1
    no_control = models.IntegerField() #Atributo no_control es tipo de dato Integer
    nombre = models.CharField(max_length=50) # Atributo nombre es tipo de dato Char y su tamanio maximo es 50
    apellido = models.CharField(max_length=80) #Atributo apellido es tipo de dato Char y su tamanio maximo es 80
    fecha_nac = models.DateField(blank=True) #Atributo edad es tipo de dato Date
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE) 
    semestre = models.IntegerField() #Atributo semestre es tipo de dato Integer
    promedio = models.FloatField() #Atributo promedio es tipo de dato Float (Decimal)

    def __str__(self): #funcion __str__ regresa un string para identificar al objeto de los demas
        return str(self.no_control) #Regresa el no_control en forma de string


