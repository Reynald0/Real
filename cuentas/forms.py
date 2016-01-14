# -*- encoding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from .models import Alumno

class RegistroAlumno(forms.Form):
    # OPCIONES maneja tuplas, donde el primer valor de la linea 9 es el valor que se guardara en la base de datos
    # y el segundo valor es el que aparecera en el formulario
    OPCIONES = (
    ('Ing. Sistemas Computacionales', "Ing. Sistemas Computacionales",),
    ('Ing. Industrial', 'Ing. Industrial'),
    )
    #usuario     = forms.CharField(min_length=5,widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Usuario'}))
    #carrera     = forms.ChoiceField(choices=OPCIONES, widget=forms.Select(attrs={'class': 'form-control','placeholder':'Edad'}))
    usuario     = forms.CharField(help_text='Nombre de usuario',min_length=5,widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Usuario', 'id': 'Usuario'}))
    clave       = forms.CharField(min_length=5, widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':'Contraseña', 'id': 'Clave'}))
    email       = forms.EmailField(label='E-Mail',widget=forms.EmailInput(attrs={'class': 'form-control','placeholder':'Correo electrónico', 'id': 'E-Mail'}))
    no_control  = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control','placeholder':'Número de control', 'id': 'No control'}))
    nombre      = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Nombre', 'id': 'Nombre'}))
    apellido    = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Apellido', 'id': 'Apellido'}))
    edad        = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control','placeholder':'Edad', 'id': 'Edad'}))
    carrera     = forms.ChoiceField(choices=OPCIONES, widget=forms.Select(attrs={'class': 'form-control','placeholder':'Edad', 'id': 'Carrera'}))
    promedio    = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control','placeholder':'Promedio', 'id': 'Promedio'}))
    semestre    = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control','placeholder':'Semestre', 'id': 'Semestre'}))

    def clean_usuario(self):
        #Comprueba que no exista un usuario igual en la base de datos
        usuario = str(self.cleaned_data['usuario'])
        if User.objects.filter(first_name=usuario):
            raise forms.ValidationError('El usuario ya existe!')
        return usuario

    def clean_no_control(self):
        #Comprueba que no exista un numero de control igual en la base de datos
        no_control = str(self.cleaned_data['no_control'])
        if Alumno.objects.filter(no_control=no_control):
            raise forms.ValidationError('El número de control ya existe!')
        return no_control

    def clean_email(self):
        #Comprueba que no exista un email igual en la base de datos
        email = self.cleaned_data['email']
        if User.objects.filter(email=email):
            raise forms.ValidationError('El correo ya fue registrado!')
        return email

class LogAlumno(forms.Form):
    usuario = forms.CharField(min_length=5, widget=forms.TextInput(attrs={'class': 'form-control'}))
    clave = forms.CharField(min_length=5, widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean_usuario(self):
        #Comprueba que exista un username en la base de datos
        usuario = self.cleaned_data['usuario']
        if not User.objects.filter(username=usuario):
            raise forms.ValidationError('El nombre de usuario no existe!')
        return usuario
