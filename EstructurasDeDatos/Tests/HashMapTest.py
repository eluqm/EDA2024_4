from ..HashMap import HashMap
from ..LinkedList import LinkedList

hash_map = HashMap()

# Insertar pares clave-valor
hash_map.put("apple", 1)
hash_map.put("banana", 2)
hash_map.put("grape", 3)

# Obtener valores
print("Get 'apple':", hash_map.get("apple"))  # Debería imprimir 1
print("Get 'banana':", hash_map.get("banana"))  # Debería imprimir 2
print("Get 'grape':", hash_map.get("grape"))  # Debería imprimir 3
print("Get 'orange':", hash_map.get("orange"))  # Debería imprimir None

# Comprobar si la clave existe
print("Contains 'banana':", hash_map.containsKey("banana"))  # Debería imprimir True
print("Contains 'orange':", hash_map.containsKey("orange"))  # Debería imprimir False

# Eliminar una entrada
print("Remove 'banana':", hash_map.remove("banana"))  # Debería imprimir 2
print("Get 'banana':", hash_map.get("banana"))  # Debería imprimir None

# Comprobar si está vacío
print("Is empty:", hash_map.is_empty())  # Debería imprimir False

# Obtener tamaño
print("Size:", len(hash_map))  # Debería imprimir 2 (porque 'banana' fue removido)

entries = hash_map.entry_set()
for entry in entries:
    print(entry) 