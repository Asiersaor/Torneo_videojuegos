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
        datos = {"username": "angelote", "first_name": "Angel", "last_name": "Merino Lopez", "password1": "ca0", "password2": "ca0"}
        peticion = self.client.post(url, datos)
        usuarios_despues = Usuario.objects.count()
        error = peticion.context["form"].errors
        self.assertEqual(peticion.status_code, 200)
        self.assertEqual(usuarios_despues, usuarios_antes)
        self.assertIn("password2", error)
    def test_form_password1_no_igual_password2(self): 
        usuarios_antes = Usuario.objects.count()
        url = reverse("registro")
        datos = {"username": "angelote", "first_name": "Angel", "last_name": "Merino Lopez", "password1": "caracol04", "password2": "caracol03"}
        peticion = self.client.post(url, datos)
        usuarios_despues = Usuario.objects.count()
        error = peticion.context["form"].errors
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
        error = peticion.context["form"].errors
        self.assertEqual(peticion.status_code, 200)
        self.assertEqual(usuarios_despues, usuarios_antes)
        self.assertIn("username", error)
    def test_form_valido(self):
        usuarios_antes = Usuario.objects.count()
        url = reverse("registro")
        datos = {"username": "angelote", "first_name": "Angel", "last_name": "Merino Lopez", "password1": "caracol04", "password2": "caracol04"}
        peticion = self.client.post(url, datos)
        usuarios_despues = Usuario.objects.count()
        usuario_existente = Usuario.objects.filter(username="angelote").exists()
        self.assertEqual(peticion.status_code, 302)
        self.assertEqual(usuarios_despues, usuarios_antes + 1)
        self.assertTrue(usuario_existente)
class AppInicioSesion(TestCase):
    def test_form_incompleto_no_inicia_sesion(self):
        url = reverse("inicio_sesion")
        datos = {"username": "", "password": ""}
        peticion = self.client.post(url, datos)
        sesion = self.client.session
        self.assertEqual(peticion.status_code, 200)
        self.assertNotIn("_auth_user_id", sesion)

