from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

class Noticia(models.Model):
    titulo = models.CharField(max_length=50)
    texto = models.TextField()
    fecha_publicacion = models.DateTimeField(default = timezone.now ,blank=True, null = True)

    def __str__(self):
        return self.titulo
