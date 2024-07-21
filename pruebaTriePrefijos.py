from EstructurasDeDatos.Trie import Trie
from leer_csv import leer_csv 

def main():
    archivo_csv = 'archive\\spotify_data.csv' 
    canciones = leer_csv(archivo_csv, 100)
    trieArbol = Trie()
    
    for cancion in canciones:
        trieArbol.insert(cancion.get_track_name())

    resultado_busqueda = trieArbol.searchAll('W')
    print('Resultado de búsqueda para "W":')
    for palabra in resultado_busqueda:
        print(palabra)

if __name__ == "__main__":
    main()