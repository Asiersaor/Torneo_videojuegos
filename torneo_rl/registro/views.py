from django.shortcuts import render, redirect
from .forms import FormularioRegistro
from django.contrib.auth import login

# Create your views here.
def registro(request):
    if request.method == "POST":
        form = FormularioRegistro(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect("")
    else:
        form = FormularioRegistro()
    return render(request, "registro/registro.html", {"form": form}) 
    