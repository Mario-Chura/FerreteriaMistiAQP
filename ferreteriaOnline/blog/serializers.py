from rest_framework import serializers
from .models import *


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("__all__")

    def create(self,validated_data):
        return Post.objects.create(**validated_data)

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ("__all__")

    def create(self,validated_data):
        return Categoria.objects.create(**validated_data)