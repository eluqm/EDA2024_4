from .LinkedList import LinkedList
class BTreeNode:
    def __init__(self, t, leaf=False):
        self.t = t  # Grado mínimo
        self.leaf = leaf  # Verdadero si el nodo es una hoja
        self.keys = []  # Lista de claves en el nodo
        self.children = []  # Lista de hijos del nodos
        self.song_lists = []  # Lista de LinkedLists de canciones
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

    def insert(self, k, song):
        root = self.root
        if len(root.keys) == 2 * self.t - 1:
            temp = BTreeNode(self.t)
            self.root = temp
            temp.children.insert(0, root)
            self.split_child(temp, 0)
            self.insert_non_full(temp, k, song)
        else:
            self.insert_non_full(root, k, song)

    def split_child(self, parent, i):
        t = self.t
        node = parent.children[i]
        new_node = BTreeNode(t, node.leaf)
        parent.children.insert(i + 1, new_node)
        parent.keys.insert(i, node.keys[t - 1])
        parent.song_lists.insert(i, node.song_lists[t - 1])
        new_node.keys = node.keys[t:(2 * t - 1)]
        new_node.song_lists = node.song_lists[t:(2 * t - 1)]
        node.keys = node.keys[0:(t - 1)]
        node.song_lists = node.song_lists[0:(t - 1)]
        if not node.leaf:
            new_node.children = node.children[t:(2 * t)]
            node.children = node.children[0:t]

    def insert_non_full(self, node, k, song):
        i = len(node.keys) - 1
        if node.leaf:
            while i >= 0 and k < node.keys[i]:
                i -= 1
            if i >= 0 and k == node.keys[i]:
                node.song_lists[i].add(song)
            else:
                node.keys.insert(i + 1, k)
                song_list = LinkedList()
                song_list.add(song)
                node.song_lists.insert(i + 1, song_list)
        else:
            while i >= 0 and k < node.keys[i]:
                i -= 1
            i += 1
            if len(node.children[i].keys) == 2 * self.t - 1:
                self.split_child(node, i)
                if k > node.keys[i]:
                    i += 1
            self.insert_non_full(node.children[i], k, song)

    def print_tree(self, node=None, level=0):
        if node is None:
            node = self.root
        print("Level", level, " ", len(node.keys), ":", node.keys)
        level += 1
        for child in node.children:
            self.print_tree(child, level)