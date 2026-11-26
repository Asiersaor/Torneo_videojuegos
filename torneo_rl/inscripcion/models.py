from django.db import models

# Modelo de inscripcion para asignar el formulario. 

class Inscripcion(models.Model):
   class nivel_participante(models.TextChoices): # Clase con TextChoices para crear un desplegable para asignar niveles.
        AMATEUR = ("LOW","Amateur")
        MIDDLE = ("MID", "Normal")
        PRO_PLAYER = ("PRO", "Experto")
   usuario = models.ForeignKey("registro.Usuario", on_delete=models.CASCADE)
   juego = models.ForeignKey("home.Torneo", on_delete=models.CASCADE)
   nivel = models.CharField(max_length=30, choices= nivel_participante, default=nivel_participante.MIDDLE)

   def __str__(self): # Metodo para hacer visible los datos en la plantilla.
       return f"{self.usuario.username} ({self.get_nivel_display()})"