from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

# Modelo para el registro y el guardado de usuario.

class Usuario(AbstractUser): # Metodo con AbstractUser para usar el objeto de usuarios por defecto de django.
    ROL_CHOICES = [
        ("admin", "Administrador"),
        ("usuario", "Usuario"),
    ]
    rol = models.CharField(max_length=20, choices=ROL_CHOICES, default="usuario")
