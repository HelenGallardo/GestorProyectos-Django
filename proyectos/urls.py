from django.urls import path
from .views import (
    ProyectoCreateView,
    ProyectoDeleteView,
    ProyectoDetailView,
    ProyectoListView,
    ProyectoUpdateView,
    TareaCreateView,
    TareaDeleteView,
    TareaUpdateView,
)

app_name = "proyectos"

urlpatterns = [
    path("", ProyectoListView.as_view(), name="lista"),
    path("proyectos/", ProyectoListView.as_view(), name="lista_alt"),
    path("proyectos/nuevo/", ProyectoCreateView.as_view(), name="nuevo"),
    path("proyectos/<int:pk>/", ProyectoDetailView.as_view(), name="detalle"),
    path("proyectos/<int:pk>/editar/", ProyectoUpdateView.as_view(), name="editar"),
    path("proyectos/<int:pk>/eliminar/", ProyectoDeleteView.as_view(), name="eliminar"),
    path(
        "proyectos/<int:proyecto_pk>/tareas/nueva/",
        TareaCreateView.as_view(),
        name="tarea_nueva",
    ),
    path("tareas/<int:pk>/editar/", TareaUpdateView.as_view(), name="tarea_editar"),
    path("tareas/<int:pk>/eliminar/", TareaDeleteView.as_view(), name="tarea_eliminar"),
]
