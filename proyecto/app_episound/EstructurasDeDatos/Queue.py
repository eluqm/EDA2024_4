class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0
        self.current = None

    def is_empty(self):
        return self.size == 0

    def enqueue(self, data):
        new_node = Node(data)
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

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty queue")
        return self.front.data

    def __len__(self):
        return self.size
    
    def get_current(self):
        if self.current is None:
            raise IndexError("No current song")
        return self.current.data

    def next_song(self):
        if self.current is None or self.current.next is None:
            raise IndexError("No next song")
        self.current = self.current.next
        return self.current.data