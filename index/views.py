from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


def index(request):
    """Atiende la petición GET /"""
    return render(request, "index/index.html")


@login_required
def avisos(request):
    """Atiende la petición GET /"""
    #es_maestro = request.user.groups.filter(name="maestro").exists()
    tipo = request.user.typo
    if tipo == "teacher":
        es_maestro = True
    else:
        es_maestro = False

    return render(request, "avisos/avisos.html", { "es_maestro": es_maestro })


