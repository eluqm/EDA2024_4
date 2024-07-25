from cancion import Cancion
from EstructurasDeDatos.Array import Array
from EstructurasDeDatos.LinkedList import LinkedList
import csv

def leer_csv(archivo_csv, n):
    canciones = LinkedList()
    lista_canciones = []
    with open(archivo_csv, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        contador = 0  

        for row in reader:
            if contador < n:
                # Crear una instancia de Cancion con los datos del CSV
                cancion = Cancion(
                    id=row['id'].strip(),
                    artist_name=row['artist_name'].strip(),
                    track_name=row['track_name'].strip(),
                    track_year=row['year'].strip(),
                    track_id=row['track_id'].strip(),
                    track_popularity=int(row['popularity']),
                    track_duration_ms=int(row['duration_ms'])
                )
                lista_canciones.append(cancion)
                contador += 1 
            else:
                break 
    
    for cancion in lista_canciones:
        canciones.add(cancion)
    
    return canciones