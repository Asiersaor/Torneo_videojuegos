from django.shortcuts import render, redirect
from .forms import FormularioInscripcion
from django.contrib.auth.decorators import login_required

# Vistas de la aplicacion "inscripcion".

@login_required
def inscripcion(request): # Vista para mostrar la plantilla junto al formulario.
    if request.method == "POST":
        form = FormularioInscripcion(request.POST)
        if form.is_valid():
            inscripcion = form.save(commit=False)
            inscripcion.usuario = request.user
            inscripcion.save()
            return redirect("torneo_rl")
    else:
        form = FormularioInscripcion()
    return render(request, "inscripcion/inscripcion.html", {"form": form})

