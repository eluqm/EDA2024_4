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
    
    def change_position(self, current_pos, new_pos):
        if current_pos < 0 or new_pos < 0 or current_pos >= self.size or new_pos >= self.size:
            raise IndexError("Position out of bounds")

        if self.is_empty():
            return

        if current_pos == new_pos:
            return

        prev_node = None
        node_to_move = self.front
        for _ in range(current_pos):
            prev_node = node_to_move
            node_to_move = node_to_move.next

        # Remove the node from the queue
        if prev_node:
            prev_node.next = node_to_move.next
        else:
            self.front = node_to_move.next
        
        if node_to_move == self.rear:
            self.rear = prev_node
        
        # Insert the node at the new position
        if new_pos == 0:
            node_to_move.next = self.front
            self.front = node_to_move
        else:
            prev_node = None
            insert_after_node = self.front
            for _ in range(new_pos - 1):
                prev_node = insert_after_node
                insert_after_node = insert_after_node.next
            
            node_to_move.next = insert_after_node.next
            insert_after_node.next = node_to_move
            
            if node_to_move.next is None:
                self.rear = node_to_move