# -*- encoding: utf-8 -*-
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import EmailMessage
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.template import Context
from django.template.loader import get_template
from documentos.models import ComprobanteDomicilio, CredencialEstudiante, Kardex
from .forms import RegistroAlumno, LogAlumno, AlumnoForm, CambiarPassForm
from .models import Alumno, Carrera, Estado_Solicitud
from datetime import date



def enviar_datos_al_correo(correo_electronico, nombre_usuario, password):
    subject = "Registro REAL"
    to = [correo_electronico]
    from_email = 'reynaldobernard15@gmail.com'

    contexto = {
        'user': nombre_usuario,
        'pass': password
    }

    message = get_template('email/email_plantilla.html').render(Context(contexto))
    msg = EmailMessage(subject, message, to=to, from_email=from_email)
    msg.content_subtype = 'html'
    msg.send()

def calcular_edad(fecha_nac):
    diferencia_fechas = date.today() - fecha_nac
    diferencia_fechas_dias = diferencia_fechas.days
    edad_numerica = diferencia_fechas_dias / 365.2425 # 365.2425 ---> Valor gregoriano de un año
    edad = int(edad_numerica)
    return edad



def inicio(request): #Se define la funcion inicio el cual es el nombre de la vista a mostrar
    # Regresa el html 'inicio' unicado en la carpeta templates/cuentas de la aplicacion cuentas,
    # es decir, la ruta es /app_name/templates/app_name(good practice)/X.html
    # en este caso cuentas/templates/cuentas(buena practica ponerlo asi)/inicio.html
    return render(request, 'cuentas/inicio.html')

def registro_alumno(request): #Se define la funcion registro_alumno el cual es el nombre de la vista a mostrar
    mensaje = 'Registrado exitosamente, se ha enviado un correo con sus datos!'
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
            apellido_paterno = cleaned_data.get('apellido_paterno')
            apellido_materno = cleaned_data.get('apellido_materno')
            fecha_nac   = cleaned_data.get('fecha_nac')
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
                usuario_alumno.last_name = u"{0} {1}".format(apellido_materno.title(),apellido_paterno.title())
                # Como ya se obtiene la variable email, se le asigna al atributo email del objeto usuario_alumno
                usuario_alumno.email = email
            except IntegrityError: #Si el usuario ya existe manda un mensaje
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
            alumno.apellido_paterno = apellido_paterno.title()
            alumno.apellido_materno = apellido_materno.title()
            #Se asigna al objeto/modelo alumno la fecha_nac obtenida por el metodo post anteriormente
            # por medio del metodo POST (ver lineas de la 26 a la 35)
            alumno.fecha_nac = fecha_nac
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
            #Enviar correo con nombre de usuario y contraseña
            #enviar_datos_al_correo(email, usuario, clave)
            # Una vez creado se da por hecho que  esta correcto y se manda a autenticar (login)
            # se crea un objeto log_alumno al cual se le asigna el usuario y contrasena obtenidos por el formulario (metodo post)
            # Como esta correcto no se hace una validacion (try - except )
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

@login_required(login_url='login_alumno')
def lista_alumnos(request): #Se define la funcion lista_alumnos el cual es el nombre de la vista a mostrar
    if request.user.is_superuser: #Si el usuario es super usuario
        alumnos = Alumno.objects.order_by('no_control')
        total_alumnos = len(Alumno.objects.all())
        alumnos_en_proceso = Alumno.objects.order_by('no_control').filter(estado_solicitud__id=1)
        alumnos_en_espera = Alumno.objects.order_by('no_control').filter(estado_solicitud__id=2)
        alumnos_aprobados = Alumno.objects.order_by('no_control').filter(estado_solicitud__id=3)
        alumnos_no_aprobados = Alumno.objects.order_by('no_control').filter(estado_solicitud__id=4)
        diccionario_documentos = {}
        for alumno in alumnos_en_espera:
            documento_comprobante_domicilio = ComprobanteDomicilio.objects.get(alumno=alumno)
            documento_credencial_estudiante = CredencialEstudiante.objects.get(alumno=alumno)
            documento_kardex = Kardex.objects.get(alumno=alumno)
            diccionario_documentos[alumno.no_control] = [str(documento_comprobante_domicilio.url_documento),
                                              str(documento_credencial_estudiante.url_documento),
                                              str(documento_kardex.url_documento)]

        # Regresa el html 'lista_alumnos' renderizado para ser visto y con las variables: alumnos, total_alumnos
        return render(request, 'cuentas/lista_alumnos/todos.html', {'alumnos': alumnos, 'total_alumnos': total_alumnos,
                               'alumnos_en_espera' : len(alumnos_en_espera), 'diccionario_documentos': diccionario_documentos,
                               'alumnos_en_proceso': len(alumnos_en_proceso), 'alumnos_aprobados': len(alumnos_aprobados),
                               'alumnos_no_aprobados': len(alumnos_no_aprobados)})
    else:
        return redirect('perfil_alumno')

