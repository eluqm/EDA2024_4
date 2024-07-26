import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..',)))

import time
from EstructurasDeDatos.Array import Array

def medir_tiempo_insercion(elementos):
    array = Array(99001)
    start_time = time.time()
    for elemento in elementos:
        array.append(elemento)
    end_time = time.time()
    return end_time - start_time