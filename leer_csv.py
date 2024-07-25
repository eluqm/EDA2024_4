from cancion import Cancion
from EstructurasDeDatos.LinkedList import LinkedList
from collections import namedtuple
import csv
import random

def leer_csv(archivo_csv, n):
    canciones = LinkedList()
    canciones_lista = []

    # Leer todas las canciones del archivo CSV
    with open(archivo_csv, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            cancion = Cancion(
                id=row['id'].strip(),
                artist_name=row['artist_name'].strip(),
                track_name=row['track_name'].strip(),
                track_year=row['year'].strip(),
                track_id=row['track_id'].strip(),
                track_popularity=int(row['popularity']),
                track_duration_ms=int(row['duration_ms'])
            )
            canciones_lista.append(cancion)

    # Seleccionar aleatoriamente n canciones sin repetir
    canciones_seleccionadas = random.sample(canciones_lista, min(n, len(canciones_lista)))

    # Agregar las canciones seleccionadas a la lista enlazada
    for cancion in canciones_seleccionadas:
        canciones.add(cancion)

    return canciones