from django import forms
from .models import Inscripcion

# Formulario para la inscripcion.

class FormularioInscripcion(forms.ModelForm):
    class Meta:
        model = Inscripcion
        fields = ["nivel", "juego"]