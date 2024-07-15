from leer_csv import *
from HashMap.HashMap import *
archivo_csv = "./archive/spotify_data.csv"

def main():
    canciones_map = HashMap()
    cancionesnum = 0

    try:
        canciones = leer_csv(archivo_csv)
        for cancion in canciones:
            canciones_map.put(cancion.get_artist_id(), cancion)

        for entry in canciones_map.entry_set():
            key = entry.key
            value = entry.value
            print(f"Key: {key}, Value: {value}")
            cancionesnum += 1

        print(f"Número de canciones: {cancionesnum}")

    except IOError as e:
        print(f"Error leyendo el archivo: {e}")

if __name__ == "__main__":
    main()