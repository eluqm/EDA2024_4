import sys
sys.path.append("../")
from leer_csv import leer_csv
from .EstructurasDeDatos.Trie import Trie

archivo_csv = 'archive\\spotify_data.csv'
canciones = leer_csv(archivo_csv, 100)
trieArbol = Trie()

#Se insertan las n canciones dentro del trie
for cancion in canciones:
    trieArbol.insert(cancion.get_track_name(), cancion)

#Lista con todas las canciones que empiezan con la letra
resultado_busqueda = trieArbol.searchAll('W')
