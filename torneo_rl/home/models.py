from django.db import models

# Modelo de Torneo.

class Torneo(models.Model):
    juego = models.CharField(max_length=30)
    def __str__(self):
        return self.juego

# Clase Meta para distinguir plurales y singulares.

    class Meta:
        verbose_name = "Torneo"
        verbose_name_plural = "Torneos"