import time

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertar(self, data):
        nuevo_nodo = Node(data)
        nuevo_nodo.next = self.head
        self.head = nuevo_nodo

def medir_tiempo_insercion(elementos):
    linked_list = LinkedList()
    start_time = time.time()
    for elemento in elementos:
        linked_list.insertar(elemento)
    end_time = time.time()
    return end_time - start_time