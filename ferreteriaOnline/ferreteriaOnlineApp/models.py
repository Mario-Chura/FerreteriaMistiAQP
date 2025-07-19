from django.db import models

# Create your models here.


class Categoria(models.Model):
    nombre = models.CharField(max_length=200)
    fecha_publicacion = models.DateField('fecha de publicacion')
    
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    marca = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.IntegerField(default=0)
    reservado = models.BooleanField(default=False)
    descontable = models.BooleanField(default=False)
    fecha_publicacion = models.DateTimeField('fecha de publicacion')
    imagen = models.ImageField(upload_to='productos',blank=True,null=True)
    
    def __str__(self):
        return self.nombre
    