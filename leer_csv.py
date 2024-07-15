import csv
from cancion import *
def leer_csv(archivo_csv):
    canciones = []
    with open(archivo_csv, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            cancion = Cancion()
            cancion.set_artist_id(row[0].strip())
            cancion.set_artist_name(row[1].strip())
            cancion.set_track_name(row[2].strip())
            canciones.append(cancion)
    return canciones