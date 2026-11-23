from django.test import TestCase
from .models import Inscripcion
from django.urls import reverse
from django.contrib.auth import get_user_model
from home.models import Torneo

Usuario = get_user_model()

# Create your tests here.
class AppInscripcion(TestCase):
    def setUp(self):
        self.usuario = Usuario.objects.create_user(username="angelote", password="caracol04")
        self.client.force_login(self.usuario)
        self.torneo = Torneo.objects.create(juego= "Rocket League")
    def test_form_inscripcion_vacia(self):
        inscripcion_antes = Inscripcion.objects.count()
        url = reverse("inscripcion")
        datos = {"nivel":"", "juego":""}
        peticion = self.client.post(url, datos)
        error = peticion.context["form"].errors
        inscripcion_despues = Inscripcion.objects.count()
        self.assertEqual(peticion.status_code, 200)
        self.assertEqual(inscripcion_despues, inscripcion_antes)
        self.assertIn("nivel", error)
        self.assertIn("juego", error)
    def test_form_inscripcion_correcta(self):
        inscripcion_antes = Inscripcion.objects.count()
        url = reverse("inscripcion")
        datos = {"nivel":"MID", "juego":self.torneo.pk}
        peticion = self.client.post(url, datos)
        inscripcion_despues = Inscripcion.objects.count()
        self.assertRedirects(peticion, reverse("torneo_rl"))
        self.assertEqual(inscripcion_despues, inscripcion_antes + 1)
    def test_form_sin_inicio_sesion(self):
        self.client.logout()
        inscripcion_antes = Inscripcion.objects.count()
        url = reverse("inscripcion")
        datos = {"nivel":"MID", "juego":self.torneo.pk}
        peticion = self.client.post(url, datos)
        inscripcion_despues = Inscripcion.objects.count()
        self.assertEqual(peticion.status_code, 302)
        self.assertEqual(inscripcion_despues, inscripcion_antes)
    def test_form_incompleto_un_campo(self):
        inscripcion_antes = Inscripcion.objects.count()
        url = reverse("inscripcion")
        datos = {"nivel":"MID", "juego":""}
        peticion = self.client.post(url, datos)
        error = peticion.context["form"].errors
        inscripcion_despues = Inscripcion.objects.count()
        self.assertEqual(peticion.status_code, 200)
        self.assertEqual(inscripcion_despues, inscripcion_antes)
        self.assertIn("juego", error)

