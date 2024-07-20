from .HashMap import HashMap  

class TrieNode:
    def __init__(self):
        self.children = HashMap()  
        self.isWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        current = self.root
        for char in word:
            if not current.children.containsKey(char):
                current.children.put(char, TrieNode())
            current = current.children.get(char)
        current.isWord = True
    
    def search(self, word):
        current = self.root
        for char in word:
            if not current.children.containsKey(char):
                return False
            current = current.children.get(char)
        return current.isWord
    
    def startsWith(self, prefix):
        current = self.root
        for char in prefix:
            if not current.children.containsKey(char):
                return False
            current = current.children.get(char)
        return True