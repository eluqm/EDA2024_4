import sys
from .EstructurasDeDatos.Array import Array

sys.path.append("../")
from leer_csv import leer_csv

# Crear instancias de Cancion
numero = int(input("Ingresar las canciones: "))
canciones = Array(int(numero))

def datos():
  canciones = leer_csv("../archive/spotify_data.csv", numero)
  return canciones
