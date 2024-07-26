class Array:
    def __init__(self, capacity=10):
        self._capacity = capacity
        self._size = 0
        self._data = [None] * capacity 
    
    def _resize(self, new_capacity):
        new_data = [None] * new_capacity
        for i in range(self._size):
            new_data[i] = self._data[i]
        self._data = new_data
        self._capacity = new_capacity

    def append(self, item):
        if self._size == self._capacity:
            self._resize(2 * self._capacity) 
        self._data[self._size] = item
        self._size += 1

    def get(self, index):
        if index < 0 or index >= self._size:
            raise IndexError("Índice fuera de rango.")
        return self._data[index]

    def __len__(self):
        return self._size
    
    def __iter__(self):
        for i in range(self._size):
            yield self._data[i]

    def get_by_id(self, id):
        for item in self._data:
            if item is not None and hasattr(item, 'id') and item.id == id:
                return item
        return None