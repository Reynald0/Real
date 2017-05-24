# -*- encoding: utf-8 -*-
from datetime import date
from django import forms
from django.contrib.auth.models import User
from .models import Alumno, Carrera

class RegistroAlumno(forms.Form):
    usuario     = forms.CharField(min_length=5,widget=forms.TextInput(attrs={'id': 'Usuario'}))
    clave       = forms.CharField(min_length=5, widget=forms.PasswordInput(attrs={'id': 'Clave'}))
    email       = forms.EmailField(widget=forms.EmailInput(attrs={'id': 'Email', 'type': 'email', 'class':'validate'}))
    no_control  = forms.IntegerField(widget=forms.NumberInput(attrs={'id': 'No control', 'length' : '8', 'class':'validate'}))
    nombre      = forms.CharField(widget=forms.TextInput(attrs={'id': 'Nombre'}))
    apellido_paterno = forms.CharField(widget=forms.TextInput(attrs={'id': 'Apellido'}))
    apellido_materno = forms.CharField(widget=forms.TextInput(attrs={'id': 'Apellido'}))
    fecha_nac   = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'datepicker'}))
    carrera     = forms.ModelChoiceField(queryset=Carrera.objects.all(), initial=1)
    promedio    = forms.FloatField(widget=forms.NumberInput(attrs={'id': 'Promedio'}))
    semestre    = forms.IntegerField(widget=forms.NumberInput(attrs={'id': 'Semestre'}))

    def clean_usuario(self):
        try:
            usuario = str(self.cleaned_data['usuario'])
        except Exception:
            # Deja que se registren con caractereres especiales
            raise forms.ValidationError('Solo se permite caracteres alfanuméricos. Letras, dígitos y @/./+/-/_ únicamente.')
            return  usuario
        # Comprueba que no exista un usuario igual en la base de datos
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
        promedio = float(self.cleaned_data['promedio'])
        if promedio > 100.0:
            raise forms.ValidationError('Promedio en escala de 1 a 100')
        return promedio

    def clean_fecha_nac(self):
        #Comprueba que el promedio no sea mayor a 100
        fecha_nac = self.cleaned_data['fecha_nac']
        anio_nacimiento = int(fecha_nac.year)
        if (int(date.today().year) - anio_nacimiento) < 17:
            raise forms.ValidationError(u'No se pueden registrar menores de 17 años')
        return fecha_nac

class LogAlumno(forms.Form):
    usuario = forms.CharField(min_length=5,widget=forms.TextInput(attrs={'id': 'Usuario'}))
    clave = forms.CharField(min_length=5, widget=forms.PasswordInput(attrs={'id': 'Clave'}))

    def clean_usuario(self):
        #Comprueba que exista un username en la base de datos
        usuario = self.cleaned_data['usuario']
        if not User.objects.filter(username=usuario.title()):
            raise forms.ValidationError('El nombre de usuario no existe!')
        return usuario

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ('carrera', 'semestre', 'promedio')

class CambiarPassForm(forms.Form):
    clave_actual = forms.CharField(min_length=5,widget=forms.PasswordInput(attrs={'id': 'clave_actual'}))
    clave_nueva = forms.CharField(min_length=5, widget=forms.PasswordInput(attrs={'id': 'clave_nueva'}))
    confirmar_clave_nueva = forms.CharField(min_length=5, widget=forms.PasswordInput(attrs={'id': 'confirmar_clave_nueva'}))