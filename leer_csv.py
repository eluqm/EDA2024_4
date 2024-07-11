from cancion import Cancion
import csv

def leer_csv(archivo_csv):
    canciones = []
    with open(archivo_csv, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        contador = 0  

        for row in reader:
            if contador < 50:
                cancion = Cancion()
                cancion.set_artist_name(row['artist_name'].strip())
                cancion.set_track_name(row['track_name'].strip())
                cancion.set_track_id(row['track_id'].strip()) 
                cancion.set_popularity(int(row['popularity']))
                cancion.set_year(int(row['year']))
                cancion.set_duration_ms(int(row['duration_ms']))
                canciones.append(cancion)
                contador += 1 
            else:
                break 

    return canciones