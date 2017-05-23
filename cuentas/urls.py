from django.conf.urls import include, url
from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'Real.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.inicio, name='inicio'),
    url(r'^informacion/$', views.informacion, name='informacion'),
    url(r'^registro/$', views.registro_alumno, name='registro'),
    url(r'^login/$', views.login_alumno, name='login_alumno'),
    url(r'^logout/$', views.logout_alumno, name='logout_alumno'),
    url(r'^perfil/$', views.perfil_alumno, name='perfil_alumno'),
    url(r'^perfil/editar/$', views.editar_perfil_alumno, name='editar_perfil_alumno'),
    url(r'^perfil/solicitar_beca/$', views.solicitar_beca, name='solicitar_beca'),
    url(r'^perfil/cambiar_pass/$', views.cambiar_pass, name='cambiar_pass'),
    url(r'^contacto/$', views.contacto, name='contacto'),
    url(r'^lista_alumnos/$', views.lista_alumnos, name='lista_alumnos'),
    url(r'^lista_alumnos/en_proceso/', views.lista_alumnos_en_proceso, name='lista_alumnos_en_proceso'),
    url(r'^lista_alumnos/en_evaluacion/', views.lista_alumnos_en_evaluacion, name='lista_alumnos_en_evaluacion'),
    url(r'^lista_alumnos/aprobados/', views.lista_alumnos_aprobados, name='lista_alumnos_aprobados'),
    url(r'^lista_alumnos/no_aprobados/', views.lista_alumnos_no_aprobados, name='lista_alumnos_no_aprobados'),
    url(r'^lista_alumnos/aprobar/(?P<matricula>[0-9]+)$', views.aprobar_alumno, name='aprobar_alumno'),
    url(r'^lista_alumnos/no_aprobar/(?P<matricula>[0-9]+)$', views.no_aprobar_alumno, name='no_aprobar_alumno'),
]
