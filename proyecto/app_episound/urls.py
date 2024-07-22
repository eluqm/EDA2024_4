from django.contrib import admin
from django.urls import path
from app_episound import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('mostrarCancion', views.mostrar_cancion , name="index"),
    path('miMusica', views.miMusica, name="miMusica"),
    path('buscador', views.buscar, name="buscar"),
    path('reproduccion', views.reproducir, name="reproducir")
]
