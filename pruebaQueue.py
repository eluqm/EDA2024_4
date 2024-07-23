from EstructurasDeDatos.Queue import Queue
from cancion import Cancion

def main():
    queue = Queue()

    # Crear canciones
    song1 = Cancion(track_name="Song A", track_id="a1", track_popularity=80, track_duration_ms=210000)
    song2 = Cancion(track_name="Song B", track_id="b1", track_popularity=85, track_duration_ms=220000)
    song3 = Cancion(track_name="Song C", track_id="c1", track_popularity=75, track_duration_ms=200000)

    # Encolar canciones
    queue.enqueue(song1)
    queue.enqueue(song2)
    queue.enqueue(song3)

    print("Contenido de la cola:")
    for song in queue:
        if(song == queue.get_current()):
            print('Sonando');
            print(song);
            print('----');
        print(song)

    # Verificar tamaño
    print('TAMAÑO DE LA COLA');
    print(len(queue));

    # Verificar el elemento al frente
    print('PRIMERA CANCIÓN');
    print(queue.peek_front());

    # Verificar el elemento al final
    print('ULTIMA CANCIÓN');
    print(queue.peek_rear());

    # Obtener y verificar el elemento actual
    print('CANCIÓN QUE ESTA SONANDO');
    print(queue.get_current());

    # Obtener siguiente canción
    queue.next_song();
    
    print('\n\nCANCIÓN ACTUAL');
    print(queue.get_current());

    queue.next_song();
    print('CANCIÓN ACTUAL');
    print(queue.get_current());

    try:
        print(queue.next_song());
    except IndexError as e:
        assert str(e) == "No next song", "Error: Mensaje de error para siguiente canción no encontrado"

    print('\n\n\nCANCIÓN ACTUAL');
    print(queue.get_current());

    try:
        print(queue.prev_song());
    except IndexError as e:
        assert str(e) == "No previous song", "Error: Mensaje de error para canción previa no encontrado"

    
    print("\n\nContenido de la cola:")
    for song in queue:
        if(song == queue.get_current()):
            print('Sonando');
            print(song);
            print('----');
            next
        else:
            print(song)

    queue.remove(song2)
    assert len(queue) == 2, "Error: Tamaño de la cola no es 2 después de eliminar Song B"
    assert not queue.contains(song2), "Error: La canción eliminada aún está en la cola"

if __name__ == "__main__":
    main()