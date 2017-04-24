from __future__ import unicode_literals

from django.db import models
from cuentas.models import Alumno


class ComprobanteDomicilio(models.Model):
    def user_directory_path(self, filename):
        identificador = self.alumno.no_control
        return u"{0}/comprobante_domicilio".format(identificador)

    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    url_documento = models.FileField(upload_to=user_directory_path)

    def __str__(self):  # funcion __str__ regresa un string para identificar al objeto de los demas
        return str(self.alumno.no_control) + " comprobante de domicilio"  # Regresa el numero de control del alumno


class CredencialEstudiante(models.Model):
    def user_directory_path(self, filename):
        identificador = self.alumno.no_control
        return u"{0}/credencial_estudiante".format(identificador)

    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    url_documento = models.FileField(upload_to=user_directory_path)

    def __str__(self):  # funcion __str__ regresa un string para identificar al objeto de los demas
        return str(self.alumno.no_control) + " credencial de estudiante"  # Regresa el numero de control del alumno


class Kardex(models.Model):
    def user_directory_path(self, filename):
        identificador = self.alumno.no_control
        return u"{0}/kardex".format(identificador)

    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    url_documento = models.FileField(upload_to=user_directory_path)

    def __str__(self):  # funcion __str__ regresa un string para identificar al objeto de los demas
        return str(self.alumno.no_control) + " kardex"  # Regresa el numero de control del alumno
