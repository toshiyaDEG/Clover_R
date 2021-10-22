from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from index.models import Aviso

from usuarios.models import Account



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

            return render(request, "avisos/avisos.html", { "es_maestro": es_maestro, "avisos":avisos})

    return render(request, "avisos/subiraviso.html", {"es_maestro": es_maestro})
