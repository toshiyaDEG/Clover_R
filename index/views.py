from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from index.models import Aviso

from usuarios.models import Account
from materias.models import Materia

from .serializers import MateriaSerializer
from .serializers import AvisoSerializer

from rest_framework import viewsets

import datetime

def index(request):
    """Atiende la petición GET /"""
    return render(request, "index/index.html")


@login_required
def avisos(request):
    """Atiende la petición GET /avisos"""
    avisos = Aviso.objects.all()
    tipo = request.user.typo
    if tipo == "teacher":
        es_maestro = True
    else:
        es_maestro = False

    return render(request, "avisos/avisos.html", {"es_maestro":es_maestro, "avisos":avisos})



@login_required
def subiraviso(request):
    """Atiende la petición GET /subiraviso"""
    avisos = Aviso.objects.all()
    tipo = request.user.typo
    if tipo == "teacher":
        es_maestro = True
    else:
        es_maestro = False

    if es_maestro:
        if request.method == 'POST':
            titulo_f = request.POST.get("titulo")
            contenido_f = request.POST.get("contenido")
            if request.FILES:
                imagen_f = request.FILES["imagen"]
            else:
                imagen_f = None

            aviso = Aviso(
                user=request.user,
                titulo=titulo_f,
                contenido=contenido_f,
            )
            aviso.save()
            aviso.imagen=imagen_f
            aviso.save()

            msg ="Anuncio publicado correctamente"

            return render(request, "avisos/subiraviso.html", {
                "msg":msg,
                "es_maestro": es_maestro,
                "avisos":avisos})

    return render(request, "avisos/subiraviso.html", {"es_maestro": es_maestro})


# Vistas basadas en clases para Django Rest
class MateriaViewSet(viewsets.ModelViewSet):
    """
    API que permite realizar operaciones en la tabla Materia
    """
    # Se define el conjunto de datos sobre el que va a operar la vista,
    # en este caso sobre todos los users disponibles.
    queryset = Materia.objects.all().order_by('id')
    # Se define el Serializador encargado de transformar la peticiones
    # en formato JSON a objetos de Django y de Django a JSON.
    serializer_class = MateriaSerializer


class AvisoViewSet(viewsets.ModelViewSet):
    """
    API que permite realizar operaciones en la tabla Avisos
    """
    # Se define el conjunto de datos sobre el que va a operar la vista,
    # en este caso sobre todos los users disponibles.
    queryset = Aviso.objects.all().order_by('id')
    # Se define el Serializador encargado de transformar la peticiones
    # en formato JSON a objetos de Django y de Django a JSON.
    serializer_class = AvisoSerializer
