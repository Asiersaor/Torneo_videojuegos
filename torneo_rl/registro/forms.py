from django import forms
from .models import Usuario
from django.contrib.auth.forms import UserCreationForm

# Formularios para la aplicacion de "registro".

class FormularioRegistro(UserCreationForm): # Formulario para el registro de usuarios.
    class Meta(UserCreationForm.Meta):
        model = Usuario
        fields = ["username", "first_name", "last_name"]

class ModificacionCuenta(forms.ModelForm): # Formulario para la modificacion de usuarios.
    class Meta:
        model = Usuario
        fields = ["username", "first_name", "last_name", "rol"]
