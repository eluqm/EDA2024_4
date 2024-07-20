import sys
import os

# Agrega el directorio principal al sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from EstructurasDeDatos.B_tree import BTree
from leer_csv import leer_csv
from EstructurasDeDatos.LinkedList import LinkedList
from EstructurasDeDatos.HashMap import HashMap

def extraer_años(canciones):
    """Extrae los años de una lista de canciones."""
    años = HashMap()
    for cancion in canciones:
        año = cancion.get_track_year()
        if not años.containsKey(año):  # Accede al año de la canción
            años.put(año, LinkedList())
        cancionesRecolectadas = años.get(año)
        cancionesRecolectadas.add(cancion)
    return años

n = int(input("Introduce el número de canciones a listar: "))
valor = int(input("Año a buscar: "))
canciones = leer_csv('archive/spotify_data.csv', n)
t = 3  # Grado mínimo
btree = BTree(t)
años = extraer_años(canciones)

# Inserta los años en el B-tree
for entry in años.entry_set():
    año = entry.key
    btree.insert(int(año))  # Accede a los datos del nodo
    if int(año) == valor:
        print(f"Canciones del año {año}:")
        for cancion in entry.value:
            print(cancion)  # Imprimir información de la canción

# Imprimir el árbol
print("\nB-tree:")
btree.print_tree()

