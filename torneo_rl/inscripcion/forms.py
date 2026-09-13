from django import forms
from .models import Inscripcion

class FormularioInscripcion(forms.ModelForm):
    class Meta:
        model = Inscripcion
        fields = ["nivel", "juego"]