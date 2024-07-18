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
    
    def insert(self, k):
        root = self.root
        if len(root.keys) == 2 * self.t - 1:
            temp = BTreeNode(self.t)
            self.root = temp
            temp.children.insert(0, root)
            self.split_child(temp, 0)
            self.insert_non_full(temp, k)
        else:
            self.insert_non_full(root, k)

    def split_child(self, parent, i):
        t = self.t
        node = parent.children[i]
        new_node = BTreeNode(t, node.leaf)
        parent.children.insert(i + 1, new_node)
        parent.keys.insert(i, node.keys[t - 1])
        new_node.keys = node.keys[t:(2 * t - 1)]
        node.keys = node.keys[0:(t - 1)]
        if not node.leaf:
            new_node.children = node.children[t:(2 * t)]
            node.children = node.children[0:t]