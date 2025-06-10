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
    
    # URLs de Categorías
    path('categorias/', views.CategoriaListView.as_view(), name='categoria-list'),
    path('categoria/<int:pk>/', views.CategoriaDetailView.as_view(), name='categoria-detail'),
    path('categoria/crear/', views.CategoriaCreateView.as_view(), name='categoria-create'),
    path('categoria/<int:pk>/editar/', views.CategoriaUpdateView.as_view(), name='categoria-update'),
    path('categoria/<int:pk>/eliminar/', views.CategoriaDeleteView.as_view(), name='categoria-delete'),
    
    # URLs de Productos
    path('productos/', views.ProductoListView.as_view(), name='producto-list'),
    path('producto/<int:pk>/', views.ProductoDetailView.as_view(), name='producto-detail'),
    path('producto/crear/', views.ProductoCreateView.as_view(), name='producto-create'),
    path('producto/<int:pk>/editar/', views.ProductoUpdateView.as_view(), name='producto-update'),
    path('producto/<int:pk>/eliminar/', views.ProductoDeleteView.as_view(), name='producto-delete'),
] 