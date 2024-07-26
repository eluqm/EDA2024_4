import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..',)))

import time
from EstructurasDeDatos.LinkedList import LinkedList

def medir_tiempo_insercion(elementos):
    linked_list = LinkedList()
    start_time = time.time()
    for i, elemento in enumerate(elementos):
        linked_list.insert(i, elemento)  
    end_time = time.time()
    return end_time - start_time