from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

class Noticia(models.Model):
    titulo = models.CharField(max_length=50) #Crea un campo del tipo 'char' con una extension maxima de 50 caracteres
    texto = models.TextField() #Crea un campo del tipo 'campo de texto'
    #Crea un campo del tipo fecha y hora. Por defecto la fecha y hora actual, puede ser vacio, puede ser nulo.
    fecha_publicacion = models.DateTimeField(default = timezone.now ,blank=True, null = True)

    def __str__(self): #Metodo que permite asignarle un string al objeto para poder ser identificado por las personas
        return self.titulo #regresa el titulo del objeto, en este caso de la clase Noticia
