from django.shortcuts import render, redirect
from .forms import FormularioInscripcion
from django.contrib.auth.decorators import login_required
from .models import Inscripcion

# Create your views here.
@login_required
def inscripcion(request):
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

@login_required
def panel_admin(request):
    if request.user.rol != "admin":
        return redirect("home")
    inscripciones = list(Inscripcion.objects.all())
    return render(request, "inscripcion/panel_admin.html", {"inscripciones": inscripciones})

@login_required
def editar_inscripcion(request, id):
    if request.user.rol != "admin":
        return redirect("home")
    inscripcion_existente = Inscripcion.objects.get(id=id)
    if request.method == "POST":
        form = FormularioInscripcion(request.POST,instance=inscripcion_existente)
        if form.is_valid():
            inscripcion = form.save(commit=False)
            inscripcion.save()
            return redirect("panel_admin")
        else:
            form = FormularioInscripcion(instance=inscripcion_existente)
    else:
        form = FormularioInscripcion(instance=inscripcion_existente)
    return render(request, "inscripcion/inscripcion.html", {"form": form})
