from EstructurasDeDatos.TreeAVL import AVLTree
from leer_csv import leer_csv
from cancion import Cancion

def main():
    # Crear algunas canciones con diferentes años
    canciones = [
        Cancion(id="1", track_year=2020, track_name="BSong A", track_id="a1", track_popularity=80, track_duration_ms=210000),
        Cancion(id="2", track_year=2021, track_name="Song B", track_id="b1", track_popularity=85, track_duration_ms=220000),
        Cancion(id="3", track_year=2020, track_name="ASong C", track_id="c1", track_popularity=75, track_duration_ms=200000),
        Cancion(id="4", track_year=2022, track_name="Song D", track_id="d1", track_popularity=90, track_duration_ms=230000),
        Cancion(id="5", track_year=2021, track_name="Song E", track_id="e1", track_popularity=95, track_duration_ms=250000)
    ]

    avlArbol = AVLTree()
    
    # Insertar las canciones en el árbol AVL
    for cancion in canciones:
        avlArbol.insert(cancion.get_track_popularity(), cancion)
    
    # Obtener las canciones en orden ascendente
    print("Canciones ordenadas (ascendente):")
    for song in avlArbol.ascending():
        print(f' - {song}')
    
    # Obtener las canciones en orden descendente
    print("\nCanciones ordenadas (descendente):")
    for song in avlArbol.descending():
        print(f' - {song}')

if __name__ == "__main__":
    main()