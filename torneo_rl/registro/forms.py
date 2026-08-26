from django import forms
from .models import Usuario
from django.contrib.auth.forms import UserCreationForm

class FormularioRegistro(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Usuario
        fields = ["username", "first_name", "last_name"]
