from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from . import views


from .models import Tarea

urlpatterns = [
    path('', views.materias, name="materias"),
    path('lengua_materna/', views.lengua_materna, name="lengua_materna"),
    path('desafios_matematicos/', views.desafios_matematicos, name="desafios_matematicos"),
    path('ciencias_naturales/', views.ciencias_naturales, name="ciencias_naturales"),
    path('educacion_civica/', views.educacion_civica, name="educacion_civica"),
    path('jalisco/', views.jalisco, name="jalisco"),
    path('ingles/', views.ingles, name="ingles"),
    #path('tareas/', views.tareas, name="tareas"),
    path('subir_respuesta/', views.subir_respuesta, name="subir_respuesta"),
    path('subirtarea/', views.subirtarea, name="subirtarea")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#path('<int:pk>/', views.subir_respuesta, name="subir_respuesta")