@login_required(login_url='login_alumno')
def lista_alumnos_en_proceso(request):
    alumnos = Alumno.objects.all().filter(estado_solicitud__id=1).order_by('no_control')
    if request.user.is_superuser:  # Si el usuario es super usuario
        total_alumnos = len(Alumno.objects.all())
        alumnos_en_proceso = Alumno.objects.order_by('no_control').filter(estado_solicitud__id=1)
        alumnos_en_espera = Alumno.objects.order_by('no_control').filter(estado_solicitud__id=2)
        alumnos_aprobados = Alumno.objects.order_by('no_control').filter(estado_solicitud__id=3)
        alumnos_no_aprobados = Alumno.objects.order_by('no_control').filter(estado_solicitud__id=4)
        # Regresa el html 'lista_alumnos' renderizado para ser visto y con las variables: alumnos, total_alumnos
        return render(request, 'cuentas/lista_alumnos/en_proceso.html',
                      {'alumnos': alumnos, 'total_alumnos': total_alumnos,
                       'alumnos_en_espera': len(alumnos_en_espera),
                       'alumnos_en_proceso': len(alumnos_en_proceso),
                       'alumnos_aprobados': len(alumnos_aprobados),
                       'alumnos_no_aprobados': len(alumnos_no_aprobados)})

@login_required(login_url='login_alumno')
def lista_alumnos_en_evaluacion(request):
    if request.user.is_superuser:  # Si el usuario es super usuario
        alumnos = Alumno.objects.all().filter(estado_solicitud__id=2).order_by('no_control')
        total_alumnos = len(Alumno.objects.all())
        alumnos_en_proceso = Alumno.objects.order_by('no_control').filter(estado_solicitud__id=1)
        alumnos_en_espera = Alumno.objects.order_by('no_control').filter(estado_solicitud__id=2)
        alumnos_aprobados = Alumno.objects.order_by('no_control').filter(estado_solicitud__id=3)
        alumnos_no_aprobados = Alumno.objects.order_by('no_control').filter(estado_solicitud__id=4)
        diccionario_documentos = {}
        for alumno in alumnos_en_espera:
            documento_comprobante_domicilio = ComprobanteDomicilio.objects.get(alumno=alumno)
            documento_credencial_estudiante = CredencialEstudiante.objects.get(alumno=alumno)
            documento_kardex = Kardex.objects.get(alumno=alumno)
            diccionario_documentos[alumno.no_control] = [str(documento_comprobante_domicilio.url_documento),
                                                         str(documento_credencial_estudiante.url_documento),
                                                         str(documento_kardex.url_documento)]

        # Regresa el html 'lista_alumnos' renderizado para ser visto y con las variables: alumnos, total_alumnos
        return render(request, 'cuentas/lista_alumnos/todos.html',
                      {'alumnos': alumnos, 'total_alumnos': total_alumnos,
                       'alumnos_en_espera': len(alumnos_en_espera),
                       'diccionario_documentos': diccionario_documentos,
                       'alumnos_en_proceso': len(alumnos_en_proceso),
                       'alumnos_aprobados': len(alumnos_aprobados),
                       'alumnos_no_aprobados': len(alumnos_no_aprobados)})

@login_required(login_url='login_alumno')
def lista_alumnos_aprobados(request):
    if request.user.is_superuser:  # Si el usuario es super usuario
        alumnos = Alumno.objects.all().filter(estado_solicitud__id=3).order_by('no_control')
        if request.user.is_superuser:  # Si el usuario es super usuario
            total_alumnos = len(Alumno.objects.all())
            alumnos_en_proceso = Alumno.objects.order_by('no_control').filter(estado_solicitud__id=1)
            alumnos_en_espera = Alumno.objects.order_by('no_control').filter(estado_solicitud__id=2)
            alumnos_aprobados = Alumno.objects.order_by('no_control').filter(estado_solicitud__id=3)
            alumnos_no_aprobados = Alumno.objects.order_by('no_control').filter(estado_solicitud__id=4)
            # Regresa el html 'lista_alumnos' renderizado para ser visto y con las variables: alumnos, total_alumnos
            return render(request, 'cuentas/lista_alumnos/aprobados.html',
                          {'alumnos': alumnos, 'total_alumnos': total_alumnos,
                           'alumnos_en_espera': len(alumnos_en_espera),
                           'alumnos_en_proceso': len(alumnos_en_proceso),
                           'alumnos_aprobados': len(alumnos_aprobados),
                           'alumnos_no_aprobados': len(alumnos_no_aprobados)})

