from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'Real.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('cuentas.urls')), #Asume que el index esta dentro de la aplicacion cuentas
    url(r'', include('noticias.urls')), #Escanea la url y cacha las url que estan en la aplicacion noticias
]
