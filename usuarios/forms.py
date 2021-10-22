from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Account


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60)
    first_name = forms.CharField(max_length=60)
    last_name = forms.CharField(max_length=60)
# help_text='Requerido. Agrega un correo válido'

    class Meta:
        model = Account
        fields = ("username", "email", "first_name", "last_name", "password1", "password2")
