from .HashMap import HashMap  
from .LinkedList import LinkedList

class TrieNode:
    def __init__(self):
        # El HashMap usa caracteres como claves y los nodos hijos como valores.
        self.children = HashMap()  
        # Marca si este nodo representa el final de una palabra.
        self.isWord = False

class Trie:
    def __init__(self):
        # El Trie comienza con un nodo raíz vacío.
        self.root = TrieNode()
    
    def insert(self, word):
        current = self.root
        for char in word:
            # Si el carácter no está en los hijos del nodo actual, se agrega un nuevo nodo.
            if not current.children.containsKey(char):
                current.children.put(char, TrieNode())
            # Mover al siguiente nodo según el carácter actual.
            current = current.children.get(char)
        # Marca el final de la palabra.
        current.isWord = True
    
    def search(self, word):
        current = self.root
        for char in word:
            # Si el carácter no está en los hijos del nodo actual, la palabra no está en el Trie.
            if not current.children.containsKey(char):
                return False
            # Mover al siguiente nodo según el carácter actual.
            current = current.children.get(char)
        # Devuelve True si el nodo final de la palabra está marcado como verdadero.
        return current.isWord
    
    def startsWith(self, prefix):
        current = self.root
        for char in prefix:
            # Si el carácter del prefijo no está en los hijos del nodo actual, el prefijo no está en el Trie.
            if not current.children.containsKey(char):
                return False
            # Mover al siguiente nodo según el carácter actual.
            current = current.children.get(char)
        # Si se recorren todos los caracteres del prefijo, se considera que el prefijo existe en el Trie.
        return True
    
    def searchAll(self, prefix):
        current = self.root
        for char in prefix:
            if not current.children.containsKey(char):
                return LinkedList() 
            current = current.children.get(char)
        
        words_list = LinkedList()
        self.searchDepth(current, prefix, words_list)
        return words_list

    def searchDepth(self, node, prefix, words_list):
        if node.isWord:
            words_list.add(prefix)
        
        for char in node.children.entry_set():  # Usar entry_set() para obtener las claves del HashMap
            self.searchDepth(node.children.get(char.key), prefix + char.key, words_list)