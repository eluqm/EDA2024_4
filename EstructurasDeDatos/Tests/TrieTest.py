from ..Trie import *

trie = Trie()

# Pruebas de inserción
print("Inserting 'apple'...")
trie.insert("apple")
print("Inserting 'app'...")
trie.insert("app")
print("Inserting 'banana'...")
trie.insert("banana")

# Pruebas de búsqueda
print("Searching for 'apple':", trie.search("apple"))  # Debería imprimir True
print("Searching for 'app':", trie.search("app"))      # Debería imprimir True
print("Searching for 'banana':", trie.search("banana"))# Debería imprimir True
print("Searching for 'ban':", trie.search("ban"))      # Debería imprimir False
print("Searching for 'apples':", trie.search("apples")) # Debería imprimir False

# Pruebas de prefijos
print("Starts with 'app':", trie.startsWith("app"))    # Debería imprimir True
print("Starts with 'ban':", trie.startsWith("ban"))    # Debería imprimir True
print("Starts with 'bat':", trie.startsWith("bat"))    # Debería imprimir False
print("Starts with 'a':", trie.startsWith("a"))        # Debería imprimir True
print("Starts with 'b':", trie.startsWith("b"))        # Debería imprimir True