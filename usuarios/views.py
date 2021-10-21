from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from usuarios.forms import RegistrationForm
from usuarios.models import Account
from django.contrib.auth.decorators import login_required


# View desde la cual el maestro puede registrar alumnos
@login_required()
def registration_view(request):
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