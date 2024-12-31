from django.shortcuts import render

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