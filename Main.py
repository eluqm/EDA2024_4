from EstructurasDeDatos.Trie import Trie
from leer_csv import leer_csv 

def main():
    archivo_csv = 'archive\\spotify_data.csv' 
    canciones = leer_csv(archivo_csv, 100)
    trieArbol = Trie()
    
    for cancion in canciones:
        trieArbol.insert(cancion.get_track_name())

    resultado_busqueda = trieArbol.search('Do Not Let Me Go')
    print(f'Resultado de búsqueda para: {resultado_busqueda}')

if __name__ == "__main__":
    main()