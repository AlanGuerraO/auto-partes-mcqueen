from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, TemplateView

# Create your views here.

class HomeView(TemplateView):
    template_name = 'home.html'