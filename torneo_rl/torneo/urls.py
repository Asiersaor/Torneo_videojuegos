from django.urls import path
from .views import generar_torneo, encuentros, ver_torneo

urlpatterns = [
    path("generador_torneo_rl/", generar_torneo, name= "generador_torneo_rl"),
    path("encuentros_torneo_rl/<int:id>/", encuentros, name= "encuentros_torneo_rl"),
    path("vista_torneo_rl/", ver_torneo, name= "vista_torneo_rl")
]