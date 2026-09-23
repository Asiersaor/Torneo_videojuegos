from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

#Create your models here.
class Enfrentamiento(models.Model):
   participante_1 = models.ForeignKey("inscripcion.Inscripcion", null=True, blank=True, on_delete=models.SET_NULL, related_name="enfrentamientos_como_p1")
   participante_2 = models.ForeignKey("inscripcion.Inscripcion", null=True, blank=True, on_delete=models.SET_NULL, related_name="enfrentamientos_como_p2")
   victorias_participante_1 = models.IntegerField(default=0)
   victorias_participante_2 = models.IntegerField(default=0)
   ganador_enfrentamiento = models.ForeignKey("inscripcion.Inscripcion", null=True, blank=True, on_delete=models.SET_NULL, related_name="enfrentamientos_ganados")
   class nivel_rondas(models.TextChoices):
      CUARTOS = ("CUARTOS", "Cuartos")
      SEMIFINALES = ("SEMIFINALES", "Semifinales")
      FINAL = ("FINAL", "Final")
   ronda = models.CharField(max_length=30, choices= nivel_rondas, default=nivel_rondas.CUARTOS)
   siguiente_enfrentamiento = models.ForeignKey("self", null=True, blank=True, on_delete=models.SET_NULL)
class Partida(models.Model):
   enfrentamiento = models.ForeignKey(Enfrentamiento, on_delete=models.CASCADE)
   numero_de_partidas = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(3)])
   ganador_partida = models.ForeignKey("inscripcion.Inscripcion", null=True, blank=True, on_delete=models.SET_NULL)