from dataclasses import field
from rest_framework import serializers
from .models import *


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ("__all__")

    def create(self,validated_data):
        return Producto.objects.create(**validated_data)

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ("__all__")

    def create(self,validated_data):
        return Categoria.objects.create(**validated_data)