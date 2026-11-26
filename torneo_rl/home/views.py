from django.shortcuts import render
from .models import Torneo

# Vistas de la aplicacion "home".

def listado_torneos(request): # Vista listado torneos.
    torneos = Torneo.objects.all()
    return render(request, "home/listado.html", {"torneos": torneos})

def inicio(request): # Vista para mostrar la pagina de inicio.
    return render(request, "home/inicio.html")