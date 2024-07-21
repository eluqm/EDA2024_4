class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
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
    
    def _insert(self, root, key):
        if not root:
            return Node(key)
        
        if key < root.key:
            root.left = self._insert(root.left, key)
        else:
            root.right = self._insert(root.right, key)
        
        return self._rebalance(root)

    def insert(self, key):
        if not hasattr(self, 'root'):
            self.root = None
        self.root = self._insert(self.root, key)

    def _in_order(self, root, result):
        if not root:
            return
        self._in_order(root.left, result)
        result.append(root.key)
        self._in_order(root.right, result)

    def in_order(self):
        result = []
        self._in_order(self.root, result)
        return result