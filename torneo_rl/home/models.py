from django.db import models

# Create your models here.
class Torneo(models.Model):
    juego = models.CharField(max_length=30)
    def __str__(self):
        return self.juego
    class Meta:
        verbose_name = "Torneo"
        verbose_name_plural = "Torneos"