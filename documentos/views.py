from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.shortcuts import render, get_object_or_404, redirect
from documentos.forms import ComprobanteDomicilioForm, CredencialEstudianteForm, KardexForm
from documentos.models import ComprobanteDomicilio, CredencialEstudiante, Kardex
from cuentas.views import Alumno



@login_required(login_url='login_alumno')
def comprobante_domicilio(request):
    usuario_alumno = get_object_or_404(Alumno, user= request.user)
    if request.method == 'POST':  # Si el formulario envia algo con el metodo POST
        form = ComprobanteDomicilioForm(request.POST, request.FILES)  # Se crea el objeto form, a este objeto se le asigna el modelo LogAlumno
        if form.is_valid():  # Si el formulario es valido
            cleaned_data = form.cleaned_data
            usuario = request.user
            url_del_documento = cleaned_data.get('url_documento')  # Se obtiene el valor del campo usuario
            # Verifica que se pueda registrar el archivo
            try:
                archivo = ComprobanteDomicilio.objects.get(alumno=usuario_alumno)
                archivo.url_documento = url_del_documento
                archivo.save()
            except Exception  as e:  # Si el usuario ya existe manda un mensaje
                archivo = ComprobanteDomicilio.objects.create(alumno=usuario_alumno, url_documento=url_del_documento)
                archivo.save()
                return render(request, 'documentos/comprobante_domicilio.html', {'form': form})
            return redirect('perfil_alumno')
        else:  # De lo contrario, el formulario no es valido
            # Regresa el html 'login' renderizado con la variable form, que es el formulario previamente rellenado
            return render(request, 'documentos/comprobante_domicilio.html', {'form': form})
    else: # De lo contrario, la persona esta apenas por registrarse
        # Se crea el bojeto form con el formulario LogAlumno
        form = ComprobanteDomicilioForm()
        # Regresa el html 'comprobante_domicilio' renderizado con la variable form en blanco.
        return render(request, 'documentos/comprobante_domicilio.html', {'form': form})

@login_required(login_url='login_alumno')
def credencial_estudiante(request):
    usuario_alumno = get_object_or_404(Alumno, user= request.user)
    if request.method == 'POST':  # Si el formulario envia algo con el metodo POST
        form = CredencialEstudianteForm(request.POST, request.FILES)  # Se crea el objeto form, a este objeto se le asigna el modelo LogAlumno
        if form.is_valid():  # Si el formulario es valido
            cleaned_data = form.cleaned_data
            usuario = request.user
            url_del_documento = cleaned_data.get('url_documento')  # Se obtiene el valor del campo usuario
            # Verifica que se pueda registrar el archivo
            try:
                archivo = CredencialEstudiante.objects.get(alumno=usuario_alumno)
                archivo.url_documento = url_del_documento
                archivo.save()
            except Exception  as e:  # Si el usuario ya existe manda un mensaje
                archivo = CredencialEstudiante.objects.create(alumno=usuario_alumno, url_documento=url_del_documento)
                archivo.save()
                return render(request, 'documentos/credencial_estudiante.html', {'form': form})
            return redirect('perfil_alumno')
        else:  # De lo contrario, el formulario no es valido
            # Regresa el html 'login' renderizado con la variable form, que es el formulario previamente rellenado
            return render(request, 'documentos/credencial_estudiante.html', {'form': form})
    else: # De lo contrario, la persona esta apenas por registrarse
        # Se crea el bojeto form con el formulario LogAlumno
        form = CredencialEstudianteForm()
        # Regresa el html 'comprobante_domicilio' renderizado con la variable form en blanco.
        return render(request, 'documentos/credencial_estudiante.html', {'form': form})


@login_required(login_url='login_alumno')
def kardex(request):
    usuario_alumno = get_object_or_404(Alumno, user= request.user)
    if request.method == 'POST':  # Si el formulario envia algo con el metodo POST
        form = KardexForm(request.POST, request.FILES)  # Se crea el objeto form, a este objeto se le asigna el modelo LogAlumno
        if form.is_valid():  # Si el formulario es valido
            cleaned_data = form.cleaned_data
            usuario = request.user
            url_del_documento = cleaned_data.get('url_documento')  # Se obtiene el valor del campo usuario
            # Verifica que se pueda registrar el archivo
            try:
                archivo = Kardex.objects.get(alumno=usuario_alumno)
                archivo.url_documento = url_del_documento
                archivo.save()
            except Exception  as e:  # Si el usuario ya existe manda un mensaje
                archivo = Kardex.objects.create(alumno=usuario_alumno, url_documento=url_del_documento)
                archivo.save()
                return render(request, 'documentos/credencial_estudiante.html', {'form': form})
            return redirect('perfil_alumno')
        else:  # De lo contrario, el formulario no es valido
            # Regresa el html 'login' renderizado con la variable form, que es el formulario previamente rellenado
            return render(request, 'documentos/credencial_estudiante.html', {'form': form})
    else: # De lo contrario, la persona esta apenas por registrarse
        # Se crea el bojeto form con el formulario LogAlumno
        form = KardexForm()
        # Regresa el html 'comprobante_domicilio' renderizado con la variable form en blanco.
        return render(request, 'documentos/credencial_estudiante.html', {'form': form})