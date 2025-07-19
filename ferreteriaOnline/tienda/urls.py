from django.urls import path

from .import views


urlpatterns = [
    
    path('',views.tienda, name="Tienda"),

    path('productoapi',views.ProductoView.as_view(),name='productoapi'),
    path('productoapi/<int:producto_id>',views.ProductoDetailView.as_view()),
    path('categoriaapi',views.CategoriaView.as_view(),name='categoriaapi'),
    path('categoriaapi/<int:categoria_id>',views.CategoriaDetailView.as_view())
    
]


