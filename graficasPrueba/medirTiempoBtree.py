import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..',)))

import time
from EstructurasDeDatos.B_tree import BTree

def medir_tiempo_insercion(elementos):
    btree = BTree(t=3)  
    start_time = time.time()
    for elemento in elementos:
        btree.insert(elemento, f'Song_{elemento}')  
    end_time = time.time()
    return end_time - start_time