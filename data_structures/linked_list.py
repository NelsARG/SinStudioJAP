from data_structures.node import Node


class LinkedList:
    # Estrategia de lista enlazada para gestionar archivos
    def __init__(self):
        self.head = None
        self.size = 0

    def is_empty(self):
        #Retorna True si la lista no contiene elementos
        return self.head is None

    def append(self, data):
        #inserta un nuevo nodo al final de la lista
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1

    def find_by_name(self, filename):
        #Busca y retorna el elemento cuyo nombre coincida
        current = self.head
        while current:
            #Asumimos que los datos almacenados tienen la propiedad 'filename'
            if hasattr(current.data, 'filename') and current.data.filename == filename:
                return current.data
            current = current.next
        return None

    def delete_by_name(self, filename):
        #Elimina un nodo por el nombre del archivo liberando la referencia
        if self.is_empty():
            return False

        if hasattr(self.head.data, 'filename') and self.head.data.filename == filename:
            self.head = self.head.next
            self.size -= 1
            return True

        current = self.head
        while current.next:
            if hasattr(current.next.data, 'filename') and current.next.data.filename == filename:
                current.next = current.next.next
                self.size -= 1
                return True
            current = current.next

        return False

    def get_all(self):
        #Retorna un generador con todos los elementos de la lista
        current = self.head
        while current:
            yield current.data
            current = current.next
