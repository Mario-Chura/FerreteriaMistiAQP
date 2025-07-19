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
        model = CategoriaProd
        fields = ('id','nombre','created')

    def create(self,validated_data):
        return CategoriaProd.objects.create(**validated_data)
