from django.urls import path
from .views import inicio ,listado_torneos

urlpatterns = [
    path("rl/", inicio, name="torneo_rl"),
    path("", listado_torneos, name="home")
]