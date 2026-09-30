from data_structures.stack import Stack


class HistoryManager:
    #Sistema de control de cambios basado en dos pilas independientes (Undo y Redo)
    def __init__(self):
        self.undo_stack = Stack()
        self.redo_stack = Stack()

    def record_state(self, current_content):
        #guarda un nuevo estado en la pila Undo y limpia la pila Redo
        self.undo_stack.push(current_content)
        self.redo_stack.clear()

    def undo(self, active_content):
        #Deshace la ultima modificacion restaurando el estado previo
        if self.undo_stack.is_empty():
            return False, "No hay cambios para deshacer.", active_content

        #Apilamos el estado actual en Redo antes de retroceder
        self.redo_stack.push(active_content)
        previous_content = self.undo_stack.pop()
        return True, "Cambio deshecho (Undo exitoso).", previous_content

    def redo(self, active_content):
        #Rehace el ultimo cambio previamente deshecho
        if self.redo_stack.is_empty():
            return False, "No hay cambios para rehacer.", active_content

        #Apilamos el estado actual en Undo antes de avanzar
        self.undo_stack.push(active_content)
        next_content = self.redo_stack.pop()
        return True, "Cambio rehecho (Redo exitoso).", next_content

    def clear_history(self):
        #vacía el historial de cambios
        self.undo_stack.clear()
        self.redo_stack.clear()
