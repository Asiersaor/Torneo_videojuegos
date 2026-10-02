from django.urls import path
from .views import registro, inicio_sesion, cierre_sesion, cuenta_perfil

urlpatterns = [
    path("registro/", registro, name="registro"),
    path("login/", inicio_sesion, name="inicio_sesion"),
    path("logout/", cierre_sesion, name="cerrar_sesion"),
    path("perfil/", cuenta_perfil, name="cuenta_perfil")
]