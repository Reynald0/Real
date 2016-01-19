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
    usuario     = forms.CharField(min_length=5,widget=forms.TextInput(attrs={'id': 'Usuario'}))
    clave       = forms.CharField(min_length=5, widget=forms.PasswordInput(attrs={'id': 'Clave'}))
    email       = forms.EmailField(widget=forms.EmailInput(attrs={'id': 'Email', 'type': 'email', 'class':'validate'}))
    no_control  = forms.IntegerField(widget=forms.NumberInput(attrs={'id': 'No control', 'length' : '8', 'class':'validate'}))
    nombre      = forms.CharField(widget=forms.TextInput(attrs={'id': 'Nombre'}))
    apellido    = forms.CharField(widget=forms.TextInput(attrs={'id': 'Apellido'}))
    edad        = forms.IntegerField(widget=forms.NumberInput(attrs={'id': 'Edad'}))
    carrera     = forms.ChoiceField(choices=OPCIONES, widget=forms.Select(attrs={'id': 'Carrera'}))
    promedio    = forms.FloatField(widget=forms.NumberInput(attrs={'id': 'Promedio'}))
    semestre    = forms.IntegerField(widget=forms.NumberInput(attrs={'id': 'Semestre'}))

    def clean_usuario(self):
        #Comprueba que no exista un usuario igual en la base de datos
        usuario = str(self.cleaned_data['usuario'])
        if User.objects.filter(first_name=usuario):
            raise forms.ValidationError('El usuario ya existe!')
        return usuario

    def clean_no_control(self):
        #Comprueba que no exista un numero de control igual en la base de datos
        #Comprueba que el numero de control sea exactamente de 8 digitos
        no_control = str(self.cleaned_data['no_control'])
        if Alumno.objects.filter(no_control=no_control):
            raise forms.ValidationError('El número de control ya existe!')
        elif len(no_control) > 8:
            raise forms.ValidationError('Solo se permiten 8 dígitos en el número de control')
        return no_control

    def clean_email(self):
        #Comprueba que no exista un email igual en la base de datos
        email = self.cleaned_data['email']
        if User.objects.filter(email=email):
            raise forms.ValidationError('El correo ya fue registrado!')
        return email

    def clean_promedio(self):
        #Comprueba que el promedio no sea mayor a 100
        promedio = int(self.cleaned_data['promedio'])
        if promedio > 100:
            raise forms.ValidationError('Promedio en escala de 1 a 100')
        return promedio

class LogAlumno(forms.Form):
    usuario = forms.CharField(min_length=5,widget=forms.TextInput(attrs={'placeholder':'Usuario', 'id': 'Usuario'}))
    clave = forms.CharField(min_length=5, widget=forms.PasswordInput(attrs={'placeholder':'Contraseña', 'id': 'Clave'}))

    def clean_usuario(self):
        #Comprueba que exista un username en la base de datos
        usuario = self.cleaned_data['usuario']
        if not User.objects.filter(username=usuario.title()):
            raise forms.ValidationError('El nombre de usuario no existe!')
        return usuario
