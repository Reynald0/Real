from django.contrib import admin
from .models import ComprobanteDomicilio, CredencialEstudiante, Kardex


class ComprobanteDomicilioAdmin(admin.ModelAdmin):
    list_display = ('alumno', 'url_documento')


class CredencialEstudianteAdmin(admin.ModelAdmin):
    list_display = ('alumno', 'url_documento')


class KardexAdmin(admin.ModelAdmin):
    list_display = ('alumno', 'url_documento')


admin.site.register(ComprobanteDomicilio, ComprobanteDomicilioAdmin)
admin.site.register(CredencialEstudiante, CredencialEstudianteAdmin)
admin.site.register(Kardex, KardexAdmin)
