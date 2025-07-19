from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Categoria(models.Model):
    nombre=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='categoria'
        verbose_name_plural='categorias'

    def __str__(self):
        return self.nombre

class Post(models.Model):
    titulo=models.CharField(max_length=50)
    contenido=models.CharField(max_length=1000)
    image=models.ImageField(upload_to='blog', null=True, blank=True)
    #Un autor puede crear varios post relacion de uno a varios
    #Si se va el autor se van sus post

    autor=models.ForeignKey(User, on_delete=models.CASCADE)
    #Una categoria puede estar en varios post y viseversa many to many
    categorias=models.ManyToManyField(Categoria)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='post'
        verbose_name_plural='posts'

    def __str__(self):
        return self.titulo