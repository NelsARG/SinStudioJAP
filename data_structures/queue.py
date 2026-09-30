from data_structures.node import Node


class Queue:
    # Estructura FIFO para el buffer de peticiones a la IA
    def __init__(self):
        self.front_node = None
        self.rear_node = None
        self.size = 0

    def is_empty(self):
        #Retorna true si la cola no contiene elementos
        return self.front_node is None

    def enqueue(self, data):
        #Encola un nuevo elemento al final de la cola
        new_node = Node(data)
        if self.is_empty():
            self.front_node = new_node
            self.rear_node = new_node
        else:
            self.rear_node.next = new_node
            self.rear_node = new_node
        self.size += 1

    def dequeue(self):
        #Desencola y retorna el elemento al frente de la cola
        if self.is_empty():
            return None
        dequeued_data = self.front_node.data
        self.front_node = self.front_node.next
        if self.front_node is None:
            self.rear_node = None
        self.size -= 1
        return dequeued_data

    def peek(self):
        #Retorna el elemento al frente sin removerlo
        if self.is_empty():
            return None
        return self.front_node.data
