from django.contrib import admin
from .models import Proyecto, Tarea


@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "usuario", "fecha_creacion")
    search_fields = ("nombre", "descripcion", "usuario__username")
    list_filter = ("fecha_creacion", "usuario")


@admin.register(Tarea)
class TareaAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "titulo",
        "proyecto",
        "fecha_limite",
        "completada",
        "fecha_creacion",
    )
    search_fields = ("titulo", "descripcion", "proyecto__nombre")
    list_filter = ("completada", "fecha_limite", "fecha_creacion")
