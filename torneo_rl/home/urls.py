from django.urls import path
from .views import inicio ,listado_torneos

# Urls de la aplicacion de "home".

urlpatterns = [
    path("rl/", inicio, name="torneo_rl"),
    path("", listado_torneos, name="home")
]