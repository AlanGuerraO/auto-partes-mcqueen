from django.db import models

# Create your models here.

class Categorias(models.Model):
    """
    Modelo que representa las categorías de productos en la tienda.
    
    Este modelo almacena las diferentes categorías bajo las cuales se pueden
    clasificar los productos, como 'Llantas', 'Lubricantes', etc.
    
    Atributos:
        nombre (str): Nombre de la categoría
        imagen (ImageField): Imagen representativa de la categoría (opcional)
    """
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='categorias/', null=True, blank=True)

    def __str__(self):
        return self.nombre


class Marcas(models.Model):
    """
    Modelo que representa las marcas de productos disponibles.
    
    Almacena información sobre los fabricantes o marcas de los productos,
    permitiendo organizar los productos por fabricante.
    
    Atributos:
        nombre (str): Nombre de la marca
        logo (ImageField): Logo de la marca (opcional)
        sitio_web (URLField): Sitio web oficial de la marca (opcional)
    """
    nombre = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='marcas/', null=True, blank=True)
    sitio_web = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.nombre


class Productos(models.Model):
    """
    Modelo principal que representa los productos disponibles en la tienda.
    
    Este modelo almacena toda la información relacionada con los productos
    que se venden en la tienda, incluyendo sus detalles, precios y relaciones
    con categorías y marcas.
    
    Atributos:
        nombre (str): Nombre del producto
        descripcion (text): Descripción detallada del producto
        precio (decimal): Precio del producto con dos decimales
        stock (int): Cantidad disponible del producto
        marca (ForeignKey): Relación con el modelo Marcas (opcional)
        categoria (ForeignKey): Relación con el modelo Categorias (opcional)
        imagen (ImageField): Imagen del producto (opcional)
    """
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    marca = models.ForeignKey(Marcas, on_delete=models.SET_NULL, null=True, blank=True, related_name='productos')
    categoria = models.ForeignKey(Categorias, on_delete=models.SET_NULL, null=True, blank=True, related_name='productos')
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)

    def __str__(self):
        return self.nombre