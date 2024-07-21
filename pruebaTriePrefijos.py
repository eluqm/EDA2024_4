from EstructurasDeDatos.Trie import Trie
from leer_csv import leer_csv 

def main():
    archivo_csv = 'archive\\spotify_data.csv'
    canciones = leer_csv(archivo_csv, 100)
    trieArbol = Trie()
    
    # Insertar las canciones en el Trie
    for cancion in canciones:
        trieArbol.insert(cancion.get_track_name(), cancion)
    
    # Buscar canciones que empiezan con "W" (o cualquier otro prefijo para probar)
    resultado_busqueda = trieArbol.searchAll('W')
    
    # Imprimir el resultado de búsqueda
    print('Resultado de búsqueda para "W":')
    for cancion in resultado_busqueda:
        print(f' - {cancion}')
        
if __name__ == "__main__":
    main()