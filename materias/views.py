from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.http.request import HttpRequest
from django.shortcuts import render, HttpResponse, redirect
from usuarios.models import Account
from .models import Tarea, Materia, Respuesta


# Views de las materias, menú general e individuales.
@login_required()
def materias(request):
    """Atiende la petición GET /materias que muestra el menú de todas las materias"""
    # Validando si el usuario es maestro
    tipo = request.user.typo
    if tipo == "teacher":
        es_maestro = True
    else:
        es_maestro = False

    return render(request, "materias/materias.html", {"es_maestro":es_maestro})


@login_required()
def lengua_materna(request):
    """Atiende la petición GET /lengua_materna para la vista tareas de Lengua materna"""
    tarea_cn = Tarea.objects.filter(materia_tarea__id = 1)

    # Validando si el usuario es maestro
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

    # Validando si el usuario es maestro
    tipo = request.user.typo
    if tipo == "teacher":
        es_maestro = True
    else:
        es_maestro = False

    return render(request, "materias/ciencias_naturales.html",{"tarea_cn":tarea_cn, "es_maestro":es_maestro})


@login_required()
def desafios_matematicos(request):
    """Atiende la petición GET /desafios_matematicos para la vista de tareas de Desafíos matemáticos"""
    tarea_cn = Tarea.objects.filter(materia_tarea__id = 2)

    # Validando si el usuario es maestro
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

    # Validando si el usuario es maestro
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

    # Validando si el usuario es maestro
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

    # Validando si el usuario es maestro
    tipo = request.user.typo
    if tipo == "teacher":
        es_maestro = True
    else:
        es_maestro = False

    return render(request, "materias/jalisco.html", {"tarea_cn":tarea_cn, "es_maestro":es_maestro})

# Aquí inician funcionalidades para gestionar tareas
@login_required()
def respuesta(request, id_tarea):
    """Función para que los alumnos suban tareas"""
    tarea_cn = Tarea.objects.filter(materia_tarea__id = 3)
    materias = Materia.objects.all()
    tarea_obj = Tarea.objects.get(pk=id_tarea)

    # Validando si el usuario es maestro
    tipo = request.user.typo
    if tipo == "teacher":
        es_maestro = True
    else:
        es_maestro = False

    if request.method == 'POST':
        #materia_f = request.POST.get("materia_tarea2", None)
        tema_f = request.POST.get("tema")
        comentario_f = request.POST.get("comentario")
        materiaId = request.POST.get("materia_tarea", None)
        materia_f = Materia.objects.get(pk=materiaId)

        if request.FILES:
            archivo_f = request.FILES["archivo"]
        else:
            archivo_f = None

        respuesta = Respuesta(
            user=request.user,
            materia_tarea=materia_f,
            tema=tema_f,
            comentario=comentario_f,
        )
        respuesta.save()
        respuesta.archivo=archivo_f
        respuesta.save()

        return HttpResponse("Tu archivo se ha subido correctamente")

    return render(request, "tareas/respuesta.html",{
            "tarea_cn":tarea_cn,
            "tarea_obj":tarea_obj,
            "es_maestro":es_maestro,
            "materias":materias
        }
    )


@login_required()
def subirtarea(request, msg=""):
    """Atiende la petición GET y POST /subirtarea"""
    materias = Materia.objects.all()

    tipo = request.user.typo
    if tipo == "teacher":
        es_maestro = True
    else:
        es_maestro = False

    if es_maestro:
        if request.method == 'POST':
            tema_f = request.POST.get("tema")
            comentario_f = request.POST.get("comentario")
            fecha_f = request.POST.get("fechaLimite")
            materiaId = request.POST.get("materia", None)
            materia_f = Materia.objects.get(pk=materiaId)
            if request.FILES:
                archivo_f = request.FILES["archivo"]
            else:
                archivo_f = None

            tarea = Tarea(
                user=request.user,
                tema=tema_f,
                comentario=comentario_f,
                fechaLimite=fecha_f,
                materia_tarea=materia_f
            )
            tarea.save()
            tarea.archivo=archivo_f
            tarea.save()

            return HttpResponse("La tarea se ha publicado correctamente")
    return render(request, "tareas/subirtarea.html",{
        "es_maestro":es_maestro,
        "materias":materias
        }
    )


@login_required()
def eliminar(request, id_tarea):
    """Atiende las peticiones GET y DELETE para eliminar tareas"""
    # Validando si el usuario es maestro
    tipo = request.user.typo
    if tipo == "teacher":
        es_maestro = True
    else:
        es_maestro = False

    tarea_obj = Tarea.objects.get(pk=id_tarea)
    tarea_obj.delete()

    return redirect("/avisos", {"es_maestro":es_maestro})


@login_required()
def editar(request, id_tarea):
    """Atiende las peticiones GET y POST /editar"""
    tarea_cn = Tarea.objects.filter(materia_tarea__id = 3)
    materias = Materia.objects.all()
    tarea_obj = Tarea.objects.get(pk=id_tarea)

    # Validando si el usuario es maestro
    tipo = request.user.typo
    if tipo == "teacher":
        es_maestro = True
    else:
        es_maestro = False

    if es_maestro:
        # Trabajando POST
        if request.method == 'POST':
            archivo_f = request.FILES["archivo"]

            tema_f = request.POST.get("tema")
            comentario_f = request.POST.get("comentario")
            fecha_f = request.POST.get("fechaLimite")
            #archivo_f = request.POST.get("archivo")
            materiaId = request.POST.get("materia", None)
            materia_f = Materia.objects.get(pk=materiaId)

            tarea_obj.archivo=archivo_f
            tarea_obj.tema = tema_f
            tarea_obj.comentario = comentario_f
            tarea_obj.fechaLimite = fecha_f
            tarea_obj.materia_tarea= materia_f
            tarea_obj.save()

            return HttpResponse("La tarea se ha editado correctamente")

        # Trabajando GET
        return render(request, "materias/editar.html",
        {
            "tarea_cn":tarea_cn,
            "tarea_obj":tarea_obj,
            "es_maestro":es_maestro,
            "materias":materias
        }
        )
    else:
        raise Http404("No tienes permiso de editar")
