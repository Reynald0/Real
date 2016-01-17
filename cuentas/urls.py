from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'Real.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.inicio, name='inicio'),
    url(r'^informacion/$', views.informacion, name='informacion'),
    url(r'^registro/$', views.registro_alumno, name='registro'),
    url(r'^registrado/$', views.registrado, name='registrado'),
    url(r'^noticias/$', views.noticias, name='noticias'),
    url(r'^login/$', views.login_alumno, name='login_alumno'),
    url(r'^logout/$', views.logout_alumno, name='logout_alumno'),
    url(r'^contacto/$', views.contacto, name='contacto'),
    url(r'^lista_alumnos/$', views.lista_alumnos, name='lista_alumnos'),
]
