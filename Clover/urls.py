"""Clover URL Configuration
"""
from django.urls import path, include, re_path
from django.conf import settings
from django.contrib import admin
from django.views.static import serve

urlpatterns = [
    path('', include("index.urls")),
    path('materias/', include("materias.urls")),
    path('usuarios/', include("usuarios.urls")),
    path('admin/', admin.site.urls)
]

if settings.DEBUG:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        })
    ]