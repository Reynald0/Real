# -*- encoding: utf-8 -*-
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import RegistroAlumno, LogAlumno
from .models import Alumno

def inicio(request): #Se define la funcion inicio el cual es el nombre de la vista a mostrar
    # Regresa el html 'inicio' unicado en la carpeta templates/cuentas de la aplicacion cuentas,
    # es decir, la ruta es /app_name/templates/app_name(good practice)/X.html
    # en este caso cuentas/templates/cuentas(buena practica ponerlo asi)/inicio.html
    return render(request, 'cuentas/inicio.html')

def registro_alumno(request): #Se define la funcion registro_alumno el cual es el nombre de la vista a mostrar
    show_msg = False
    mensaje = 'Registrado exitosamente.'
    error = False
    if request.method == 'POST': #Si el formulario envia algo con el metodo POST
        form = RegistroAlumno(request.POST) #Se crea el objeto form, a este objeto se le asigna el modelo RegistroAlumno
        if form.is_valid(): #Si el formulario es valido
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
            # Verifica que se pueda crear el usuario
            try:
                usuario_alumno = User.objects.create_user(username=usuario.title(), password=clave)
                # A continuacion se una el metodo title()  en 'nombre' y 'apellido' para poner cualquier cadena de esta forma 'Esto Es Un Titulo'
                # Es decir, todas las primeras letras de cada palabra en mayuscula
                # Como ya se obtiene la variable nombre, se le asigna al atributo email del objeto usuario_alumno
                usuario_alumno.first_name = nombre.title()
                # Como ya se obtiene la variable apellido, se le asigna al atributo email del objeto usuario_alumno
                usuario_alumno.last_name = apellido.title()
                # Como ya se obtiene la variable email, se le asigna al atributo email del objeto usuario_alumno
                usuario_alumno.email = email
            except IntegrityError as e: #Si el usuario ya existe manda un mensaje
                mensaje = 'Ya existe ese usuario.'
                error = True
                # regresa el html registro con las variables error, mensaje y show_msg previamente declarados y asignados
                return render(request,'cuentas/registro.html', {'error':error, 'mensaje': mensaje, 'show_msg': show_msg})
            # Una vez creado el usuario se pasa a crear el Alumno que mediante una llave foranea hace referencia al Usuario creado
            # Es decir, un Alumno debe tener su Usuario para poder iniciar sesion, aqui se aprovecha la tabla User de Django
            alumno = Alumno() #Se crea el objeto alumno usando el modelo Alumno
            #Se asigna al objeto/modelo alumno el no_control obtenido por el metodo post anteriormente
            # por medio del metodo POST (ver lineas de la 26 a la 35)
            alumno.no_control = no_control
            #Se asigna al objeto/modelo alumno el nombre obtenido por el metodo post anteriormente
            # por medio del metodo POST (ver lineas de la 26 a la 35), ademas se usa el metodo title() para darle un formato
            # a pesar de que sea mayusculas o minusculas
            alumno.nombre = nombre.title()
            #Se asigna al objeto/modelo alumno el apellido obtenido por el metodo post anteriormente
            # por medio del metodo POST (ver lineas de la 26 a la 35), ademas se usa el metodo title() para darle un formato
            # a pesar de que sea mayusculas o minusculas
            alumno.apellido = apellido.title()
            #Se asigna al objeto/modelo alumno la edad obtenida por el metodo post anteriormente
            # por medio del metodo POST (ver lineas de la 26 a la 35)
            alumno.edad = edad
            #Se asigna al objeto/modelo alumno la carrera obtenida por el metodo post anteriormente
            # por medio del metodo POST (ver lineas de la 26 a la 35)
            alumno.carrera = carrera
            #Se asigna al objeto/modelo alumno el promedio obtenido por el metodo post anteriormente
            # por medio del metodo POST (ver lineas de la 26 a la 35)
            alumno.promedio = promedio
            #Se asigna al objeto/modelo alumno el semestre obtenido por el metodo post anteriormente
            # por medio del metodo POST (ver lineas de la 26 a la 35)
            alumno.semestre = semestre
            # Por ultimo, guardamos el objeto Alumno
            #Se asigna al objeto/modelo alumno el usuario_alumno, es decir, el objeto usuario_alumno ya ha sido creado arriba
            # por tanto al ser una llave foranea (del objeto alumno) hara referencia a la llave primaria del objeto usuario_alumno
            # Si se llega a borrar un usuario_alumno tambien se borara el objeto alumno
            alumno.user = usuario_alumno
            # Se guarda el objeto usuario_alumno
            usuario_alumno.save()
            # Se guarda el objeto alumno
            alumno.save()
            # Una vez creado se da por hecho que todo esta correcto y se manda a autenticar (login)
            # se crea un objeto log_alumno al cual se le asigna el usuario y contrasena obtenidos por el formulario (metodo post)
            # Como todo esta correcto no se hace una validacion (try - except )
            log_alumno = authenticate(username=usuario.title(), password=clave)
            # Se usa el metodo login() que recibe como argumentos el request y el objeto a logear (log_alumno)
            login(request, log_alumno)
            # Ahora, se regresa a al html 'registro' y con las variables error, mensaje y show_msg para ser manipulados
            # por la plantilla
            return render(request,'cuentas/registro.html', {'error':error, 'mensaje': mensaje, 'show_msg': show_msg})
    else: # sino, entonces la persona entra a la pagina 'registro' para registrarse
        form = RegistroAlumno() #Crea el objeto form, al objeto form se le asigna el formulario RegistroAlumno
    #Se regresa el html 'registro' renderizado con el formulario a mostrar, en este caso 'form'
    # Darse cuenta que la variable enviada a la platilla es la llave del diccionario
    return render(request, 'cuentas/registro.html', {'form': form})

