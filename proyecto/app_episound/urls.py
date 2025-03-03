from django.contrib import admin
from django.urls import path
from app_episound import views
from .views import *


urlpatterns = [
    path('', views.mostrar_cancion, name="index"),
    path('miMusica', views.miMusica, name="miMusica"),
    path('buscador', views.buscar, name="buscar"),
    path('reproduccion', views.reproducir, name="reproducir"),
    path('guardar-id/', views.guardar_id, name='guardar_id'),
    path('guardar-id-Busc/', views.guardar_idBusc, name="guardar_idBusc"),
    path('eliminar_id/', views.eliminar_id, name='eliminar_id'),
    path('next_song/', views.next_song, name='next_song'),
    path('prev_song/', views.prev_song, name='prev_song'),
    path('play_btn/', views.play_song, name='play_song'),
    path('miMusica/TiempodeDuracion/', views.TimeDurationBtree, name="songs_duration"),
    path('miMusica/TiempodeDuracion/songs_ascending_Btree/', views.songs_ascend_btree , name='songs_ascending_Btree'),
    path('miMusica/TiempodeDuracion/songs_descending_Btree/', views.songs_descend_btree , name='songs_descending_Btree'),
    path('miMusica/Año/', views.TimeDurationAvl, name="songs_año"),
    path('miMusica/Año/songs_ascend_avlAños/', views.songs_ascend_avlAños, name='songs_ascending_AvlAños'),
    path('miMusica/Año/songs_descending_avlAños/', views.songs_descend_avlAños, name='songs_descending_AvlAños'),
    path('miMusica/Popularidad/', views.TimePopularidadAvl, name="songs_popularidad"),
    path('miMusica/Popularidad/songs_ascend_avlPopularidad/', views.songs_ascend_avlPopularidad, name="songs_ascending_AvlPopularidad"),
    path('miMusica/Popularidad/songs_descending_avlPopularidad/', views.songs_descend_avlPopularidad, name="songs_descending_AvlPopularidad"),
    
    path('cambiarPosicion/', cambiarPosicion, name='cambiarPosicion'),
    path('random/', views.random, name='random'),

    # Add more paths as needed
]