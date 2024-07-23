from django.shortcuts import render, redirect
from django.http import HttpResponse
from .in_memory_data import canciones, current_song , next_song , datos
from EstructurasDeDatos.HashMap import HashMap
from EstructurasDeDatos.LinkedList import LinkedList
# Create your views here.

misCanciones = HashMap()
testeo = LinkedList()

global_canciones = datos()

def index(request):
  return render(request, "inicio/page.html") 

def miMusica(request):
  context = {
    'canciones': testeo
  }
  return render(request, "miMusica/page.html", context)

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

def guardar_id(request):
    if request.method == 'POST':
        cancion_id = request.POST.get('cancion_id')
        try:
            cancion_id = int(cancion_id)
            cancion_select = global_canciones.get(cancion_id)
            testeo.add(cancion_select)
            print(f"ID de la canción recibida: {cancion_id}")
            print(f"Detalles de la canción seleccionada: {cancion_select}")
        except ValueError as e:
            print(f"Error: {e}")

    return redirect('index')











################ FUNCIONES PARA LA BUSQUEDA ################
# Inicializa el Trie e inserta las canciones
'''import sys
sys.path.append("../")
from leer_csv import leer_csv
from .EstructurasDeDatos.Trie import Trie

canciones = leer_csv("../archive/spotify_data.csv", 1000)
trieArbol = Trie()
print(f"Total de canciones leídas: {len(canciones)}")

for cancion in canciones:
    trieArbol.insert(cancion.get_track_name(), cancion) 


def buscar(request):
    query = request.GET.get('query', '')  # Captura el valor de búsqueda
    print(f"Search query received: {query}")  # Imprime la consulta en la consola
    
    if query:
        # Busca todas las canciones que comienzan con el prefijo dado en el Trie
        resultados = trieArbol.searchAll(query)
        print(resultados.size);
        #print(resultados.get(0));
        print(f"Search results: {resultados}")  # Imprime los resultados en la consola
    else:
        resultados = []

    context = {
        'canciones': resultados  # Pasa los resultados como una lista de canciones al contexto
    }
    return render(request, "buscador/page.html", context)'''