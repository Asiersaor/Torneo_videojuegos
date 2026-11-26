from django.test import TestCase
from .models import Torneo
from django.urls import reverse

# Clase para la creacion de tests y apartado de "home".

class AppHome(TestCase):

    def setUp(self): # Metodo para agregar un Torneo como ejemplo para los tests.
        self.torneo = Torneo.objects.create(juego= "Rocket League")

    def test_pagina_inicio(self):  # Test de comprobacion de la carga de vista del torneo.
        url = reverse("torneo_rl")
        peticion = self.client.get(url)
        self.assertEqual(peticion.status_code, 200)
        self.assertTemplateUsed(peticion, "home/inicio.html")

    def test_listado_juegos(self): # Test de comprobacion del listado completo de juegos.
        url = reverse("home")
        peticion = self.client.get(url)
        listado = peticion.context["torneos"]
        self.assertEqual(peticion.status_code, 200)
        self.assertContains(peticion, "Rocket League")
        self.assertIn(self.torneo, listado)

    def test_listado_vacio(self): # Test de comprobacion de listado vacio.
        self.torneo.delete()
        url = reverse("home")
        peticion = self.client.get(url)
        listado = peticion.context["torneos"]
        self.assertEqual(len(listado), 0)
        self.assertNotContains(peticion, "Rocket League")

        