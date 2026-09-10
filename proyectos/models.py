from django.db import models
from django.contrib.auth.models import User

class Proyecto(models.Model):
    nombre = models.CharField(max_length=120)
    descripcion = models.TextField(blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="proyectos"
    )

    class Meta:
        ordering = ["-fecha_creacion"]

    def __str__(self):
        return self.nombre


class Tarea(models.Model):
    proyecto = models.ForeignKey(
        Proyecto,
        on_delete=models.CASCADE,
        related_name="tareas"
    )
    titulo = models.CharField(max_length=120)
    descripcion = models.TextField(blank=True)
    fecha_limite = models.DateField(blank=True, null=True)
    completada = models.BooleanField(default=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["completada", "fecha_limite", "-fecha_creacion"]

    def __str__(self):
        return self.titulo
