from django.contrib import admin
from .models import Noticia

class NoticiaAdmin(admin.ModelAdmin): # No estoy seguro del funcionamiento y declaracion de esta clase
    #Clase auxiliar que permite ver los campos especificados por medio de una tupla
    # llamada list_display, en la tupla se enlistan los campos a mostrar, no es necesario que sean todos los del modelo
    #En este caso se mandan a mostrar los campos titulo, texto y fecha_publicacion del modelo Noticia
    list_display = ('titulo', 'texto', 'fecha_publicacion')

admin.site.register(Noticia, NoticiaAdmin) #Registra al modelo Noticia en el panel de administracion
