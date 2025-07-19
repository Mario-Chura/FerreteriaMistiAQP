from django.urls import path
from ferreteriaOnlineApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('', views.index, name="Index")
    
]

#Para que nos deje mostrar las imagenes
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
