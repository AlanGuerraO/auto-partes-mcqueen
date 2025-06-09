from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, TemplateView
from .models import Categorias, Productos, Marcas

# Create your views here.

class HomeView(TemplateView):
    template_name = 'home.html'

class CategoriaListView(ListView):
    model = Categorias
    template_name = 'categorias/categoria_list.html'
    context_object_name = 'object_list'