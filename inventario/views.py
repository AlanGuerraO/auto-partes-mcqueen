from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, TemplateView
from .models import Categorias, Productos, Marcas
from django.urls import reverse_lazy, reverse

# Create your views here.

class HomeView(TemplateView):
    template_name = 'home.html'

class CategoriaListView(ListView):
    model = Categorias
    template_name = 'categorias/categoria_list.html'
    context_object_name = 'object_list'

class CategoriaDetailView(DetailView):
    model = Categorias
    template_name = 'categorias/categoria_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['productos'] = self.object.productos.all()
        return context

class CategoriaCreateView(CreateView):
    model = Categorias
    template_name = 'categorias/categoria_form.html'
    fields = '__all__'
    success_url = reverse_lazy('categoria-list')

class CategoriaUpdateView(UpdateView):
    model = Categorias
    template_name = 'categorias/categoria_form.html'
    fields = '__all__'
    success_url = reverse_lazy('categoria-list')

class CategoriaDeleteView(DeleteView):
    model = Categorias
    template_name = 'categorias/categoria_confirm_delete.html'
    success_url = reverse_lazy('categoria-list')