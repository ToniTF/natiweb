from django.urls import path
from .views import home_view, ProyectoListView, ProyectoDetailView, ProyectoCreateView, ProyectoUpdateView, ProyectoDeleteView, contacto_view

app_name = 'principal'  # Define el namespace aquí

urlpatterns = [
    path('', home_view, name='home'),  # Ruta asociada a la vista 'home_view'
    path('proyectos/', ProyectoListView.as_view(), name='proyecto-lista'),
    path('proyectos/<int:pk>/', ProyectoDetailView.as_view(), name='proyecto-detalle'),
    path('proyectos/nuevo/', ProyectoCreateView.as_view(), name='proyecto-nuevo'),
    path('proyectos/editar/<int:pk>/', ProyectoUpdateView.as_view(), name='proyecto-editar'),
    path('proyectos/eliminar/<int:pk>/', ProyectoDeleteView.as_view(), name='proyecto-eliminar'),
    path('contacto/', contacto_view, name='contacto'),
]

