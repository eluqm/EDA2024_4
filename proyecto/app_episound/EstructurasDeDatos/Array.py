class Array:
    def __init__(self, capacity=10):
        self._capacity = capacity
        self._size = 0
        self._data = [None] * capacity 
    
    def _resize(self, new_capacity):
        """Redimensiona el arreglo cuando se supera la capacidad actual."""
        new_data = [None] * new_capacity
        for i in range(self._size):
            new_data[i] = self._data[i]
        self._data = new_data
        self._capacity = new_capacity

    def append(self, item):
        if self._size == self._capacity:
            self._resize(2 * self._capacity)  # Doble la capacidad si es necesario
        self._data[self._size] = item
        self._size += 1

    def get(self, index):
        """Devuelve el elemento en la posición especificada."""
        if index < 0 or index >= self._size:
            raise IndexError("Índice fuera de rango.")
        return self._data[index]

    def __len__(self):
        """Devuelve la longitud del arreglo."""
        return self._size
    
    def __iter__(self):
        """Función para poder iterar."""
        for i in range(self._size):
            yield self._data[i]