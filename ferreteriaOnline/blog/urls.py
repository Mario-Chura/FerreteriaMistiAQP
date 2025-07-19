from django.urls import path
from .import views

urlpatterns = [

    path('',views.blog, name="Blog"),
    path('categoria/<int:categoria_id>/', views.categoria, name="categoria" ),

    path('blogapi',views.PostView.as_view(),name='blogapi'),
    path('blogapi/<int:blog_id>',views.PostDetailView.as_view()),
    path('categoriaapi',views.CategoriaView.as_view(),name='categoriaapi'),
    path('categoriaapi/<int:categoria_id>',views.CategoriaDetailView.as_view())

    
]