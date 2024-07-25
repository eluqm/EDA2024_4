from EstructurasDeDatos.Queue import Queue
from cancion import Cancion

def main():
    queue = Queue()

    # Crear canciones
    song1 = Cancion(id="1", track_name="Song A", track_id="1", track_popularity=80, track_duration_ms=210000)
    song2 = Cancion(id="2", track_name="Song B", track_id="2", track_popularity=85, track_duration_ms=220000)
    song3 = Cancion(id="3", track_name="Song C", track_id="3", track_popularity=75, track_duration_ms=200000)
    song4 = Cancion(id="4", track_name="Song D", track_id="4", track_popularity=75, track_duration_ms=200000)
    song5 = Cancion(id="5", track_name="Song E", track_id="5", track_popularity=75, track_duration_ms=200000)
    song6 = Cancion(id="6",track_name="Song F", track_id="6", track_popularity=75, track_duration_ms=200000)


    # Encolar canciones
    queue.enqueue(song1)
    queue.enqueue(song2)
    queue.enqueue(song3)
    queue.enqueue(song4)
    queue.enqueue(song5)
    queue.enqueue(song6)
    
    

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

    print('\n---------PRUEBAS DE CAMBIO DE POSICIÓN---------')
    for song in queue:
        if(song == queue.get_current()):
            print('Sonando')
            print(song);
            print('----')
            next
        else:
            print(song)

    print('\nBusqueda de la cancion C: ')
    print(queue.find_position(song3))

    print(queue.get(0))
    
    queue.change_position(queue.find_position(song3), 0)

    print('\n---------PRUEBAS DE CAMBIO DE POSICIÓN---------')
    for song in queue:
        if(song == queue.get_current()):
            print('Sonando')
            print(song);
            print('----')
            next
        else:
            print(song)

    queue.random()

    print('\n---------PRUEBAS ALEATORIO---------')
    for song in queue:
        if(song == queue.get_current()):
            print('Sonando')
            print(song);
            print('----')
            next
        else:
            print(song)


if __name__ == "__main__":
    main()  