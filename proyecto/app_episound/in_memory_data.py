import sys
from .EstructurasDeDatos.Array import Array

sys.path.append("../")
from leer_csv import leer_csv


def datos():
  numero = int(input("Ingresar las canciones: "))
  canciones = leer_csv("../archive/spotify_data.csv", numero)
  return canciones
