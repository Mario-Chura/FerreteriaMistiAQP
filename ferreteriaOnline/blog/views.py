from django.shortcuts import render
from blog.models import Post, Categoria


from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import *
# Create your views here.

def blog(request):
    posts=Post.objects.all()
    return render(request, "blog/blog.html",{"posts": posts})

def categoria(request, categoria_id):
    categoria=Categoria.objects.get(id=categoria_id)
    posts=Post.objects.filter(categorias=categoria)
    return render(request,"blog/categoria.html", {'categoria': categoria, "posts": posts})

class PostView(APIView):
    
    def get(self,request):
        dataPost = Post.objects.all()
        serPost = PostSerializer(dataPost,many=True)
        return Response(serPost.data)
    
    def post(self,request):
        serPost = PostSerializer(data=request.data)
        serPost.is_valid(raise_exception=True)
        serPost.save()
        
        return Response(serPost.data)
    
class PostDetailView(APIView):
    
    def get(self,request,blog_id):
        dataPost = Post.objects.get(pk=blog_id)
        serPost = PostSerializer(dataPost)
        return Response(serPost.data)
    
    def put(self,request,blog_id):
        dataPost = Post.objects.get(pk=blog_id)
        serPost = PostSerializer(dataPost,data=request.data)
        serPost.is_valid(raise_exception=True)
        serPost.save()
        return Response(serPost.data)
    
    def delete(self,request,blog_id):
        dataPost = Post.objects.get(pk=blog_id)
        serPost = PostSerializer(dataPost)
        dataPost.delete()
        return Response(serPost.data)


class CategoriaView(APIView):
    
    def get(self,request):
        dataCategoria = Categoria.objects.all()
        serCategoria = CategoriaSerializer(dataCategoria,many=True)
        return Response(serCategoria.data)
    
    def post(self,request):
        serCategoria = CategoriaSerializer(data=request.data)
        serCategoria.is_valid(raise_exception=True)
        serCategoria.save()
        
        return Response(serCategoria.data)
    
class CategoriaDetailView(APIView):
    
    def get(self,request,categoria_id):
        dataCategoria = Categoria.objects.get(pk=categoria_id)
        serCategoria = CategoriaSerializer(dataCategoria)
        return Response(serCategoria.data)
    
    def put(self,request,categoria_id):
        dataCategoria = Categoria.objects.get(pk=categoria_id)
        serCategoria = CategoriaSerializer(dataCategoria,data=request.data)
        serCategoria.is_valid(raise_exception=True)
        serCategoria.save()
        return Response(serCategoria.data)
    
    def delete(self,request,categoria_id):
        dataCategoria = Categoria.objects.get(pk=categoria_id)
        serCategoria = CategoriaSerializer(dataCategoria)
        dataCategoria.delete()
        return Response(serCategoria.data)