def informacion(request): #Se define la funcion informacion el cual es el nombre de la vista a mostrar
    # Regresa el html 'informacion' renderizado para ser visto sin variables o en otras palabras, CONTEXTO
    return render(request, 'cuentas/informacion.html')

def contacto(request): #Se define la funcion contacto el cual es el nombre de la vista a mostrar
    # Regresa el html 'contacto' renderizado para ser visto sin variables o en otras palabras, CONTEXTO
    return render(request, 'cuentas/contacto.html')

def lista_alumnos(request): #Se define la funcion lista_alumnos el cual es el nombre de la vista a mostrar
    if not request.user.is_authenticated(): #Si el usuario no ha iniciado sesion (logeado)
        # Regresa la vista login_alumno, la vista login_alumno se encarga de mostrar el formulario
        # para poder logearse
        return login_alumno(request)
    alumnos = Alumno.objects.order_by('nombre')
    # Regresa el html 'lista_alumnos' renderizado para ser visto y con las variables: alumnos, total_alumnos
    return render(request, 'cuentas/lista_alumnos.html', {'alumnos' : alumnos , 'total_alumnos': len(alumnos)})

def login_alumno(request): #Se define la funcion login_alumno el cual es el nombre de la vista a mostrar
    error = False
    if request.method == 'POST': #Si el formulario envia algo con el metodo POST
        form = LogAlumno(request.POST) #Se crea el objeto form, a este objeto se le asigna el modelo LogAlumno
        if form.is_valid(): #Si el formulario es valido
            usuario = request.POST.get('usuario') #Se obtiene el valor del campo usuario
            clave = request.POST.get('clave') #Se obtiene el valor del campo clave
            # Se crea un objeto alumno el cual es la autenticacion con las variables usuario y clave
            usuario_alumno = authenticate(username=usuario.title(), password=clave)
            # Si existe algun  usuario_alumno, es decir, ha sido registrado el usuario que se trata de logear
            if usuario_alumno is not None:
                # Si el alumno esta activo en el sistema (osea no esta dado de baja)
                # No estoy seguro de esto!
                if usuario_alumno.is_active:
                    login(request, usuario_alumno) # Se usa el metodo log() que recibe como argumento a request y al objeto alumno
                    # Se redirige al la vista llamada inicio.
                    # Para saber como se llama cada vista hay que ver el valor de la variable 'name' en el urls.py
                    # En este caso la url llamada inicio es el inicio del sitio web
                    return redirect('inicio')
            else: # De lo contrario, el usuario no ha sido registrado
                error = True
                # Regresa el html 'login' renderizado y con el formulario rellenado a como lo dejo la persona
                # tambien la variable error (Booleano)
                return render(request, 'cuentas/login.html', {'form' : form, 'error': error})
        else: # De lo contrario, el formulario no es valido
            # Regresa el html 'login' renderizado con la variable form, que es el formulario previamente rellenado
            return render(request, 'cuentas/login.html', {'form' : form})
    else: #De lo contrario, la persona esta apenas por registrarse
        #Se crea el bojeto form con el formulario LogAlumno
        form = LogAlumno()
        #Regresa el html 'login' renderizado con la variable form en blanco.
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
