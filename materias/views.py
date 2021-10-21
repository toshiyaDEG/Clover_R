from django.http import Http404
from django.http.request import HttpRequest
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from .models import Tarea, Materia



# View para subir respuestas del alumno
@login_required()
def subir_respuesta(request):
    """Atiende la petición GET /"""
    return render(request, "tareas/subir_respuesta.html")
# def subir_respuesta(request, pk):
#     """Atiende la petición GET /"""
#     return render(request, "tareas/subir_respuesta.html", {id:pk})

@login_required()
def subirtarea(request, msg=""):
    """Atiende la petición GET y POST /subirtarea"""
    materias = Materia.objects.all()
    # es_maestro = request.user.groups.filter(name="maestro").exists()
    tipo = request.user.typo
    if tipo == "teacher":
        es_maestro = True
    else:
        es_maestro = False

    if es_maestro:
        if request.method == 'POST':
        #         archivof = request.FILES["archivo"]
            archivoform = request.FILES["archivo"]
            materiaidform = request.POST.get("materia", None)
            print(materiaidform)
            materiatareaobj = Materia.objects.get(pk=materiaidform)

            Tarea.objects.create(
                archivo=archivoform,
                tema = request.POST["tema"],
                comentario = request.POST["comentario"],
                fechaLimite = request.POST["fechaLimite"],
                materia_tarea= materiatareaobj
            )
            return HttpResponse("Tu archivo se ha subido correctamente")
        return render(request, "tareas/subirtarea.html",{"es_maestro":es_maestro,"materias":materias})

# Views de las materias
@login_required()
def materias(request):
    """Atiende la petición GET /materias que muestra el menú de todas las materias"""
    return render(request, "materias/materias.html")


@login_required()
def lengua_materna(request):
    """Atiende la petición GET /lengua_materna para la vista tareas de Lengua materna"""
    tarea_cn = Tarea.objects.filter(materia_tarea__id = 1)
    tipo = request.user.typo
    if tipo == "teacher":
        es_maestro = True
    else:
        es_maestro = False

    return render(request, "materias/lengua_materna.html", {"tarea_cn":tarea_cn, "es_maestro":es_maestro})


# Aquí empiezan las views de las materias por individual
@login_required()
def ciencias_naturales(request):
    """Atiende la petición GET /ciencias_natuarles para la vista de tareas de Ciencias naturales"""
    tarea_cn = Tarea.objects.filter(materia_tarea__id = 3)
    tipo = request.user.typo
    if tipo == "teacher":
        es_maestro = True
    else:
        es_maestro = False
    print(es_maestro)

    return render(request, "materias/ciencias_naturales.html",{"tarea_cn":tarea_cn, "es_maestro":es_maestro})



@login_required()
def desafios_matematicos(request):
    """Atiende la petición GET /desafios_matematicos para la vista de tareas de Desafíos matemáticos"""
    tarea_cn = Tarea.objects.filter(materia_tarea__id = 2)
    tipo = request.user.typo
    if tipo == "teacher":
        es_maestro = True
    else:
        es_maestro = False

    return render(request, "materias/desafios_matematicos.html", {"tarea_cn":tarea_cn, "es_maestro":es_maestro})


@login_required()
def educacion_civica(request):
    """Atiende la petición GET /educacion_civica para la vista de tareas de Educación Cívica y Ética"""
    tarea_cn = Tarea.objects.filter(materia_tarea__id= 4)
    tipo = request.user.typo
    if tipo == "teacher":
        es_maestro = True
    else:
        es_maestro = False

    return render(request, "materias/educacion_civica.html", {"tarea_cn":tarea_cn, "es_maestro":es_maestro})


@login_required()
def ingles (request):
    """Atiende la petición GET /ingles para la vista de tareas de Inglés"""
    tarea_cn = Tarea.objects.filter(materia_tarea__id = 6)
    tipo = request.user.typo
    if tipo == "teacher":
        es_maestro = True
    else:
        es_maestro = False

    return render(request, "materias/ingles.html", {"tarea_cn":tarea_cn, "es_maestro":es_maestro})


@login_required()
def jalisco(request):
    """Atiende la petición GET para la vista de tareas de Jalisco"""
    tarea_cn = Tarea.objects.filter(materia_tarea__id = 5)
    tipo = request.user.typo
    if tipo == "teacher":
        es_maestro = True
    else:
        es_maestro = False

    return render(request, "materias/jalisco.html", {"tarea_cn":tarea_cn, "es_maestro":es_maestro})