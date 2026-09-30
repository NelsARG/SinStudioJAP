class Node:
    # Nodo generico para estructuras lineales (LinkedList, Stack y Queue)
    def __init__(self, data=None):
        self.data = data
        self.next = None


class DoubleNode:
    # Nodo para estructuras doblemente enlazadas
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None


class TreeNode:
    # Nodo para el Arbol Binario con punteros a hijo izquierdo y derecho
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
