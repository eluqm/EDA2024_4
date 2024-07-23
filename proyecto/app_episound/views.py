from django.shortcuts import render, redirect
from django.http import HttpResponse
from .in_memory_data import canciones, current_song , datos
from .EstructurasDeDatos.HashMap import HashMap
from .EstructurasDeDatos.LinkedList import LinkedList
from .EstructurasDeDatos.Queue import Queue
from .EstructurasDeDatos.Trie import Trie

misCanciones = LinkedList()
colaReproducción = Queue()
global_canciones = datos()

def index(request):
  return render(request, "inicio/page.html") 

def miMusica(request):
  context = {
    'canciones': misCanciones
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
    for cancion in misCanciones:
       colaReproducción.enqueue(cancion)
       
    context = {
       'canciones': colaReproducción
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
            # Verificar si la canción ya está en la lista
            if not misCanciones.contains(cancion_select):
                misCanciones.add(cancion_select)
                print(f"ID de la canción recibida: {cancion_id}")
                print(f"Detalles de la canción seleccionada: {cancion_select}")
            else:
                print("La canción ya está en la lista.")
                
        except ValueError as e:
            print(f"Error: {e}")

    return redirect('index')

def next_song(request):
    cancion_actual = colaReproducción.next_song()
    print(f"Detalles de la canción seleccionada: {cancion_actual.track_name}")
    
    # Convertir el objeto cancion_actual en un diccionario
    contexto = {
        "cancion" : cancion_actual,
        "canciones": misCanciones
    }

    return render(request, "reproduccion/page.html", contexto)

def prev_song():

    return redirect('reproducir')

