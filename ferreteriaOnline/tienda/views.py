from django.shortcuts import render
from .models import Producto, CategoriaProd
# Create your views here.


from .serializers import *

from rest_framework.views import APIView
from rest_framework.response import Response

def tienda(request):
    productos=Producto.objects.all()
    return render(request, "tienda/tienda.html", {"productos": productos})

class ProductoView(APIView):
    
    def get(self,request):
        dataProducto = Producto.objects.all()
        serProducto = ProductoSerializer(dataProducto,many=True)
        return Response(serProducto.data)
    
    def post(self,request):
        serProducto = ProductoSerializer(data=request.data)
        serProducto.is_valid(raise_exception=True)
        serProducto.save()
        
        return Response(serProducto.data)
    
class ProductoDetailView(APIView):
    
    def get(self,request,producto_id):
        dataProducto = Producto.objects.get(pk=producto_id)
        serProducto = ProductoSerializer(dataProducto)
        return Response(serProducto.data)
    
    def put(self,request,producto_id):
        dataProducto = Producto.objects.get(pk=producto_id)
        serProducto = ProductoSerializer(dataProducto,data=request.data)
        serProducto.is_valid(raise_exception=True)
        serProducto.save()
        return Response(serProducto.data)
    
    def delete(self,request,producto_id):
        dataProducto = Producto.objects.get(pk=producto_id)
        serProducto = ProductoSerializer(dataProducto)
        dataProducto.delete()
        return Response(serProducto.data)

class CategoriaView(APIView):
    
    def get(self,request):
        dataCategoria = CategoriaProd.objects.all()
        serCategoria = CategoriaSerializer(dataCategoria,many=True)
        return Response(serCategoria.data)
    
    def post(self,request):
        serCategoria = CategoriaSerializer(data=request.data)
        serCategoria.is_valid(raise_exception=True)
        serCategoria.save()
        
        return Response(serCategoria.data)
    
class CategoriaDetailView(APIView):
    
    def get(self,request,categoria_id):
        dataCategoria = CategoriaProd.objects.get(pk=categoria_id)
        serCategoria = CategoriaSerializer(dataCategoria)
        return Response(serCategoria.data)
    
    def put(self,request,categoria_id):
        dataCategoria = CategoriaProd.objects.get(pk=categoria_id)
        serCategoria = CategoriaSerializer(dataCategoria,data=request.data)
        serCategoria.is_valid(raise_exception=True)
        serCategoria.save()
        return Response(serCategoria.data)
    
    def delete(self,request,categoria_id):
        dataCategoria = CategoriaProd.objects.get(pk=categoria_id)
        serCategoria = CategoriaSerializer(dataCategoria)
        dataCategoria.delete()
        return Response(serCategoria.data)

