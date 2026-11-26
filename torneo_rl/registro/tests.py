from django.test import TestCase
from .models import Usuario
from django.urls import reverse

# Clase para la creacion de tests y apartado de "registro".

class AppRegistro(TestCase):

    def test_form_incompleto_no_crea_usuario(self): # Test para la comprobacion del comportamiento del formulario con algun campo vacio.
        usuarios_antes = Usuario.objects.count()
        url = reverse("registro")
        datos = {"username": "", "first_name": "Angel", "last_name": "", "password1": "caracol04", "password2": "caracol04"}
        peticion = self.client.post(url, datos)
        usuarios_despues = Usuario.objects.count()
        self.assertEqual(peticion.status_code, 200)
        self.assertEqual(usuarios_despues, usuarios_antes)

    def test_form_password_corta(self): # Test para la comprobacion de la contraseña del formulario cuando es corta.
        usuarios_antes = Usuario.objects.count()
        url = reverse("registro")
        datos = {"username": "angelote", "first_name": "Angel", "last_name": "Merino Lopez", "password1": "ca0", "password2": "ca0"}
        peticion = self.client.post(url, datos)
        usuarios_despues = Usuario.objects.count()
        error = peticion.context["form"].errors
        self.assertEqual(peticion.status_code, 200)
        self.assertEqual(usuarios_despues, usuarios_antes)
        self.assertIn("password2", error)

    def test_form_password1_no_igual_password2(self): # Test para la comprobacion del formulario cuando las contraseñas no coinciden.
        usuarios_antes = Usuario.objects.count()
        url = reverse("registro")
        datos = {"username": "angelote", "first_name": "Angel", "last_name": "Merino Lopez", "password1": "caracol04", "password2": "caracol03"}
        peticion = self.client.post(url, datos)
        usuarios_despues = Usuario.objects.count()
        error = peticion.context["form"].errors
        self.assertEqual(peticion.status_code, 200)
        self.assertEqual(usuarios_despues, usuarios_antes)
        self.assertIn("password2", error)

    def test_usuario_duplicado(self): # Test para la comprobacion del registro cuando ya existe ese usuario.
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

    def test_form_valido(self): # Test para la comprobacion del formulario cuando es valido y no hay errores.
        usuarios_antes = Usuario.objects.count()
        url = reverse("registro")
        datos = {"username": "angelote", "first_name": "Angel", "last_name": "Merino Lopez", "password1": "caracol04", "password2": "caracol04"}
        peticion = self.client.post(url, datos)
        usuarios_despues = Usuario.objects.count()
        usuario_existente = Usuario.objects.filter(username="angelote").exists()
        self.assertEqual(peticion.status_code, 302)
        self.assertEqual(usuarios_despues, usuarios_antes + 1)
        self.assertTrue(usuario_existente)

# Clase para la creacion de tests y apartado de "inicio de sesion".

class AppInicioSesion(TestCase):

    def test_form_incompleto_no_inicia_sesion(self): # Test para la comprobacion del formulario con los campos vacios.
        url = reverse("inicio_sesion")
        datos = {"username": "", "password": ""}
        peticion = self.client.post(url, datos)
        error = peticion.context["form"].errors
        sesion = self.client.session
        self.assertEqual(peticion.status_code, 200)
        self.assertNotIn("_auth_user_id", sesion)
        self.assertIn("username", error)
        self.assertIn("password", error)

    def test_form_completa_inicio_sesion(self): # Test para la comprobacion del formulario completo y valido.
        Usuario.objects.create_user(username="angelote", password="caracol04")
        url = reverse("inicio_sesion")
        datos = {"username": "angelote", "password": "caracol04"}
        peticion = self.client.post(url, datos)
        sesion = self.client.session
        self.assertEqual(peticion.status_code, 302)
        self.assertIn("_auth_user_id", sesion)

# Clase para la creacion de tests y apartado de "panel de admin".

class AppPanelAdmin(TestCase):

    def test_acceso_denegado_usuario(self): # Test de acceso con usuario sin ser administrador.
        usuario = Usuario.objects.create_user(username="angelote", password="caracol04")
        url = reverse("panel_admin")
        self.client.force_login(usuario)
        peticion = self.client.get(url)
        self.assertRedirects(peticion, reverse("home"))

    def test_acceso_permitido_admin(self): # Test de acceso con un usuario administrador.
        usuario = Usuario.objects.create_user(username="angelote", password="caracol04", rol= "admin")
        url = reverse("panel_admin")
        self.client.force_login(usuario)
        peticion = self.client.get(url)
        self.assertEqual(peticion.status_code, 200)

    def test_eliminacion_usuario(self): # Test para la comprobacion de eliminacion de usuarios siendo administrador.
        usuario = Usuario.objects.create_user(username="angelote", password="caracol04")
        admin = Usuario.objects.create_user(username="admin_01", password="ejemplo01", rol="admin")
        usuarios_antes = Usuario.objects.count()
        self.client.force_login(admin)
        url = reverse("eliminar_usuario", args=[usuario.id])
        peticion = self.client.post(url)
        usuarios_despues = Usuario.objects.count()
        self.assertRedirects(peticion, reverse("panel_admin"))
        self.assertEqual(usuarios_despues, usuarios_antes - 1)

    def test_acceso_denegado_para_eliminar_usuario(self): # Test para la comprobacion de eliminacion de usuarios siendo un usuario normal.
        usuario1 = Usuario.objects.create_user(username="angelote_1", password="caracol04")
        usuario2 = Usuario.objects.create_user(username="angelote_2", password="caracol04")
        usuarios_antes = Usuario.objects.count()
        self.client.force_login(usuario1)
        url = reverse("eliminar_usuario", args=[usuario2.id])
        peticion = self.client.post(url)
        usuarios_despues = Usuario.objects.count()
        self.assertRedirects(peticion, reverse("home"))
        self.assertEqual(usuarios_despues, usuarios_antes)
