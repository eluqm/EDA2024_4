from .HashMap import HashMap  
from .LinkedList import LinkedList

class TrieNode:
    def __init__(self):
        self.children = HashMap()  
        self.isWord = False
        self.songs = LinkedList()

class Trie:
    def __init__(self):
        # El Trie comienza con un nodo raíz vacío.
        self.root = TrieNode()
    
    # Inserta una palabra en el Trie.
    def insert(self, word, song):
        current = self.root
        for char in word:
            if not current.children.containsKey(char):
                current.children.put(char, TrieNode())
            current = current.children.get(char)
        current.isWord = True
        current.songs.add(song)
    
    # Busca una palabra en el Trie.
    def search(self, word):
        current = self.root
        for char in word:
            if not current.children.containsKey(char):
                return LinkedList() 
            current = current.children.get(char)
        return current.songs if current.isWord else LinkedList()
    
    # Verifica si hay alguna palabra en el Trie que empiece con el prefijo dado.
    def startsWith(self, prefix):
        current = self.root
        for char in prefix:
            if not current.children.containsKey(char):
                return False
            current = current.children.get(char)
        return True
    
    # Busca todas las palabras que comienzan con el prefijo dado y las devuelve en una lista.
    def searchAll(self, prefix):
        current = self.root
        for char in prefix:
            if not current.children.containsKey(char):
                return LinkedList() 
            current = current.children.get(char)
        
        words_list = LinkedList()
        self.searchDepth(current, prefix, words_list)
        return words_list

    # Busca todas las palabras a partir del nodo dado y agrega las palabras encontradas a la lista.
    def searchDepth(self, node, prefix, words_list):
        if node.isWord:
            for song in node.songs:
                words_list.add(song)
        
        for char in node.children.entry_set():
            self.searchDepth(node.children.get(char.key), prefix + char.key, words_list)