@login_required(login_url='login_alumno')
def lista_alumnos_no_aprobados(request):
    if request.user.is_superuser:  # Si el usuario es super usuario
        alumnos = Alumno.objects.all().filter(estado_solicitud__id=3).order_by('no_control')
        if request.user.is_superuser:  # Si el usuario es super usuario
            total_alumnos = len(Alumno.objects.all())
            alumnos_en_proceso = Alumno.objects.order_by('no_control').filter(estado_solicitud__id=1)
            alumnos_en_espera = Alumno.objects.order_by('no_control').filter(estado_solicitud__id=2)
            alumnos_aprobados = Alumno.objects.order_by('no_control').filter(estado_solicitud__id=3)
            alumnos_no_aprobados = Alumno.objects.order_by('no_control').filter(estado_solicitud__id=4)
            # Regresa el html 'lista_alumnos' renderizado para ser visto y con las variables: alumnos, total_alumnos
            return render(request, 'cuentas/lista_alumnos/no_aprobados.html',
                          {'alumnos': alumnos, 'total_alumnos': total_alumnos,
                           'alumnos_en_espera': len(alumnos_en_espera),
                           'alumnos_en_proceso': len(alumnos_en_proceso),
                           'alumnos_aprobados': len(alumnos_aprobados),
                           'alumnos_no_aprobados': len(alumnos_no_aprobados)})

def login_alumno(request): #Se define la funcion login_alumno el cual es el nombre de la vista a mostrar
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

@login_required(login_url='login_alumno')
def logout_alumno(request): #Se define la funcion logout_alumno el cual es el nombre de la vista a mostrar
    logout(request) #Se usa el metodo logout() que recibe el request
    # Regresa la vista inicio y como inicio necesita request, entonces se le pasa el request de log_alumno
    return redirect('inicio')

@login_required(login_url='login_alumno')
def perfil_alumno(request, documento_subido=False, falta_documento=False): #Se define la funcion perfil_alumno el cual es el nombre de la vista a mostrar
    try:
        usuario_alumno = Alumno.objects.get(user_id=request.user.id)
    except ObjectDoesNotExist:
        usuario_alumno = None
    try:
        comprobante_de_domicilio = ComprobanteDomicilio.objects.get(alumno=usuario_alumno)
    except ObjectDoesNotExist:
        comprobante_de_domicilio = None
    try:
        credencial_de_estudiante = CredencialEstudiante.objects.get(alumno=usuario_alumno)
    except ObjectDoesNotExist:
        credencial_de_estudiante = None
    try:
        kardex = Kardex.objects.get(alumno=usuario_alumno)
    except ObjectDoesNotExist:
        kardex = None

    if not request.user.is_authenticated(): #Si el usuario no esta logeado
        return login_alumno(request) #Regresa la vista de login_alumno
    try: #Evalua si el usuario tiene un alumno registrado, por ejemplo: Una cuenta ADMIN no posee un alumno registrado
        alumno_user = Alumno.objects.get(user_id=request.user.pk)
        edad = calcular_edad(alumno_user.fecha_nac)
    except ObjectDoesNotExist:
        return render(request, 'cuentas/perfil.html') #No manda objeto alumno_user ya que no existe
    return render(request, 'cuentas/perfil.html',
                  {'alumno' : alumno_user , 'edad': edad,'comprobante_de_domicilio' : comprobante_de_domicilio,
                   'credencial_de_estudiante' : credencial_de_estudiante, 'kardex' : kardex, 'documento_subido' : documento_subido,
                   'falta_documento' : falta_documento})

@login_required(login_url='login_alumno')
def editar_perfil_alumno(request):
    usuario = request.user
    alumno = get_object_or_404(Alumno, user=usuario)
    if request.method == 'POST':
        form = AlumnoForm(request.POST, instance=alumno)
        if form.is_valid():
            modulo = form.save(commit=False)
            modulo.save()
            return redirect('perfil_alumno')
    else:
        form = AlumnoForm(instance=alumno)
        return render(request, 'cuentas/editar_perfil.html', {'form': form})

