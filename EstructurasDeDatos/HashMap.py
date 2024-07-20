from .LinkedList import *

class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __str__(self):
        return f"{self.key} = {self.value}"

class HashMap:
    INITIAL_CAPACITY = 16
    LOAD_FACTOR = 0.75

    def __init__(self):
        # Inicializa la tabla hash con una capacidad inicial y establece el tamaño a 0.
        self.buckets = [LinkedList() for _ in range(self.INITIAL_CAPACITY)]
        self.size = 0

    def get_bucket_index(self, key):
        # Calcula el índice del cubo donde se almacenará la entrada usando la función hash.
        hash_code = hash(key)
        return abs(hash_code) % len(self.buckets)

    def put(self, key, value):
        # Inserta una nueva entrada en la tabla hash o actualiza el valor si la clave ya existe.
        # Redimensiona la tabla si el factor de carga supera el umbral definido.
        if (self.size / len(self.buckets)) >= self.LOAD_FACTOR:
            self.resize()
        bucket_index = self.get_bucket_index(key)
        for entry in self.buckets[bucket_index]:
            if entry.key == key:
                entry.value = value
                return
        self.buckets[bucket_index].add(Entry(key, value))
        self.size += 1

    def get(self, key):
        # Busca y devuelve el valor asociado con la clave dada.
        # Devuelve None si la clave no está presente en la tabla hash.
        bucket_index = self.get_bucket_index(key)
        for entry in self.buckets[bucket_index]:
            if entry.key == key:
                return entry.value
        return None

    def remove(self, key):
        # Elimina la entrada asociada con la clave dada y devuelve su valor.
        # Disminuye el tamaño de la tabla hash si la clave se encuentra y elimina.
        bucket_index = self.get_bucket_index(key)
        for entry in self.buckets[bucket_index]:
            if entry.key == key:
                self.buckets[bucket_index].remove(entry)
                self.size -= 1
                return entry.value
        return None

    def resize(self):
        # Redimensiona la tabla hash cuando el factor de carga supera el umbral.
        # Duplica el tamaño de los cubos y vuelve a insertar todas las entradas.
        old_buckets = self.buckets
        self.buckets = [LinkedList() for _ in range(len(old_buckets) * 2)]
        self.size = 0
        for bucket in old_buckets:
            for entry in bucket:
                self.put(entry.key, entry.value)

    def entry_set(self):
        # Devuelve un conjunto de todas las entradas (pares clave-valor) en la tabla hash.
        entries = set()
        for bucket in self.buckets:
            for entry in bucket:
                entries.add(entry)
        return entries

    def __len__(self):
        # Devuelve el número de entradas en la tabla hash.
        return self.size

    def is_empty(self):
        # Devuelve True si la tabla hash está vacía (tamaño 0).
        return self.size == 0
    
    def containsKey(self, key):
        # Devuelve True si la tabla hash contiene la clave dada.
        bucket_index = self.get_bucket_index(key)
        for entry in self.buckets[bucket_index]:
            if entry.key == key:
                return True
        return False