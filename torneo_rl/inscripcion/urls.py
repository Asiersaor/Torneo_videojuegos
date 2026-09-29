from django.urls import path
from .views import inscripcion, panel_admin, editar_inscripcion

urlpatterns = [
    path("inscripcion/", inscripcion, name="inscripcion"),
    path("panel_admin/", panel_admin, name="panel_admin"),
    path("panel_admin/<int:id>/", editar_inscripcion, name="editar_inscripcion")
]