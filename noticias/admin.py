from django.contrib import admin
from .models import Noticia

class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'texto', 'fecha_publicacion')

admin.site.register(Noticia, NoticiaAdmin)
