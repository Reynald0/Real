from django.shortcuts import render
from django.utils import timezone
from .models import Noticia
from cuentas.views import login_alumno

def noticias(request):
    if not request.user.is_authenticated(): #Si el usuario NO esta autenticado (logeado)
        return login_alumno(request) #Entonces lo manda al login de alumnos
    # Obtiene todos los objetos noticias y los filtra por fecha de publicacion desde el mas actual (arriba) hasta el mas antiguo (abajo)
    noticias = Noticia.objects.all().filter(fecha_publicacion__lte=timezone.now()).order_by('-fecha_publicacion')
    #Regresa el html lista_noticias renderizado y envia la lista de las noticias al html lista_noticias
    return render(request, 'noticias/lista_noticias.html', {'noticias': noticias})
