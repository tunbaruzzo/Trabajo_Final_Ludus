from django.conf.urls.static import static
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from Principal.views import *

urlpatterns =[
    path('inicio/', inicio, name= 'inicio'),
    path('programa/', programa, name= 'programa'),
    path('instructores/', instructores, name= 'instructores'),
    path('profesionales/', profesionales, name= 'profesionales'),
    path('miembros/',miembros, name= 'miembros'),
    path('consultas/', consultas, name= 'consultas'),
    path('sobre_mi/', sobre_mi, name= 'sobre_mi'),
    path('paginaerror/', paginaerror, name= 'paginaerror'),
    path('formulario_miembro/', form_miembro, name= 'formulario_miembro'),
    path('formularioinstructor/', form_instructor, name= 'formularioinstructor'),
    path('formularioprograma/', form_programa, name= 'formularioprograma'),
    path('leer_miembros/', leer_miembros, name= 'listamiembros'),
    path('eliminar_miembros/<int:id>', eliminar_miembros, name= 'eliminar_miembros'),
    path('editar_miembros/<int:id>', editar_miembros, name= 'editar_miembros'),
    path('listadeprogramas/', listadeprogramas.as_view(), name= 'listadeprogramas'),
    path('programadetail/ <pk>', programadetail.as_view(), name= 'programadetail'),
    path('programacreacion/', programacreacion.as_view(), name= 'programacreacion'),
    path('programaeditar/<pk>', programaeditar.as_view(), name= 'programaeditar'),
    path('programaeliminar/<pk>', programaeliminar.as_view(), name= 'programaeliminar'),
    path('login/', login_ludus, name= 'login'),
    path('registro/', registro_ludus, name= 'registro'),
    path('logout/', LogoutView.as_view(template_name= "logout.html"), name='logout')

]