@login_required(login_url='login_alumno')
def cambiar_pass(request):
    usuario = get_object_or_404(User, id=request.user.id)
    alumno = get_object_or_404(Alumno, user=usuario)
    edad = calcular_edad(alumno.fecha_nac)
    if request.method == 'POST':
        form = CambiarPassForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            clave_actual = cleaned_data.get('clave_actual')
            clave_nueva = cleaned_data.get('clave_nueva')
            confirmar_clave_nueva = cleaned_data.get('confirmar_clave_nueva')
            if usuario.check_password(clave_actual):
                if clave_nueva != confirmar_clave_nueva: #Si las clave (ingresada dos veces no es IGUAL)
                    clave_incorrecta = True
                    mensaje = "La clave nueva y su confirmación no son iguales"
                    return render(request, 'cuentas/cambiar_pass.html',
                                  {'form': form, 'clave_incorrecta': clave_incorrecta, 'mensaje': mensaje})
                usuario.set_password(clave_nueva)
                usuario.save()
                log_alumno = authenticate(username=usuario.username, password=clave_nueva)
                login(request, log_alumno)
                clave_cambiada = True
                return render(request, 'cuentas/perfil.html', {'alumno': alumno, 'edad': edad, 'clave_cambiada': clave_cambiada})
            else:
                clave_incorrecta = True
                mensaje = "Contraseña incorrecta"
                return render(request, 'cuentas/cambiar_pass.html',
                              {'form' : form, 'clave_incorrecta': clave_incorrecta, 'mensaje' : mensaje})
    else:
        form = CambiarPassForm()
        return render(request, 'cuentas/cambiar_pass.html', {'form': form})

@login_required(login_url='login_alumno')
def solicitar_beca(request):
    usuario = get_object_or_404(User, id=request.user.id)
    alumno = get_object_or_404(Alumno, user=usuario)
    # Verificar si tiene los documentos subidos para solicitar la beca
    try:
        documento_comprobante_domicilio = ComprobanteDomicilio.objects.get(alumno=alumno)
    except ObjectDoesNotExist:
        documento_comprobante_domicilio = None
    try:
        documento_credencial_estudiante = CredencialEstudiante.objects.get(alumno=alumno)
    except ObjectDoesNotExist:
        documento_credencial_estudiante = None
    try:
        documento_kardex = Kardex.objects.get(alumno=alumno)
    except ObjectDoesNotExist:
        documento_kardex = None

    if documento_comprobante_domicilio is None:
        return perfil_alumno(request,False, True)
    elif documento_credencial_estudiante is None:
        return perfil_alumno(request,False, True)
    elif documento_kardex is None:
        return perfil_alumno(request,False, True)

    usuario = get_object_or_404(User, id=request.user.id)
    alumno = get_object_or_404(Alumno, user=usuario)
    alumno.estado_solicitud_id = 2 #Estado 2 es EN EVALUACION... Consultar la tabla estado_solicitud
    alumno.save()
    return redirect('perfil_alumno')


@login_required(login_url='login_alumno')
def aprobar_alumno(request, matricula):
    if request.user.is_superuser:
        alumno = get_object_or_404(Alumno, no_control=matricula)
        alumno.estado_solicitud_id = 3
        alumno.save()
        return redirect('lista_alumnos')
    else:
        return redirect('perfil_alumno')

@login_required(login_url='login_alumno')
def no_aprobar_alumno(request, matricula):
    if request.user.is_superuser:
        alumno = get_object_or_404(Alumno, no_control=matricula)
        alumno.estado_solicitud_id = 4
        alumno.save()
        return redirect('lista_alumnos')
    else:
        return redirect('perfil_alumno')

@login_required(login_url='login_alumno')
def reporte_estado_solicitud(request):
    if request.user.is_superuser:
        carreras = Carrera.objects.all().order_by('id')
        estados_solicitud = Estado_Solicitud.objects.all().order_by('id')
        lista_carreras = []
        for carrera in carreras:
            lista_estados = []
            for estado in estados_solicitud:
                poblacion = len(Alumno.objects.all().filter(carrera=carrera, estado_solicitud=estado))
                lista_estados.append(poblacion)
            lista_carreras.append({carrera.carrera: lista_estados})
        return render(request, "cuentas/reportes/reporte_estado_solicitud.html", {'lista_carreras': lista_carreras})
    else:
        return redirect('perfil_alumno')


@login_required(login_url='login_alumno')
def reporte_aprobados(request): #Muestra una lista de todos los alumnos beneficiados por carrera
    if request.user.is_superuser:
        carreras = Carrera.objects.all().order_by('id')
        lista_carreras = []
        for carrera in carreras:
            lista_alumnos = []
            # estado_solicitud__id 3 es APROBADO
            lista_alumnos_aprobados = Alumno.objects.all().filter(estado_solicitud__id=3, carrera=carrera)
            for alumno in lista_alumnos_aprobados:
                lista_alumnos.append(str(alumno))
                lista_carreras.append({carrera.carrera: lista_alumnos})
        return render(request, 'cuentas/reportes/reporte_aprobados.html', {'lista_carreras': lista_carreras})
    else:
        return redirect('perfil_alumno')