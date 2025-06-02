from django.db import models

# Create your models here.

class Categorias(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='categorias/')

    def __str__(self):
        return self.nombre


class Marcas(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Productos(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='productos/')
    stock = models.PositiveIntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField()
    marca = models.ForeignKey(Marcas, on_delete=models.SET_NULL, null=True, blank=True)
    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE, related_name='productos')

    def __str__(self):
        return self.nombre