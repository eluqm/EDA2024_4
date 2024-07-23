import sys
sys.path.append("../")
from leer_csv import leer_csv

# Crear instancias de Cancion
canciones = leer_csv("../archive/spotify_data.csv",1000)

current_song = {
    'track_name': 'You are all that I have',
    'artist_name': 'Makanaky la realeza',
    'track_duration_ms': '316316',
    'views': '1 214 321',
    'rank': '1',
    'year': '2024'
}

def datos():
  return canciones

next_song = {'track_name': 'Rara Vez', 'artist_name': 'Milo J'}
