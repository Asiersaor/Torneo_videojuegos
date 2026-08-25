from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Usuario(AbstractUser):
    ROL_CHOICES = [
        ("admin", "Administrador"),
        ("usuario", "Usuario"),
    ]
    rol = models.CharField(max_length=20, choices=ROL_CHOICES, default="usuario")
