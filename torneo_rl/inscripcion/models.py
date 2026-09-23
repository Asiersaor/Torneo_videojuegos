from django.db import models

# Create your models here.
class Inscripcion(models.Model):
   class nivel_participante(models.TextChoices):
        AMATEUR = ("LOW","Amateur")
        MIDDLE = ("MID", "Normal")
        PRO_PLAYER = ("PRO", "Experto")
   usuario = models.ForeignKey("registro.Usuario", on_delete=models.CASCADE)
   juego = models.ForeignKey("home.Torneo", on_delete=models.CASCADE)
   nivel = models.CharField(max_length=30, choices= nivel_participante, default=nivel_participante.MIDDLE)
   def __str__(self):
       return f"{self.usuario.username} ({self.get_nivel_display()})"