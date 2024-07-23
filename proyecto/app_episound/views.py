import sys
sys.path.append("../")
from django.shortcuts import render
from django.http import HttpResponse
from .in_memory_data import canciones, current_song , next_song , datos
from EstructurasDeDatos.HashMap import HashMap


misCanciones = HashMap()
global_canciones = datos()

def index(request):
  return render(request, "inicio/page.html") 

def miMusica(request):
  return render(request, "miMusica/page.html")

def buscar(request):
  return render(request, "buscador/page.html")

def mostrar_cancion(request):
    context = {
        'canciones': global_canciones
    }
    return render(request, "inicio/page.html", context)

def reproducir(request):
    context = {
        'canciones': global_canciones,
        'current_song': current_song,
        'next_song': next_song
    }
    return render(request, "reproduccion/page.html", context)

def inicio(request):
  return render(request, "inicio.html")






################ FUNCIONES PARA LA BUSQUEDA ################
from .EstructurasDeDatos.Trie import Trie
trieArbol = Trie()
for cancion in global_canciones:
    trieArbol.insert(cancion.get_track_name(), cancion) 

def buscar(request):
    query = request.GET.get('query', '')      
    if query:
        resultados = trieArbol.searchAll(query)
        print(f"Search results: {resultados}") 
    else:
        resultados = []
    context = {
        'canciones': resultados  
    }
    return render(request, "buscador/page.html", context)