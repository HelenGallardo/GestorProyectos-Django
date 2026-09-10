# Gestor de Proyectos y Tareas — Proyecto Módulo 6
Aplicación web desarrollada con Django para gestionar proyectos y tareas por usuario.

## Funcionalidades
- Registro de usuarios.
- Inicio y cierre de sesión.
- Cada usuario visualiza únicamente sus propios proyectos y tareas.
- Crear, listar, ver, editar y eliminar proyectos.
- Crear, editar y eliminar tareas asociadas a un proyecto.
- Formularios basados en `ModelForm`.
- Protección CSRF en formularios.
- Restricción de acceso con `LoginRequiredMixin`.
- Administración de Proyecto y Tarea desde Django Admin.
- Pruebas unitarias de modelos y vistas principales.
- Interfaz con Bootstrap y herencia de plantillas.

## Requisitos
- Python 3.10 o superior.
- Django 5.2.

## Instalación en Windows
1. Abrir una terminal en la carpeta del proyecto.

2. Crear el entorno virtual:
py -m venv venv

3. Activar el entorno virtual:
.\venv\Scripts\Activate.ps1

4. Instalar dependencias:
pip install -r requirements.txt

5. Crear y aplicar migraciones:
py manage.py makemigrations
py manage.py migrate

6. Crear un superusuario:
py manage.py createsuperuser

7. Ejecutar el servidor:
py manage.py runserver

8. Abrir en el navegador:
- Aplicación: http://127.0.0.1:8000/
- Login: http://127.0.0.1:8000/login/
- Registro: http://127.0.0.1:8000/registro/
- Administración: http://127.0.0.1:8000/admin/


## Pruebas unitarias
Ejecutar en terminal de VScode:
py manage.py test

## Estructura principal
gestor_proyectos_m6/
├── config/
├── proyectos/
│   ├── migrations/
│   ├── templates/
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── static/
├── templates/
├── .gitignore
├── db.sqlite3
├── manage.py
├── README.md
└── requirements.txt

## Modelos

Proyecto:
- nombre
- descripcion
- fecha_creacion
- usuario

Tarea:
- proyecto
- titulo
- descripcion
- fecha_limite
- completada
- fecha_creacion

La relación entre Proyecto y Tarea es uno a muchos: un Proyecto puede tener múltiples Tareas.
