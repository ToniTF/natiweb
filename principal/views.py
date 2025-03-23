from django.shortcuts import render
from .forms import ProyectoForm
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Proyecto

def home_view(request):
    # Lógica de la vista
    return render(request, 'home.html')

def contacto_view(request):
    # Lógica para la vista de contacto
    return render(request, 'contacto.html')

class ProyectoListView(ListView):
    model = Proyecto
    template_name = 'proyecto_list.html'

class ProyectoDetailView(DetailView):
    model = Proyecto
    template_name = 'proyecto_detail.html'

class ProyectoCreateView(CreateView):
    model = Proyecto
    template_name = 'proyecto_form.html'
    fields = ['nombre', 'descripcion', 'tecnologias', 'imagen', 'enlace']

class ProyectoUpdateView(UpdateView):
    model = Proyecto
    template_name = 'proyecto_form.html'
    fields = ['nombre', 'descripcion', 'tecnologias', 'imagen', 'enlace']

class ProyectoDeleteView(DeleteView):
    model = Proyecto
    template_name = 'proyecto_confirm_delete.html'
    success_url = reverse_lazy('principal:proyecto-lista')  # Asegúrate de que tiene el namespace
