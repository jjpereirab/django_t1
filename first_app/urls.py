from django.http import HttpResponse
from django.urls import path
from .models import Autor, Perfil

def vista_prueba(request, *args, **kwargs):
    print(args)
    print(kwargs)
    return HttpResponse("")

def vista_autor(request, *args, **kwargs):
    print(args)
    print(kwargs)
    author = Autor.objects.get(id=kwargs['id'])
    profile = Perfil.objects.get(autor_id=kwargs['id'])
    return HttpResponse(f"Autor: {author.nombre} - Website: {profile.website} - Biografia: {profile.biografia} ")

urlpatterns = [
    path('listado/', vista_prueba),
    path('detalle/<int:id>', vista_prueba),
    path('marcas/<str:marca>', vista_prueba),
    path('autor/<int:id>', vista_autor),
]