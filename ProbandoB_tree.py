from EstructurasDeDatos.B_tree import BTree
from EstructurasDeDatos.LinkedList import LinkedList
from EstructurasDeDatos.HashMap import HashMap
from cancion import Cancion

def main():
    canciones = [
        Cancion(id="1", artist_name="Artist A", track_year=2020, track_name="Song A", track_id="a1", track_popularity=80, track_duration_ms=210000),
        Cancion(id="2", artist_name="Artist B", track_year=2021, track_name="Song B", track_id="b1", track_popularity=85, track_duration_ms=220000),
        Cancion(id="3", artist_name="Artist C", track_year=2020, track_name="Song C", track_id="c1", track_popularity=75, track_duration_ms=200000),
        Cancion(id="7", artist_name="Artist T", track_year=2020, track_name="Song C", track_id="c1", track_popularity=75, track_duration_ms=200000),
        Cancion(id="8", artist_name="Artist Y", track_year=2020, track_name="Song C", track_id="c1", track_popularity=75, track_duration_ms=200000),
        Cancion(id="9", artist_name="Artist U", track_year=2020, track_name="Song C", track_id="c1", track_popularity=75, track_duration_ms=200000),
        Cancion(id="10", artist_name="Artist O", track_year=2020, track_name="Song C", track_id="c1", track_popularity=75, track_duration_ms=200000),
        Cancion(id="4", artist_name="Artist D", track_year=2022, track_name="Song D", track_id="d1", track_popularity=90, track_duration_ms=230000),
        Cancion(id="4", artist_name="Artist D", track_year=2022, track_name="Song D", track_id="d1", track_popularity=90, track_duration_ms=230000),
        Cancion(id="4", artist_name="Artist D", track_year=2022, track_name="Song D", track_id="d1", track_popularity=90, track_duration_ms=230000),
        Cancion(id="4", artist_name="Artist D", track_year=2022, track_name="Song D", track_id="d1", track_popularity=90, track_duration_ms=230000),
        Cancion(id="4", artist_name="Artist D", track_year=2022, track_name="Song D", track_id="d1", track_popularity=90, track_duration_ms=230000),
        Cancion(id="4", artist_name="Artist D", track_year=2022, track_name="Song D", track_id="d1", track_popularity=90, track_duration_ms=230000),
        Cancion(id="4", artist_name="Artist D", track_year=2022, track_name="Song D", track_id="d1", track_popularity=90, track_duration_ms=230000),
        Cancion(id="4", artist_name="Artist D", track_year=2022, track_name="Song D", track_id="d1", track_popularity=90, track_duration_ms=230000),
        Cancion(id="5", artist_name="Artist E", track_year=2021, track_name="Song E", track_id="e1", track_popularity=95, track_duration_ms=250000)
    ]

    btree = BTree(3)  # Ejemplo con grado mínimo 2

    for cancion in canciones:
        btree.insert(cancion.track_duration_ms, cancion)

    btree.print_tree()
    print("\nCanciones en orden ascendente:")
    btree.ascending()

    # Mostrar canciones en orden descendente
    print("\nCanciones en orden descendente:")
    btree.descending()

if __name__ == "__main__":
    main()



