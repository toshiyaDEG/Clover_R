from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from . import models
from usuarios.models import Account



def index(request):
    """Atiende la petición GET /"""
    return render(request, "index/index.html")


@login_required
def avisos(request):
    """Atiende la petición GET /avisos"""
    #es_maestro = request.user.groups.filter(name="maestro").exists()
    es_maestro = Account.objects.filter(typo = "teacher").exists()

    return render(request, "avisos/avisos.html", { "es_maestro": es_maestro })



@login_required
def subiraviso(request):
    """Atiende la petición GET /subiraviso"""
    es_maestro = Account.objects.filter(typo = "teacher").exists()


    return render(request, "avisos/subiraviso.html", { "es_maestro": es_maestro })
