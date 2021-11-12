from django.http.response import Http404
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import login, authenticate
from usuarios.forms import RegistrationForm
from usuarios.models import Account
from django.contrib.auth.decorators import login_required


# View desde la cual el maestro puede registrar alumnos
@login_required()
def registration_view(request):
    """Atiende la petición GET /usuarios"""
    tipo = request.user.typo
    if tipo == "teacher":
        es_maestro = True
    else:
        es_maestro = False
    context = {}
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            account = authenticate(email=email, password=raw_password, first_name=first_name, last_name=last_name)
            login(request, account)
            return redirect('avisos')
        else:
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, "usuarios/registro.html", context)


# View para mostrar la lista de alumnos
@login_required()
def alumnos(request):
    """Atiende la petición GET /alumnos"""
    grupo = Account.objects.filter(typo = "student")
    tipo = request.user.typo
    if tipo == "teacher":
        es_maestro = True
    else:
        es_maestro = False

    return render(request, "usuarios/alumnos.html", {"grupo":grupo, "es_maestro":es_maestro})

# View para eliminar alumnos
@login_required()
def eliminar_alumno(request, id_alumno):
    """Elimina usuarios de la lista de alumnos"""
    # Validando si el usuario es maestro
    tipo = request.user.typo
    if tipo == "teacher":
        es_maestro = True
    else:
        es_maestro = False


    alumno = Account.objects.get(pk=id_alumno)
    alumno.delete()

    return redirect("/avisos", {"es_maestro":es_maestro})


def editar_alumno(request, id_alumno):
    """Atiende la petición GET /editar_alumno"""
    alumno = Account.objects.get(pk=id_alumno)

    tipo = request.user.typo
    if tipo == "teacher":
        es_maestro = True
    else:
        es_maestro = False

    if es_maestro:
        if request.method == 'POST':
            username_f = request.POST.get("username")
            email_f = request.POST.get("email")
            first_name = request.POST.get("first_name")
            last_name = request.POST.get("last_name")

            alumno.username=username_f
            alumno.email=email_f
            alumno.first_name=first_name
            alumno.last_name=last_name
            alumno.save()

            return HttpResponse("Alumno editado correctamente")
        return render(request, "usuarios/edit_alumno.html",
    {
        "es_maestro":es_maestro,
        "alumno":alumno
    }
    )
    else:
        raise Http404("No tienes permiso para editar")

