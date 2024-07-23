
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .in_memory_data import canciones, current_song, datos
from .EstructurasDeDatos.HashMap import HashMap
from .EstructurasDeDatos.LinkedList import LinkedList
from .EstructurasDeDatos.Queue import Queue
from .EstructurasDeDatos.Trie import Trie

misCanciones = LinkedList()
colaReproducción = Queue()
global_canciones = datos()

trieArbol = Trie()
for cancion in canciones:
    trieArbol.insert(cancion.get_track_name(), cancion) 

def index(request):
    return render(request, "inicio/page.html") 

def miMusica(request):
    context = {
        'canciones': misCanciones
    }
    return render(request, "miMusica/page.html", context)

def buscar(request):
    query = request.GET.get('query', '')  
    if query:
        resultados = trieArbol.searchAll(query)
        print(resultados.size)
    else:
        resultados = []
    context = {
        'canciones': resultados 
    }
    return render(request, "buscador/page.html", context)

def mostrar_cancion(request):
    context = {
        'canciones': global_canciones
    }
    return render(request, "inicio/page.html", context)

def reproducir(request):
    context = {
        'canciones': colaReproducción,
        'current_song': colaReproducción.peek()  # Mostrar la canción actual
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
            if not misCanciones.contains(cancion_select):
                misCanciones.add(cancion_select)
                colaReproducción.enqueue(cancion_select)
                print(f"ID de la canción recibida: {cancion_id}")
                print(f"Detalles de la canción seleccionada: {cancion_select}")
            else:
                print("La canción ya está en la lista.")
                
        except ValueError as e:
            print(f"Error: {e}")

    return redirect('index')

def next_song(request):
    nextSong = colaReproducción.next_song()  # Obtiene la siguiente canción
    context = {
        'canciones': colaReproducción,
        'current_song': nextSong
    }
    return render(request, "reproduccion/page.html", context)

def prev_song(request):
    prev_song = colaReproducción.prev_song()
    # Necesitarás implementar lógica para la canción anterior si usas una cola circular o similar
    context = {
        'canciones': colaReproducción,
        'current_song': prev_song  # Aquí deberías definir cómo obtener la canción anterior
    }
    return render(request, "reproduccion/page.html", context)