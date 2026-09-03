from django.shortcuts import render
from .models import Torneo
# Create your views here.
def listado_torneos(request):
    torneos = Torneo.objects.all
    return render(request, "home/listado.html", {"torneos": torneos})
def inicio(request):
    return render(request, "home/inicio.html")