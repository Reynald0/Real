# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from cuentas.models import Alumno
from .validators import validate_file_extension


def ubicacion_comprobante_domicilio(instace, filename):
    identificador = instace.alumno.no_control
    return u"documentos/{0}/comprobante_domicilio/{1}".format(identificador, filename)

class ComprobanteDomicilio(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    url_documento = models.FileField(upload_to=ubicacion_comprobante_domicilio, validators=[validate_file_extension])

    def __str__(self):  # funcion __str__ regresa un string para identificar al objeto de los demas
        return str(self.alumno.no_control) + " comprobante de domicilio"  # Regresa el numero de control del alumno

    class Meta:
        verbose_name_plural = "Comprobante de domicilio"


def ubicacion_credencial_estudiante(instace, filename):
    identificador = instace.alumno.no_control
    return u"documentos/{0}/credencial_estudiante/{1}".format(identificador, filename)

class CredencialEstudiante(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    url_documento = models.FileField(upload_to=ubicacion_credencial_estudiante)

    def __str__(self):  # funcion __str__ regresa un string para identificar al objeto de los demas
        return str(self.alumno.no_control) + " credencial de estudiante"  # Regresa el numero de control del alumno

    class Meta:
        verbose_name_plural = "Credencial de estudiante"

def ubicacion_kardex(instace, filename):
        identificador = instace.alumno.no_control
        return u"documentos/{0}/kardex/{1}".format(identificador,filename)

class Kardex(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    url_documento = models.FileField(upload_to=ubicacion_kardex)

    def __str__(self):  # funcion __str__ regresa un string para identificar al objeto de los demas
        return str(self.alumno.no_control) + " kardex"  # Regresa el numero de control del alumno

    class Meta:
        verbose_name_plural = "Kardex"