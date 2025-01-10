from django.urls import path
from .views import vista_prueba, vista_autor, MiVistaView, layout



urlpatterns = [ # todas estas urls llevan /urls_first_app/ al inicio
    path('listado/', vista_prueba),
    path('detalle/<int:id>', vista_prueba),
    path('marcas/<str:marca>', vista_prueba),
    path('autor/<int:id>', vista_autor),
    path('app_url_lista_carros/', MiVistaView.as_view()),
    path('layout/', layout),
]