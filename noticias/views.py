from django.shortcuts import render
from django.utils import timezone
from .models import Noticia

def noticias(request):
    if not request.user.is_authenticated():
        return login_alumno(request)
    noticias = Noticia.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('-fecha_publicacion')
    return render(request, 'noticias/lista_noticias.html', {'noticias': noticias})
