from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from .models import Proyecto, Tarea


class ProyectoModelTest(TestCase):
    def setUp(self):
        self.usuario = User.objects.create_user(
            username="helen",
            password="clave-segura-123"
        )
        self.proyecto = Proyecto.objects.create(
            nombre="Proyecto de prueba",
            descripcion="Descripción",
            usuario=self.usuario,
        )

    def test_str_proyecto(self):
        self.assertEqual(str(self.proyecto), "Proyecto de prueba")

    def test_relacion_usuario_proyecto(self):
        self.assertEqual(self.proyecto.usuario, self.usuario)


class TareaModelTest(TestCase):
    def setUp(self):
        usuario = User.objects.create_user(
            username="usuario",
            password="clave-segura-123"
        )
        proyecto = Proyecto.objects.create(
            nombre="Proyecto",
            usuario=usuario
        )
        self.tarea = Tarea.objects.create(
            proyecto=proyecto,
            titulo="Tarea de prueba"
        )

    def test_str_tarea(self):
        self.assertEqual(str(self.tarea), "Tarea de prueba")

    def test_relacion_proyecto_tarea(self):
        self.assertEqual(self.tarea.proyecto.nombre, "Proyecto")


class ProyectoViewsTest(TestCase):
    def setUp(self):
        self.usuario = User.objects.create_user(
            username="helen",
            password="clave-segura-123"
        )
        self.otro_usuario = User.objects.create_user(
            username="otro",
            password="clave-segura-123"
        )
        self.proyecto = Proyecto.objects.create(
            nombre="Mi proyecto",
            usuario=self.usuario
        )
        self.proyecto_ajeno = Proyecto.objects.create(
            nombre="Proyecto ajeno",
            usuario=self.otro_usuario
        )

    def test_lista_requiere_login(self):
        respuesta = self.client.get(reverse("proyectos:lista"))
        self.assertEqual(respuesta.status_code, 302)

    def test_usuario_autenticado_ve_sus_proyectos(self):
        self.client.login(username="helen", password="clave-segura-123")
        respuesta = self.client.get(reverse("proyectos:lista"))
        self.assertContains(respuesta, "Mi proyecto")
        self.assertNotContains(respuesta, "Proyecto ajeno")

    def test_crear_proyecto(self):
        self.client.login(username="helen", password="clave-segura-123")
        respuesta = self.client.post(
            reverse("proyectos:nuevo"),
            {"nombre": "Nuevo proyecto", "descripcion": "Prueba"},
        )
        self.assertEqual(respuesta.status_code, 302)
        self.assertTrue(
            Proyecto.objects.filter(
                nombre="Nuevo proyecto",
                usuario=self.usuario
            ).exists()
        )
