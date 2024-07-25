
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseBadRequest
from django.http import JsonResponse
from .in_memory_data import canciones, current_song, datos
from .EstructurasDeDatos.HashMap import HashMap
from .EstructurasDeDatos.LinkedList import LinkedList
from .EstructurasDeDatos.Queue import Queue
from .EstructurasDeDatos.Trie import Trie
from .EstructurasDeDatos.B_tree import BTree
from .EstructurasDeDatos.AVLTree import AVLTree

misCanciones = LinkedList()
colaReproducción = Queue()
global_canciones = datos()
songsBtree = BTree(3)
songsAVlAño = AVLTree()
songAVlPopularidad = AVLTree()

trieArbol = Trie()
for cancion in global_canciones:
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

def guardar_id(request):
    if request.method == 'POST':
        cancion_id = request.POST.get('cancion_id')
        try:
            cancion_id = int(cancion_id)
            cancion_select = global_canciones.get_by_id(cancion_id)
            print(cancion_select)
            if not misCanciones.contains(cancion_select):
                misCanciones.add(cancion_select)
                colaReproducción.enqueue(cancion_select)
                print(f"ID de la canción recibida: {cancion_id}")
                print(f"Detalles de la canción seleccionada: {cancion_select}")
            else:
                print("La canción ya está en la lista o no se encontró.")
                
        except ValueError as e:
            print(f"Error: {e}")

    return redirect('index')

def guardar_idBusc(request):
    if request.method == 'POST':
        cancion_id = request.POST.get('cancion_id')
        try:
            cancion_id = int(cancion_id)
            cancion_select = global_canciones.get_by_id(cancion_id)
            if not misCanciones.contains(cancion_select):
                misCanciones.add(cancion_select)
                colaReproducción.enqueue(cancion_select)
                print(f"ID de la canción recibida: {cancion_id}")
                print(f"Detalles de la canción seleccionada: {cancion_select}")
            else:
                print("La canción ya está en la lista.")
                
        except ValueError as e:
            print(f"Error: {e}")

    return redirect('buscar')

def eliminar_id(request):
    if request.method == 'POST':
        cancion_id = request.POST.get('cancion_id')
        try:
            cancion_id = int(cancion_id)
            cancion_select = global_canciones.get(cancion_id)
            
            if misCanciones.contains(cancion_select):
                misCanciones.remove(cancion_select)  # Elimina de la lista de canciones
                if colaReproducción.contains(cancion_select):
                    colaReproducción.remove(cancion_select)  # Elimina de la cola de reproducción
                print(f"ID de la canción recibida: {cancion_id}")
                print(f"Detalles de la canción eliminada: {cancion_select}")
            else:
                print("La canción no está en la lista.")
                
        except ValueError as e:
            print(f"Error: {e}")

    context = {
            'canciones': colaReproducción
    }

    return render(request, "miMusica/page.html", context)

def reproducir(request):
    # Verifica si colaReproducción está definida y tiene canciones
    if not colaReproducción or colaReproducción.is_empty():
        context = {
            'canciones': [],
            'current_song': None
        }
    else:
        context = {
            'canciones': colaReproducción,
            'current_song': colaReproducción.peek()  # Mostrar la canción actual
        }
    
    return render(request, "reproduccion/page.html", context)

def next_song(request):
    try:
        current_song = colaReproducción.next_song()
        context = {
            'canciones': colaReproducción,
            'current_song': current_song,
            'show_alert': False
        }
        return render(request, "reproduccion/page.html", context)
    except IndexError:
        ultima_cancion = colaReproducción.peek_rear()
        context = {
            'canciones': colaReproducción,
            'current_song': ultima_cancion,
            'show_alert': True,
            'alert_message': 'No hay más canciones para avanzar.'
        }
        return render(request, "reproduccion/page.html", context)

def prev_song(request):
    try:
        current_song = colaReproducción.prev_song()
        context = {
            'canciones': colaReproducción,
            'current_song': current_song,
            'show_alert': False
        }
        return render(request, "reproduccion/page.html", context)
    except IndexError:
        primera_cancion = colaReproducción.peek_front()
        context = {
            'canciones': colaReproducción,
            'current_song': primera_cancion,
            'show_alert': True,
            'alert_message': 'No hay canciones anteriores.'
        }
        return render(request, "reproduccion/page.html", context)

