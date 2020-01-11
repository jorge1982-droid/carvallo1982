from django.urls import path
from .views import *

urlpatterns = [
    path('',home, name = 'index'),
    path('generales/',generales, name = 'generales'),
    path('programacion/',programacion, name = 'programacion'),
    path('tecnologia/',tecnologia, name = 'tecnologia'),
    path('tutoriales/',tutoriales, name = 'tutoriales'),
    path('videojuegos/',videojuegos, name = 'videojuegos'),
    path('inicio/',inicio),
    path('<slug:slug>',detallePost, name='detalle_Post'),  # para pasar parametros ala url siempre va al final
]
