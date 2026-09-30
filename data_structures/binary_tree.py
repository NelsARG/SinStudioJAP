from data_structures.node import TreeNode


class BinaryTree:
    #Estructura de Arbol Binario con serializacion y recorridos
    def __init__(self):
        self.root = None

    def is_empty(self):
        #retorna true si el arbol esta vacio
        return self.root is None

    def insert(self, data):
        #Inserta un dato en el arbol manteniendo la propiedad binaria
        new_node = TreeNode(data)
        if self.is_empty():
            self.root = new_node
            return

        queue = [self.root]
        while queue:
            current = queue.pop(0)
            if current.left is None:
                current.left = new_node
                break
            else:
                queue.append(current.left)

            if current.right is None:
                current.right = new_node
                break
            else:
                queue.append(current.right)

    def preorder(self, node_actual):
        # Recorrido Preorden
        res = []
        if node_actual is not None:
            res.append(node_actual.data)
            res.extend(self.preorder(node_actual.left))
            res.extend(self.preorder(node_actual.right))
        return res

    def inorder(self, node_actual):
        #Recorrido Inorden
        res = []
        if node_actual is not None:
            res.extend(self.inorder(node_actual.left))
            res.append(node_actual.data)
            res.extend(self.inorder(node_actual.right))
        return res

    def postorder(self, node_actual):
        #Recorrido Postorden
        res = []
        if node_actual is not None:
            res.extend(self.postorder(node_actual.left))
            res.extend(self.postorder(node_actual.right))
            res.append(node_actual.data)
        return res

    def serialize(self, node_actual):
        #Codificar datos:convierte la estructura en un formato representable
        if node_actual is None:
            return "NULL"
        return f"{node_actual.data},{self.serialize(node_actual.left)},{self.serialize(node_actual.right)}"

    def deserialize(self, data_string):
        #decodificar datos: reconstruye el arbol a partir de una cadena codificada
        nodes = data_string.split(",")

        def build_tree():
            if not nodes:
                return None
            val = nodes.pop(0)
            if val == "NULL":
                return None
            node = TreeNode(val)
            node.left = build_tree()
            node.right = build_tree()
            return node

        self.root = build_tree()
        return self.root
