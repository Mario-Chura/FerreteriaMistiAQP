from django.shortcuts import render, HttpResponse
from carro.carro import Carro

from .models import Producto, Categoria

from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import *

def index(request):
    carro=Carro(request)
    return render(request, "ferreteriaOnlineApp/index.html")




