from django.urls import path
from . import views

urlpatterns = [
    path('', views.registration_view, name="registro"),
    path('alumnos/', views.alumnos, name="alumnos")
]
