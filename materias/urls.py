from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from . import views


from .models import Tarea

urlpatterns = [
    path('', views.materias, name="materias"),
    path('calificar/<int:id_respuesta>/', views.calificar, name="calificar"),
    path('ciencias_naturales/', views.ciencias_naturales, name="ciencias_naturales"),
    path('desafios_matematicos/', views.desafios_matematicos, name="desafios_matematicos"),
    path('educacion_civica/', views.educacion_civica, name="educacion_civica"),
    path('editar/<int:id_tarea>/', views.editar, name="editar"),
    path('eliminar/<int:id_tarea>/', views.eliminar, name="eliminar"),
    path('ingles/', views.ingles, name="ingles"),
    path('jalisco/', views.jalisco, name="jalisco"),
    path('lengua_materna/', views.lengua_materna, name="lengua_materna"),
    path('respuesta/<int:id_tarea>/', views.respuesta, name="respuesta"),
    path('revisar_tareas/<int:id_alumno>/', views.revisar_tareas, name="revisar_tareas"),
    path('subirtarea/', views.subirtarea, name="subirtarea"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

