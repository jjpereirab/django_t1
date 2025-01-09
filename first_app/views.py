from django.views.generic import TemplateView
from django.shortcuts import render
from .models import Autor, Perfil
from django.http import HttpResponse

# Create your views here.
def mi_vista(request):
    lista = [
        {"title": "BMW"},
        {"title": "Audi"},
    ]
    contexto = {
        "context_lista": lista
    }
    return render(request, 'first_app/template_lista_carros.html', contexto)

class MiVistaView(TemplateView):
    template_name = 'first_app/template_lista_carros.html'  # <-------------------- SE TIENE QUE LLAMAR "template_name"

    def get_context_data(self):
        lista = [
            {"title": "BMW"},
            {"title": "Audi"},
        ]
        contexto = {
            "context_lista": lista
        }
        return contexto

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