def play_song(request):
    try:
        song_actual = colaReproducción.get_current()
        
        spotify_url = f"https://open.spotify.com/track/{song_actual.track_id}"
        print("Direccion preparada")
        return redirect(spotify_url)
    except IndexError:

        return HttpResponseBadRequest("No hay canción actual para reproducir.")

def TimeDurationBtree(request):
    context = {
        'canciones': colaReproducción
    }
    return render(request, "miMusica/duracion.html", context)

def TimeDurationAvl(request):
    context = {
        'canciones': colaReproducción
    }
    return render(request, "miMusica/año.html", context)

def TimePopularidadAvl(request):
    context = {
        'canciones': colaReproducción
    }
    return render(request, "miMusica/popularidad.html", context)

#Esto ya es el ordenamiento

def songs_ascend_btree(request):
    songsBtree.clear()

    # Itera sobre las canciones en misCanciones e inserta en el BTree
    for cancion in misCanciones:
        songsBtree.insert(cancion.track_duration_ms, cancion)

    # Obtén las canciones en orden ascendente
    canciones_ordenadas = songsBtree.ascending()

    context = {
        'canciones': canciones_ordenadas
    }

    return render(request, "miMusica/duracion.html", context)

def songs_descend_btree(request):
    songsBtree.clear()

    # Itera sobre las canciones en misCanciones e inserta en el BTree
    for cancion in misCanciones:
        songsBtree.insert(cancion.track_duration_ms, cancion)

    # Obtén las canciones en orden ascendente
    canciones_ordenadas = songsBtree.descending()

    context = {
        'canciones': canciones_ordenadas
    }

    return render(request, "miMusica/duracion.html", context)

def random(request):
    colaReproducción.random()
    context = {
        'canciones': colaReproducción,
        'current_song': colaReproducción.peek()  # Mostrar la canción actual
    }
    return render(request, "reproduccion/page.html", context)

def songs_ascend_btree(request):
    songsBtree.clear()
    for cancion in misCanciones:
        songsBtree.insert(cancion.track_duration_ms, cancion)
    canciones_ordenadas = songsBtree.ascending()
    context = {
        'canciones': canciones_ordenadas
    }
    return render(request, "miMusica/duracion.html", context)

def songs_descend_btree(request):
    songsBtree.clear()
    for cancion in misCanciones:
        songsBtree.insert(cancion.track_duration_ms, cancion)
    canciones_ordenadas = songsBtree.descending()
    context = {
        'canciones': canciones_ordenadas
    }
    return render(request, "miMusica/duracion.html", context)

def songs_ascend_avlAños(request):
    songsAVlAño.clear()
    for cancion in misCanciones:
        songsAVlAño.insert(cancion.track_year, cancion)
    canciones_ordenadas = songsAVlAño.ascending()
    context = {
        'canciones': canciones_ordenadas
    }
    return render(request, "miMusica/año.html", context)

def songs_descend_avlAños(request):
    songsAVlAño.clear()
    for cancion in misCanciones:
        songsAVlAño.insert(cancion.track_year, cancion)
    canciones_ordenadas = songsAVlAño.descending()
    context = {
        'canciones': canciones_ordenadas
    }
    return render(request, "miMusica/año.html", context)

def songs_ascend_avlPopularidad(request):
    songAVlPopularidad.clear()
    for cancion in misCanciones:
        songAVlPopularidad.insert(cancion.track_popularity, cancion)
    canciones_ordenadas = songAVlPopularidad.ascending()
    context = {
        'canciones': canciones_ordenadas
    }
    return render(request, "miMusica/popularidad.html", context)

def songs_descend_avlPopularidad(request):
    songAVlPopularidad.clear()
    for cancion in misCanciones:
        songAVlPopularidad.insert(cancion.track_popularity, cancion)
    canciones_ordenadas = songAVlPopularidad.descending()
    context = {
        'canciones': canciones_ordenadas
    }
    return render(request, "miMusica/popularidad.html", context)
