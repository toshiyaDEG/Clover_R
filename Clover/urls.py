"""Clover URL Configuration
"""
from django.urls import path, include, re_path
from django.conf import settings
from django.contrib import admin
from django.views.static import serve
from rest_framework import routers
from materias import views
from index import views

# Agregando rutas para django rest
router = routers.DefaultRouter() # /api/
router.register(r'materias', views.MateriaViewSet) # /api/zonas/
router.register(r'avisos', views.AvisoViewSet) # /api/tours/

urlpatterns = [
    path('', include("index.urls")),
    path('admin/', admin.site.urls),
    path('materias/', include("materias.urls")),
    path('usuarios/', include("usuarios.urls")),
    # Rutas para la url /api/
    path("api/", include(router.urls)),
    # Rutas para la autenticación url /api/auth/
    path("api/auth/", include("rest_framework.urls", namespace="rest_framework")),
]

if settings.DEBUG:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        })
    ]