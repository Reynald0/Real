# -*- encoding: utf-8 -*-
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.utils import timezone
from .forms import RegistroAlumno, LogAlumno
from .models import Alumno, Noticia

def inicio(request):
    return render(request, 'cuentas/inicio.html')

def registro_alumno(request):
    show_msg = False
    mensaje = 'Registrado exitosamente.'
    error = False
    if request.method == 'POST':
        form = RegistroAlumno(request.POST, request.FILES)
        #Comprobamos si el formulario es valido
        if form.is_valid():
            show_msg = True
            # En caso de ser valido, obtenemos los datos del formulario.
            # form.cleaned_data obtiene los datos limpios y los pone en un
            # diccionario con pares clave/valor, donde clave es el nombre del campo
            # del formulario y el valor es el valor si existe.
            cleaned_data = form.cleaned_data
            usuario     = cleaned_data.get('usuario')
            clave       = cleaned_data.get('clave')
            email       = cleaned_data.get('email')
            no_control  = cleaned_data.get('no_control')
            nombre      = cleaned_data.get('nombre')
            apellido    = cleaned_data.get('apellido')
            edad        = cleaned_data.get('edad')
            carrera     = cleaned_data.get('carrera')
            promedio    = cleaned_data.get('promedio')
            semestre    = cleaned_data.get('semestre')
            ######
            try:
                modelo_alumno = User.objects.create_user(username=usuario.title(), password=clave, first_name= nombre.title(), last_name=apellido.title())
            except IntegrityError as e:
                mensaje = 'Ya existe ese usuario.'
                error = True
                return render(request,'cuentas/registro.html', {'error':error, 'mensaje': mensaje, 'show_msg': show_msg})
            modelo_alumno.email = email
            ######
            alumno = Alumno()
            alumno.no_control = no_control
            alumno.nombre = nombre.title()
            alumno.apellido = apellido.title()
            alumno.edad = edad
            alumno.carrera = carrera
            alumno.promedio = promedio
            alumno.semestre = semestre
            # Por ultimo, guardamos el objeto Alumno
            alumno.user = modelo_alumno
            alumno.save()
            modelo_alumno.save()
            log_alumno = authenticate(username=usuario.title(), password=clave)
            login(request, log_alumno)
            # Ahora, redireccionamos a la pagina cuentas/registro.html
            # Pero lo hacemos con un redirect.
            return render(request,'cuentas/registro.html', {'error':error, 'mensaje': mensaje, 'show_msg': show_msg})
    else:
        form = RegistroAlumno()
    return render(request, 'cuentas/registro.html', {'form': form})

def informacion(request):
    return render(request, 'cuentas/informacion.html')

def noticias(request):
    if not request.user.is_authenticated():
        return login_alumno(request)
    noticias = Noticia.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('-fecha_publicacion')
    return render(request, 'cuentas/noticias.html', {'noticias': noticias})

def contacto(request):
    return render(request, 'cuentas/contacto.html')

def lista_alumnos(request):
    if not request.user.is_authenticated():
        return login_alumno(request)
    alumnos = Alumno.objects.order_by('nombre')
    return render(request, 'cuentas/lista_alumnos.html', {'alumnos' : alumnos , 'total_alumnos': len(alumnos)})

def login_alumno(request):
    error = False
    if request.method == 'POST':
        form = LogAlumno(request.POST)
        if form.is_valid():
            usuario = request.POST.get('usuario')
            clave = request.POST.get('clave')
            alumno = authenticate(username=usuario.title(), password=clave)
            if alumno is not None:
                if alumno.is_active:
                    login(request, alumno)
                    return redirect('inicio')
            else:
                error = True
                return render(request, 'cuentas/login.html', {'form' : form, 'error': error})
        else:
            error = False
            return render(request, 'cuentas/login.html', {'form' : form, 'error': error})
    else:
        form = LogAlumno()
        return render(request, 'cuentas/login.html', {'form' : form})

def logout_alumno(request):
    logout(request)
    return inicio(request)

def perfil_alumno(request):
    if not request.user.is_authenticated():
        return login_alumno(request)
    try: #Evalua si el usuario tiene un alumno registrado, por ejemplo: Una cuenta ADMIN no posee un alumno registrado
        alumno_user = Alumno.objects.get(user_id=request.user.pk)
    except ObjectDoesNotExist :
        return render(request, 'cuentas/perfil.html') #No manda objeto alumno_user ya que no existe
    return render(request, 'cuentas/perfil.html', {'alumno' : alumno_user })
