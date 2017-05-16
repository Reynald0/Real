from django.conf.urls import include, url
from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'Real.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^perfil/comprobante_domicilio/$', views.comprobante_domicilio, name='comprobante_domicilio'),
    url(r'^perfil/credencial_estudiante/$', views.credencial_estudiante, name='credencial_estudiante'),
    url(r'^perfil/kardex/$', views.kardex, name='kardex'),
]
