"""
Configuración de URLs para la aplicación de inventario.

Este módulo define todas las rutas URL disponibles en la aplicación de inventario,
incluyendo las vistas para gestionar categorías, productos y marcas.
"""

from django.urls import path
from . import views

urlpatterns = [
    # URLs de inicio
    path('', views.HomeView.as_view(), name='home'),
] 