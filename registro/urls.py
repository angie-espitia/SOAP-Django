from django.conf.urls import url
from django.contrib import admin
from main.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^docentes/$', listar_do, name='listar_do'),
    url(r'^docentes/movimiento/$', guardar_do, name='guardar_do'),    
    url(r'^docentes/movimiento/avt/$', actualizar_do, name='actualizar_do'),

    url(r'^docentes/movimiento/list/$', listar_docente, name='listar_docente'),
    url(r'^docentes/movmiento/save/$', guardar_docente, name='guardar_docente'),    
    url(r'^docentes/movmiento/act/$', actualizar_docente, name='actualizar_docente'),    
    url(r'^docentes/movmiento/act_guar/$', actualizar_guardar_docente, name='actualizar_guardar_docente'), 
    url(r'^docentes/movmiento/remove/$', eliminar_docente, name='eliminar_docente'), 

    url(r'^salones/$', salones, name='salones'),
    url(r'^salones/movimiento/list/$', listar_salones, name='listar_salones'),
    url(r'^salones/movmiento/save/$', guardar_salon, name='guardar_salon'),    
    url(r'^salones/movmiento/act/$', actualizar_salon, name='actualizar_salon'),    
    url(r'^salones/movmiento/act_guar/$', actualizar_guardar_salon, name='actualizar_guardar_salon'), 
    url(r'^salones/movmiento/remove/$', eliminar_salon, name='eliminar_salon'), 

    url(r'^$', index, name='index'), 
    url(r'^registros/movimiento/list/$', listar_registro, name='listar_registro'),
    url(r'^registros/movmiento/save/$', guardar_registro, name='guardar_registro'),    
    url(r'^registros/movmiento/act/$', actualizar_registro, name='actualizar_registro'),    
    url(r'^registros/movmiento/act_guar/$', actualizar_guardar_registro, name='actualizar_guardar_registro'), 
    url(r'^registros/movmiento/remove/$', eliminar_registro, name='eliminar_registro'),
    url(r'^registros/movmiento/docente/$', listar_docentes2, name='listar_docentes2'),
    url(r'^registros/movmiento/salon/$', listar_salones2, name='listar_salones2'),
    url(r'^registros/movmiento/filtrar/$', filtrar_registro, name='filtrar_registro'),
    url(r'^registros/movmiento/filtrar2/$', filtrar_registro2, name='filtrar_registro2'),

]
