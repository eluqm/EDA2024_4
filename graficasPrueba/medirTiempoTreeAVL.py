import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..',)))

import time
from EstructurasDeDatos.TreeAVL import AVLTree 
from cancion import Cancion 

def medir_tiempo_insercion(elementos):
    avl_tree = AVLTree()
    start_time = time.time()
    for elemento in elementos:
        song = Cancion(
            id=elemento,
            artist_name=f"Artist {elemento}",
            track_year="2024", 
            track_name=f"Song {elemento}",
            track_id=f"ID{elemento}",
            track_popularity=50,  
            track_duration_ms=1800
        )
        avl_tree.insert(elemento, song)
    end_time = time.time()
    return end_time - start_time