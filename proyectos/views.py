from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)
from .forms import ProyectoForm, RegistroForm, TareaForm
from .models import Proyecto, Tarea


class RegistroView(CreateView):
    model = User
    form_class = RegistroForm
    template_name = "registration/registro.html"
    success_url = reverse_lazy("proyectos:lista")

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response


class ProyectoListView(LoginRequiredMixin, ListView):
    model = Proyecto
    template_name = "proyectos/proyecto_list.html"
    context_object_name = "proyectos"

    def get_queryset(self):
        return Proyecto.objects.filter(usuario=self.request.user)


class ProyectoDetailView(LoginRequiredMixin, DetailView):
    model = Proyecto
    template_name = "proyectos/proyecto_detail.html"
    context_object_name = "proyecto"

    def get_queryset(self):
        return Proyecto.objects.filter(usuario=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tarea_form"] = TareaForm()
        return context


class ProyectoCreateView(LoginRequiredMixin, CreateView):
    model = Proyecto
    form_class = ProyectoForm
    template_name = "proyectos/proyecto_form.html"

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("proyectos:detalle", kwargs={"pk": self.object.pk})


class ProyectoUpdateView(LoginRequiredMixin, UpdateView):
    model = Proyecto
    form_class = ProyectoForm
    template_name = "proyectos/proyecto_form.html"

    def get_queryset(self):
        return Proyecto.objects.filter(usuario=self.request.user)

    def get_success_url(self):
        return reverse("proyectos:detalle", kwargs={"pk": self.object.pk})


class ProyectoDeleteView(LoginRequiredMixin, DeleteView):
    model = Proyecto
    template_name = "proyectos/proyecto_confirm_delete.html"
    success_url = reverse_lazy("proyectos:lista")

    def get_queryset(self):
        return Proyecto.objects.filter(usuario=self.request.user)


class TareaCreateView(LoginRequiredMixin, CreateView):
    model = Tarea
    form_class = TareaForm

    def dispatch(self, request, *args, **kwargs):
        self.proyecto = Proyecto.objects.filter(
            pk=kwargs["proyecto_pk"],
            usuario=request.user
        ).first()
        if self.proyecto is None:
            from django.http import Http404
            raise Http404("Proyecto no encontrado")
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.proyecto = self.proyecto
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("proyectos:detalle", kwargs={"pk": self.proyecto.pk})


class TareaUpdateView(LoginRequiredMixin, UpdateView):
    model = Tarea
    form_class = TareaForm
    template_name = "proyectos/tarea_form.html"

    def get_queryset(self):
        return Tarea.objects.filter(proyecto__usuario=self.request.user)

    def get_success_url(self):
        return reverse("proyectos:detalle", kwargs={"pk": self.object.proyecto.pk})


class TareaDeleteView(LoginRequiredMixin, DeleteView):
    model = Tarea
    template_name = "proyectos/tarea_confirm_delete.html"

    def get_queryset(self):
        return Tarea.objects.filter(proyecto__usuario=self.request.user)

    def get_success_url(self):
        return reverse("proyectos:detalle", kwargs={"pk": self.object.proyecto.pk})
