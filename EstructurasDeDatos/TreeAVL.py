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

    def balance_factor(self, node):
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