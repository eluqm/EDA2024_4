from .LinkedList import LinkedList  
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1
        self.list_songs = LinkedList()

class AVLTree:
    def __init__(self):
        self.root = None

    # Obtiene la altura de un nodo
    def _height(self, root):
        if not root:
            return 0
        return root.height
    
    # Actualiza la altura de un nodo
    def _update_height(self, node):
        node.height = 1 + max(self._height(node.left), self._height(node.right))

    # Calcula el factor de balanceo de un nodo
    def _balance_factor(self, node):
        if not node:
            return 0
        return self._height(node.left) - self._height(node.right)
    
    # Rotación hacia la derecha
    def _rotate_right(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        self._update_height(y)
        self._update_height(x)
        return x
    
    # Rotación hacia la izquierda
    def _rotate_left(self, x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        self._update_height(x)
        self._update_height(y)
        return y
    
    # Rebalancea un nodo
    def _rebalance(self, node):
        self._update_height(node)
        balance = self._balance_factor(node)
        
        # Si está desbalanceado hacia la izquierda
        if balance > 1:
            if self._balance_factor(node.left) < 0:
                node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        
        # Si está desbalanceado hacia la derecha
        if balance < -1:
            if self._balance_factor(node.right) > 0:
                node.right = self._rotate_right(node.right)
            return self._rotate_left(node)
        
        return node
    
    # Inserta un nodo en el árbol
    def _insert(self, root, year, song):
        if not root:
            new_node = Node(year)
            new_node.list_songs.add(song)  # Añadir la canción a la LinkedList
            return new_node
        
        if year < root.key:
            root.left = self._insert(root.left, year, song)
        elif year > root.key:
            root.right = self._insert(root.right, year, song)
        else:
            root.list_songs.add(song)  

        return self._rebalance(root)

    # Función pública para insertar un nodo
    def insert(self, year, song):
        if not hasattr(self, 'root'):
            self.root = None
        self.root = self._insert(self.root, year, song)

    # Recorre el árbol en orden y guarda las claves en una lista
    def _in_order(self, root, result):
        if not root:
            return
        self._in_order(root.left, result)
        songs = list(root.list_songs) 
        result.append((root.key, songs))
        self._in_order(root.right, result)

    # Función pública para obtener el recorrido en orden del árbol
    def in_order(self):
        result = []
        self._in_order(self.root, result)
        return result
    
    # Funciones para devolver una lista en fprma descendete o ascendente
    def _in_order_ascending(self, root, result):
        if not root:
            return
        self._in_order_ascending(root.left, result)
        for song in root.list_songs:
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
        for song in root.list_songs:
            result.add(song)
        self._in_order_descending(root.left, result)

    def descending(self):
        result = LinkedList()
        self._in_order_descending(self.root, result)
        return result