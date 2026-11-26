from django.test import TestCase
from home.models import Torneo
from inscripcion.models import Inscripcion
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Enfrentamiento
from urllib.parse import urlencode

# Metodo get_user_model para usar el usuario por defecto de django.

Usuario = get_user_model()

# Clase para la creacion de tests y apartado de "torneo".

class AppTorneo(TestCase):

    def setUp(self): # Metodo para generar un torneo y usuarios inscritos para usarlos en los tests.
        self.torneo = Torneo.objects.create(juego= "Rocket League")
        self.usuarios = []
        for i in range(1, 9):
            usuario = Usuario.objects.create_user(username=f"test0{i}", password=f"test0{i}")
            self.usuarios.append(usuario)
            Inscripcion.objects.create(usuario= usuario,juego= self.torneo, nivel= "MID")
        self.admin = Usuario.objects.create_user(username="admin", password="testadmin01", rol="admin")

    def test_pagina_bracket_torneo(self): # Test de comprobacion para el acceso al bracket del torneo.
        url = reverse("vista_torneo_rl")
        peticion = self.client.get(url)
        self.assertEqual(peticion.status_code, 200)
        self.assertTemplateUsed(peticion, "torneo/vista_torneo.html")

    def test_construccion_bracket_torneo(self): # Test de construccion de torneo siendo usuario administrador y comprobando el numero de enfrentamientos.
        self.client.force_login(self.admin)
        url = reverse("generador_torneo_rl")
        peticion = self.client.get(url)
        enfrentamientos_cuartos = Enfrentamiento.objects.filter(ronda = "CUARTOS").count()
        enfrentamientos_semis = Enfrentamiento.objects.filter(ronda = "SEMIFINALES").count()
        enfrentamientos_final = Enfrentamiento.objects.filter(ronda = "FINAL").count()
        self.assertRedirects(peticion, reverse("vista_torneo_rl"))
        self.assertEqual(enfrentamientos_cuartos, 4)
        self.assertEqual(enfrentamientos_semis, 2)
        self.assertEqual(enfrentamientos_final, 1)

    def test_construccion_torneo_fallido(self): # Test de construccion de torneo cuando no hay suficientes inscripciones.
        Inscripcion.objects.filter(usuario= self.usuarios[0]).delete()
        self.client.force_login(self.admin)
        url = reverse("generador_torneo_rl")
        peticion = self.client.get(url)
        enfrentamientos = Enfrentamiento.objects.count()
        self.assertEqual(enfrentamientos, 0)
        self.assertRedirects(peticion, reverse("home"))

    def test_construccion_sin_admin(self): # Test de construccion de torneo cuando no es un usuario administrador.
        usuario_ejemplo = Usuario.objects.create_user(username="angelote", first_name="Angel", last_name="Merino Lopez")
        self.client.force_login(usuario_ejemplo)
        url = reverse("generador_torneo_rl")
        peticion = self.client.get(url)
        self.assertRedirects(peticion, reverse("home"))

    def test_construccion_torneo_anonimo(self): # Test construccion de usuario sin ninguna cuenta iniciada.
        url = reverse("generador_torneo_rl")
        url_login = reverse("inicio_sesion")
        url_esperada = f"{url_login}?{urlencode({"next": url})}"
        peticion = self.client.get(url)
        enfrentamientos = Enfrentamiento.objects.count()
        self.assertEqual(enfrentamientos, 0)
        self.assertRedirects(peticion, url_esperada)
    