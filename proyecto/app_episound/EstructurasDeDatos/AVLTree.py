from .LinkedList import LinkedList  
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1
        self.avlName = AVLTree()
        self.list_songs = LinkedList()

class AVLTree:
    def __init__(self):
        self.root = None

    def _height(self, root):
        if not root:
            return 0
        return root.height
    
    def _update_height(self, node):
        node.height = 1 + max(self._height(node.left), self._height(node.right))

    def _balance_factor(self, node):
        if not node:
            return 0
        return self._height(node.left) - self._height(node.right)
    
    def _rotate_right(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        self._update_height(y)
        self._update_height(x)
        return x
    
    def _rotate_left(self, x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        self._update_height(x)
        self._update_height(y)
        return y
    
    def _rebalance(self, node):
        self._update_height(node)
        balance = self._balance_factor(node)
        
        if balance > 1:
            if self._balance_factor(node.left) < 0:
                node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        
        if balance < -1:
            if self._balance_factor(node.right) > 0:
                node.right = self._rotate_right(node.right)
            return self._rotate_left(node)
        
        return node
    
    def _insert_year(self, root, song):
        if not root:
            new_node = Node(song.get_track_year())
            new_node.avlName.root = new_node.avlName._insert_name(new_node.avlName.root, song.get_track_name(), song)
            return new_node
        
        if song.get_track_year() < root.key:
            root.left = self._insert_year(root.left, song)
        elif song.get_track_year() > root.key:
            root.right = self._insert_year(root.right, song)
        else:
            root.avlName.root = root.avlName._insert_name(root.avlName.root, song.get_track_name(), song)

        return self._rebalance(root)
    
    def _insert_name(self, root, firstChar, song):
        if not root:
            new_node = Node(firstChar)
            new_node.list_songs.add(song)
            return new_node
        
        if firstChar < root.key:
            root.left = self._insert_name(root.left, firstChar, song)
        elif firstChar > root.key:
            root.right = self._insert_name(root.right, firstChar, song)
        else:
            root.list_songs.add(song) 

        return self._rebalance(root)

    def insert(self, song):
        if not self.root:
            self.root = Node(float('-inf'))  # Usa un valor adecuado en lugar de None
        self.root = self._insert_year(self.root, song)
    
    def insert_word(self, word, song):
        if not self.root:
            self.root = Node(float('-inf'))  # Usa un valor adecuado en lugar de None
        firstChar = word[0].lower()
        if not self.root.avlName.root:
            self.root.avlName.root = Node(firstChar)
        self.root.avlName.root = self._insert_name(self.root.avlName.root, firstChar, song)


    #FUNCIONES PARA RECORRER EL AVL DE CADA NODO EN ORDEN ALFABETICO
    def _allSongsName(self, root, result):
        if not root:
            return
        self._allSongsName(root.left, result)
        for song in root.list_songs:
            result.add(song)
        self._allSongsName(root.right, result)

    def allSongsName(self):
        result = LinkedList()
        self._allSongsName(self.root, result)
        return result


    #FUNCIONES PARA OBTENER UNA LISTA ORDENADA
    def _in_order_ascending(self, root, result):
        if not root:
            return
        self._in_order_ascending(root.left, result)
        for song in root.avlName.allSongsName():
            result.add(song)
        self._in_order_ascending(root.right, result)

    def ascending(self):
        result = LinkedList()
        self._in_order_ascending(self.root, result)
        return result

    def _in_order_descending(self, root, result):
        if not root:
            return
        self._in_order_descending(root.right, result)
        for song in root.avlName.allSongsName():
            result.add(song)
        self._in_order_descending(root.left, result)

    def descending(self):
        result = LinkedList()
        self._in_order_descending(self.root, result)
        return result


    #FUNCIONES PARA HALLAR UNA CANCIÓN ESPECIFICADA POR AÑO
    def _find(self, root, year):
        if not root:
            return None
        if root.key == year:
            return root
        elif year < root.key:
            return self._find(root.left, year)
        else:
            return self._find(root.right, year)

    def specifiedYear(self, year):
        node = self._find(self.root, year)
        if node:
            return node.avlName.allSongsName()
        else:
            return LinkedList()