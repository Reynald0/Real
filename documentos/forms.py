# -*- encoding: utf-8 -*-
from django import forms
from documentos.models import ComprobanteDomicilio, CredencialEstudiante, Kardex


class ComprobanteDomicilioForm(forms.ModelForm):
    class Meta:
        model = ComprobanteDomicilio
        fields = ('url_documento',)


class CredencialEstudianteForm(forms.ModelForm):
    class Meta:
        model = CredencialEstudiante
        fields = ('url_documento',)


class KardexForm(forms.ModelForm):
    class Meta:
        model = Kardex
        fields = ('url_documento',)
