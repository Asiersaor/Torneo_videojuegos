from django.urls import path
from .views import inscripcion

# Urls de la aplicacion de "inscripcion".

urlpatterns = [
    path("inscripcion/", inscripcion, name="inscripcion")
]