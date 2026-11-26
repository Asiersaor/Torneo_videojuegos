from django.urls import path
from .views import registro, inicio_sesion, cierre_sesion, cuenta_perfil, panel_admin, editar_usuario, eliminar_usuario

# Urls de la aplicacion de "registro", "inicio de sesion" y de "panel administrador".

urlpatterns = [
    path("registro/", registro, name="registro"),
    path("login/", inicio_sesion, name="inicio_sesion"),
    path("logout/", cierre_sesion, name="cerrar_sesion"),
    path("perfil/", cuenta_perfil, name="cuenta_perfil"),
    path("panel_admin/", panel_admin, name="panel_admin"),
    path("panel_admin/<int:id>/editar_usuario", editar_usuario, name="editar_usuario"),
    path("panel_admin/<int:id>/eliminar_usuario/", eliminar_usuario, name="eliminar_usuario")
]