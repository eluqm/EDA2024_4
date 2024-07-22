import sys
sys.path.append("../")
from leer_csv import leer_csv

# Crear instancias de Cancion
canciones = leer_csv("../archive/spotify_data.csv",16)