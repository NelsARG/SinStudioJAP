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


