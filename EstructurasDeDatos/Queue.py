import random
from .LinkedList import LinkedList

class Node:
    def __init__(self, data, position=None):
        self.data = data
        self.next = None
        self.prev = None
        self.position = position 

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0
        self.current = None

    def is_empty(self):
        return self.size == 0

    def enqueue(self, data):
        new_node = Node(data, self.size)  # Establecemos la posición del nuevo nodo
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            new_node.prev = self.rear
            self.rear = new_node
        self.size += 1
        if self.size == 1:
            self.current = self.front

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        data = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        else:
            self.front.prev = None
        self.size -= 1
        if self.current == self.front:
            self.current = self.front
        return data

    def remove(self, item):
        current = self.front
        while current:
            if current.data == item:
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                if current == self.front:
                    self.front = current.next
                if current == self.rear:
                    self.rear = current.prev
                self.size -= 1
                self._update_positions()  # Actualizamos las posiciones después de la eliminación
                return
            current = current.next
        raise ValueError("Item not found in queue")

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty queue")
        return self.front.data

    def __len__(self):
        return self.size

    def __iter__(self):
        self.iter_node = self.front
        return self

    def __next__(self):
        if self.iter_node is None:
            raise StopIteration
        data = self.iter_node.data
        self.iter_node = self.iter_node.next
        return data

    def get_current(self):
        if self.current is None:
            raise IndexError("No current song")
        return self.current.data

    def next_song(self):
        if self.current is None or self.current.next is None:
            raise IndexError("No next song")
        self.current = self.current.next
        return self.current.data

    def prev_song(self):
        if self.current is None or self.current.prev is None:
            raise IndexError("No previous song")
        self.current = self.current.prev
        return self.current.data

    def clear(self):
        self.front = None
        self.rear = None
        self.size = 0
        self.current = None

    def contains(self, item):
        current = self.front
        while current:
            if current.data == item:
                return True
            current = current.next
        return False
        
    def peek_front(self):
        if self.is_empty():
            raise IndexError("Peek from empty queue")
        return self.front.data
    
    def peek_rear(self):
        if self.is_empty():
            raise IndexError("Peek from empty queue")
        return self.rear.data

    def find_position(self, item):
        current = self.front
        while current:
            if current.data == item:
                return current.position
            current = current.next
        raise ValueError("Item not found in queue")
    
    def get(self, position):
        if position < 0 or position >= self.size:
            raise IndexError("Position out of bounds")
        current = self.front
        while current:
            if current.position == position:
                return current.data
            current = current.next
        raise ValueError("Song not found at position")
    
    def put(self, position, new_data):
        if position < 0 or position >= self.size:
            raise IndexError("Position out of bounds")
        current = self.front
        while current:
            if current.position == position:
                current.data = new_data
                return
            current = current.next
        raise ValueError("Position not found")

    def _update_positions(self):
        current = self.front
        position = 0
        while current:
            current.position = position
            current = current.next
            position += 1

    def change_position(self, posicion_actual, posicion_nueva):
        if posicion_actual == posicion_nueva:
            return

        if (posicion_actual < 0 or posicion_actual >= self.size or
            posicion_nueva < 0 or posicion_nueva >= self.size):
            raise IndexError("Posición fuera de los límites")
        
        factCambio = posicion_actual - posicion_nueva
        data_actual = self.get(posicion_actual)
        if factCambio < 0:
            for i in range(abs(factCambio)):
                data_nueva = self.get(posicion_actual + 1 + i)
                self.put(posicion_actual + i, data_nueva)
            self.put(posicion_nueva, data_actual)
        else:
            for i in range(abs(factCambio)):
                data_nueva = self.get(posicion_actual - 1 - i)
                self.put(posicion_actual - i, data_nueva)
            self.put(posicion_nueva, data_actual)

        self._update_positions()


    def random(self):
        if self.is_empty():
            return

        # Convertir la cola a una LinkedList
        lista_datos = LinkedList()
        actual = self.front
        while actual:
            lista_datos.add(actual.data)
            actual = actual.next

        # Barajar usando el algoritmo de Fisher-Yates
        n = len(lista_datos)
        for i in range(n - 1, 0, -1):
            j = random.randint(0, i)
            lista_datos.swap(i, j)

        # Vaciar la cola
        self.clear()

        # Rellenar la cola con los datos barajados
        current = lista_datos.head
        while current:
            self.enqueue(current.data)
            current = current.next