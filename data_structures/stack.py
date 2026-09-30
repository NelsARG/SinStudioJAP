from data_structures.node import Node


class Stack:
    #estructura LIFO para sintaxis e historial
    def __init__(self):
        self.top_node = None
        self.size = 0

    def is_empty(self):
        #Retorna true si la pila esta vacia
        return self.top_node is None

    def push(self, data):
        #Apila un nuevo elemento en la parte superior
        new_node = Node(data)
        new_node.next = self.top_node
        self.top_node = new_node
        self.size += 1

    def pop(self):
        #Desapila y retorna el elemento superior
        if self.is_empty():
            return None
        popped_data = self.top_node.data
        self.top_node = self.top_node.next
        self.size -= 1
        return popped_data

    def peek(self):
        #Retorna el elemento en la cima sin quitarlo
        if self.is_empty():
            return None
        return self.top_node.data

    def clear(self):
        #vacía la pila
        self.top_node = None
        self.size = 0
