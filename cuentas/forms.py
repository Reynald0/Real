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
    ('Ing. Civil', 'Ing. Civil'),
    ('Ing. Quimica', 'Ing. Quimica'),
    ('Ing. Petrolera', 'Ing. Petrolera'),
    ('Ing. Ambiental', 'Ing. Ambiental'),
    ('Ing. Bioquimica', 'Ing. Bioquimica'),
    ('Ing. Informatica', 'Ing. Informatica'),
    ('Lic. en Administracion', 'Lic. en Administracion'),
    ('Ing. Gestion Empresarial', 'Ing. Gestion Empresarial'),
    ('Ing. en Tecnologias de la Informacion y Comunicaciones', 'Ing. TICs'),
    )
    #usuario     = forms.CharField(help_text='Nombre de usuario',min_length=5,widget=forms.TextInput(attrs={'placeholder':'Usuario', 'id': 'Usuario'}))
    #usuario     = forms.CharField(min_length=5,widget=forms.TextInput(attrs={'placeholder':'Usuario'}))
    #carrera     = forms.ChoiceField(choices=OPCIONES, widget=forms.Select(attrs={'placeholder':'Edad'}))
    usuario     = forms.CharField(min_length=5,widget=forms.TextInput(attrs={'placeholder':'Usuario', 'id': 'Usuario'}))
    clave       = forms.CharField(min_length=5, widget=forms.PasswordInput(attrs={'placeholder':'Contraseña', 'id': 'Clave'}))
    email       = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Correo electrónico', 'id': 'Email', 'type': 'email', 'class':'validate'}))
    no_control  = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'Número de control', 'id': 'No control', 'length' : '8'}))
    nombre      = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Nombre', 'id': 'Nombre'}))
    apellido    = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Apellido', 'id': 'Apellido'}))
    edad        = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'Edad', 'id': 'Edad'}))
    carrera     = forms.ChoiceField(choices=OPCIONES, widget=forms.Select(attrs={'placeholder':'Edad', 'id': 'Carrera'}))
    promedio    = forms.FloatField(widget=forms.NumberInput(attrs={'placeholder':'Promedio', 'id': 'Promedio'}))
    semestre    = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'Semestre', 'id': 'Semestre'}))

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
    usuario = forms.CharField(min_length=5,widget=forms.TextInput(attrs={'placeholder':'Usuario', 'id': 'Usuario'}))
    clave = forms.CharField(min_length=5, widget=forms.PasswordInput(attrs={'placeholder':'Contraseña', 'id': 'Clave'}))

    def clean_usuario(self):
        #Comprueba que exista un username en la base de datos
        usuario = self.cleaned_data['usuario']
        if not User.objects.filter(username=usuario):
            raise forms.ValidationError('El nombre de usuario no existe!')
        return usuario
