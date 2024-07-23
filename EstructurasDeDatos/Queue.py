class Node:
    def __init__(self, data, position=None):
        self.data = data
        self.next = None
        self.position = position  # Añadido para mantener la posición del nodo

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
        self.size -= 1
        if self.current == self.front:
            self.current = self.front
        return data

    def remove(self, item):
        current = self.front
        previous = None

        while current:
            if current.data == item:
                if previous:
                    previous.next = current.next
                else:
                    self.front = current.next
                if not current.next:
                    self.rear = previous
                self.size -= 1
                self._update_positions()  # Actualizamos las posiciones después de la eliminación
                return
            previous = current
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
        if self.current is None or self.current == self.front:
            raise IndexError("No previous song")
        current = self.front
        while current.next != self.current:
            current = current.next
        self.current = current
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

    def _update_positions(self):
        current = self.front
        position = 0
        while current:
            current.position = position
            current = current.next
            position += 1