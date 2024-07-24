class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def add(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.size += 1

    def remove(self, data):
        if self.head is None:
            return False

        if self.head.data == data:
            self.head = self.head.next
            self.size -= 1
            return True

        current = self.head
        while current.next is not None and current.next.data != data:
            current = current.next

        if current.next is not None:
            current.next = current.next.next
            self.size -= 1
            return True

        return False

    def contains(self, data):
        current = self.head
        while current is not None:
            if current.data == data:
                return True
            current = current.next
        return False

    def __len__(self):
        return self.size

    def __iter__(self):
        self.current = self.head
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration
        data = self.current.data
        self.current = self.current.next
        return data

    def get(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Índice fuera de rango.")
        current = self.head
        for _ in range(index):
            current = current.next
        return current.data

    def clear(self):
        self.head = None
        self.size = 0

    def insert(self, index, data):
        if index < 0 or index > self.size:
            raise IndexError("Índice fuera de rango.")
        if index == 0:
            self.add(data)  # Add at the beginning
        else:
            new_node = Node(data)
            current = self.head
            for _ in range(index - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node
            self.size += 1

    def to_list(self):
        result = []
        current = self.head
        while current is not None:
            result.append(current.data)
            current = current.next
        return result
    
    def swap(self, index1, index2):
        if index1 < 0 or index1 >= self.size or index2 < 0 or index2 >= self.size:
            raise IndexError("Índice fuera de rango.")
        
        node1 = self.get_node(index1)
        node2 = self.get_node(index2)
        
        # Intercambiar los datos
        node1.data, node2.data = node2.data, node1.data

    def get_node(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Índice fuera de rango.")
        
        current = self.head
        for _ in range(index):
            current = current.next
        return current