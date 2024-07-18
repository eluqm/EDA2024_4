class BTreeNode:
    def __init__(self, t, leaf=False):
        self.t = t  # Grado mínimo
        self.leaf = leaf  # Verdadero si el nodo es una hoja
        self.keys = []  # Lista de claves en el nodo
        self.children = []  # Lista de hijos del nodo

class BTree:
    def __init__(self, t):
        self.root = BTreeNode(t, True)  # Inicializa el árbol con una raíz vacía
        self.t = t  # Grado mínimo

    def search(self, k, node=None):
        if node is None:
            node = self.root
        i = 0
        while i < len(node.keys) and k > node.keys[i]:
            i += 1
        if i < len(node.keys) and k == node.keys[i]:
            return (node, i)
        if node.leaf:
            return None
        else:
            return self.search(k, node.children[i])

