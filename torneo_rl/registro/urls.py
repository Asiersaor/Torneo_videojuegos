from django.urls import path
from .views import registro, inicio_sesion, cierre_sesion

urlpatterns = [
    path("registro/", registro, name="registro"),
    path("login/", inicio_sesion, name="inicio_sesion"),
    path("logout/", cierre_sesion, name="cerrar_sesion")
]