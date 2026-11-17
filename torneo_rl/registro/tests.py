from django.test import TestCase
from .models import Usuario
from django.urls import reverse

# Create your tests here.
class AppRegistro(TestCase):
    def test_form_incompleto_no_crea_usuario(self):
        usuarios_antes = Usuario.objects.count()
        url = reverse("registro")
        datos = {"username": "", "first_name": "Angel", "last_name": "", "password1": "caracol04", "password2": "caracol04"}
        peticion = self.client.post(url, datos)
        usuarios_despues = Usuario.objects.count()
        self.assertEqual(peticion.status_code, 200)
        self.assertEqual(usuarios_despues, usuarios_antes)
    def test_form_password_corta(self):
        usuarios_antes = Usuario.objects.count()
        url = reverse("registro")
        datos = {"username": "angelote", "first_name": "Angel", "last_name": "Merino Lopez", "password1": "caracol0", "password2": "ca0"}
        peticion = self.client.post(url, datos)
        usuarios_despues = Usuario.objects.count()
        error = peticion.context["form"].errors
        self.assertEqual(peticion.status_code, 200)
        self.assertEqual(usuarios_despues, usuarios_antes)
        self.assertIn("password2", error)
    def test_form_password1_no_igual_password2(self): # No terminado
        usuarios_antes = Usuario.objects.count()
        url = reverse("registro")
        datos = {"username": "angelote", "first_name": "Angel", "last_name": "Merino Lopez", "password1": "caracol04", "password2": "caracol03"}
        peticion = self.client.post(url, datos)
        usuarios_despues = Usuario.objects.count()
        error = peticion.context["form"].errors
        print(error)
        self.assertEqual(peticion.status_code, 200)
        self.assertEqual(usuarios_despues, usuarios_antes)
        self.assertIn("password2", error)
    def test_usuario_duplicado(self):
        Usuario.objects.create(username="angelote", first_name="Angel", last_name="Merino Lopez")
        usuarios_antes = Usuario.objects.count()
        url = reverse("registro")
        datos = {"username": "angelote", "first_name": "Angel", "last_name": "Merino Lopez", "password1": "caracol04", "password2": "caracol04"}
        peticion = self.client.post(url, datos)
        usuarios_despues = Usuario.objects.count()
        self.assertEqual(peticion.status_code, 200)
        self.assertEqual(usuarios_despues, usuarios_antes)
