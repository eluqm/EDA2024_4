from django.contrib import admin
from django.urls import path
from app_episound import views
from .views import *

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('mostrarCancion', views.mostrar_cancion , name="index"),
    path('miMusica', views.miMusica, name="miMusica"),
    path('buscador', views.buscar, name="buscar"),
    path('reproduccion', views.reproducir, name="reproducir"),
    path('guardar-id/', views.guardar_id, name='guardar_id'),
    path('eliminar_id/', views.eliminar_id, name='eliminar_id'),
    path('next_song/', views.next_song, name='next_song'),
    path('prev_song/', views.prev_song, name='prev_song'),
]
