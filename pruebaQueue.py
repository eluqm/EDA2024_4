from EstructurasDeDatos.Queue import Queue
from cancion import Cancion

def main():
    queue = Queue()

    # Crear canciones
    song1 = Cancion(id="1", artist_name="Artist A", track_year=2020, track_name="Song A", track_id="a1", track_popularity=80, track_duration_ms=210000)
    song2 = Cancion(id="2", artist_name="Artist B", track_year=2021, track_name="Song B", track_id="b1", track_popularity=85, track_duration_ms=220000)
    song3 = Cancion(id="3", artist_name="Artist C", track_year=2020, track_name="Song C", track_id="c1", track_popularity=75, track_duration_ms=200000)

    # Encolar canciones
    queue.enqueue(song1)
    queue.enqueue(song2)
    queue.enqueue(song3)

    # Verificar tamaño
    assert len(queue) == 3, "Error: Tamaño de la cola no es 3"

    # Verificar el elemento al frente
    assert queue.peek_front() == song1, "Error: El frente de la cola no es Song A"

    # Verificar el elemento al final
    assert queue.peek_rear() == song3, "Error: El final de la cola no es Song C"

    # Obtener y verificar el elemento actual
    assert queue.get_current() == song1, "Error: La canción actual no es Song A"

    # Obtener siguiente canción
    assert queue.next_song() == song2, "Error: La siguiente canción no es Song B"
    assert queue.next_song() == song3, "Error: La siguiente canción no es Song C"

    # Intentar obtener siguiente canción cuando no hay más canciones
    try:
        queue.next_song()
    except IndexError as e:
        assert str(e) == "No next song", "Error: Mensaje de error para siguiente canción no encontrado"

    # Intentar obtener canción previa
    assert queue.prev_song() == song2, "Error: La canción previa no es Song B"

    # Intentar obtener canción previa cuando no hay más canciones previas
    try:
        queue.prev_song()
    except IndexError as e:
        assert str(e) == "No previous song", "Error: Mensaje de error para canción previa no encontrado"

    # Eliminar canción y verificar
    queue.remove(song2)
    assert len(queue) == 2, "Error: Tamaño de la cola no es 2 después de eliminar Song B"
    assert not queue.contains(song2), "Error: La canción eliminada aún está en la cola"

    # Vaciar la cola y verificar
    queue.clear()
    assert len(queue) == 0, "Error: Tamaño de la cola no es 0 después de limpiar"

    # Verificar si la cola está vacía
    assert queue.is_empty(), "Error: La cola debería estar vacía"

if __name__ == "__main__":
    main()