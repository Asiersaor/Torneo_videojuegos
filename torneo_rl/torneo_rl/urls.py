
from django.contrib import admin
from django.urls import path, include   

#Urls de todas las aplicaciones.

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('registro.urls')),
    path('', include('home.urls')),
    path('', include('inscripcion.urls')),
    path('', include('torneo.urls'))
]
