from .LinkedList import LinkedList

class BTreeNode:
    def __init__(self, t, leaf=False):
        self.t = t  # Grado mínimo
        self.leaf = leaf  # Verdadero si el nodo es una hoja
        self.keys = LinkedList()  # LinkedList de claves en el nodo
        self.children = LinkedList()  # LinkedList de hijos del nodo
        self.song_lists = LinkedList()  # LinkedList de LinkedLists de canciones

class BTree:
    def __init__(self, t):
        self.root = BTreeNode(t, True)  # Inicializa el árbol con una raíz vacía
        self.t = t  # Grado mínimo

    def search(self, k, node=None):
        if node is None:
            node = self.root
        i = 0
        current_key = node.keys.head
        while current_key and k > current_key.data:
            i += 1
            current_key = current_key.next
        if current_key and k == current_key.data:
            return (node, i)
        if node.leaf:
            return None
        else:
            return self.search(k, node.children.get(i))

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
        node = parent.children.get(i)
        new_node = BTreeNode(t, node.leaf)
        parent.children.insert(i + 1, new_node)
        parent.keys.insert(i, node.keys.get(t - 1))
        parent.song_lists.insert(i, node.song_lists.get(t - 1))
        new_node_keys = LinkedList()
        new_node_song_lists = LinkedList()
        for j in range(t, 2 * t - 1):
            new_node_keys.add(node.keys.get(j))
            new_node_song_lists.add(node.song_lists.get(j))
        new_node.keys = new_node_keys
        new_node.song_lists = new_node_song_lists
        node_keys = LinkedList()
        node_song_lists = LinkedList()
        for j in range(t - 1):
            node_keys.add(node.keys.get(j))
            node_song_lists.add(node.song_lists.get(j))
        node.keys = node_keys
        node.song_lists = node_song_lists
        if not node.leaf:
            new_node_children = LinkedList()
            for j in range(t, 2 * t):
                new_node_children.add(node.children.get(j))
            new_node.children = new_node_children
            node_children = LinkedList()
            for j in range(t):
                node_children.add(node.children.get(j))
            node.children = node_children

    def insert_non_full(self, node, k, song):
        i = len(node.keys) - 1
        if node.leaf:
            while i >= 0 and k < node.keys.get(i):
                i -= 1
            if i >= 0 and k == node.keys.get(i):
                node.song_lists.get(i).add(song)
            else:
                node.keys.insert(i + 1, k)
                song_list = LinkedList()
                song_list.add(song)
                node.song_lists.insert(i + 1, song_list)
        else:
            while i >= 0 and k < node.keys.get(i):
                i -= 1
            i += 1
            if len(node.children.get(i).keys) == 2 * self.t - 1:
                self.split_child(node, i)
                if k > node.keys.get(i):
                    i += 1
            self.insert_non_full(node.children.get(i), k, song)

    def print_tree(self, node=None, level=0):
        if node is None:
            node = self.root
        print("Level", level, " ", len(node.keys), ":", [key for key in node.keys])
        level += 1
        for child in node.children:
            self.print_tree(child, level)
            
    def in_orden(self, node=None):
        if node is None:
            node = self.root
        result = LinkedList()
        i = 0
        while i < len(node.keys):
            if not node.leaf:
                result.extend(self.in_orden(node.children.get(i)))
            song_list = node.song_lists.get(i).to_list()
            result.extend(song_list)
            i += 1
        if not node.leaf:
            result.extend(self.in_orden(node.children.get(i)))
        return result

    def ascending(self):
        songs = self.in_orden()
        return songs

    def in_orden_reverse(self, node=None):
        if node is None:
            node = self.root
        result = LinkedList()
        i = len(node.keys) - 1
        while i >= 0:
            if not node.leaf:
                result.extend(self.in_orden_reverse(node.children.get(i + 1)))
            song_list = node.song_lists.get(i).to_list()
            result.extend(song_list)
            i -= 1
        if not node.leaf:
            result.extend(self.in_orden_reverse(node.children.get(0)))
        return result

    def descending(self):
        songs = self.in_orden_reverse()
        return songs
    
    def clear(self):
        self.root = BTreeNode(self.t, True)  # Reinicializa el árbol con una nueva raíz vacía
