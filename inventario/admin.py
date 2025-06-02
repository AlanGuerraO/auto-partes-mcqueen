from django.contrib import admin
from .models import Categorias, Marcas, Productos

# Register your models here.

admin.site.register(Categorias)
admin.site.register(Marcas)
admin.site.register(Productos)