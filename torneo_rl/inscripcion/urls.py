from django.urls import path
from .views import inscripcion

urlpatterns = [
    path("inscripcion/", inscripcion, name="inscripcion")
]