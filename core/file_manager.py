from data_structures.linked_list import LinkedList


class CodeFile:
    # Representa un archivo de codigo guardado en memoria
    def __init__(self, filename, content=""):
        self.filename = filename
        self.content = content


class FileManager:
    # Administra los archivos abiertos en la sesion mediante LinkedList
    def __init__(self):
        self.files_list = LinkedList()
        self.active_file = None

    def create_file(self, filename, initial_content=""):
        # Crea un nuevo archivo en memoria y lo establece como activo
        existing = self.files_list.find_by_name(filename)
        if existing:
            return False, f"El archivo '{filename}' ya existe."

        new_file = CodeFile(filename, initial_content)
        self.files_list.append(new_file)
        self.active_file = new_file
        return True, f"Archivo '{filename}' creado correctamente."

    def list_files(self):
        # Retorna la lista de todos los archivos abiertos y su estado
        if self.files_list.is_empty():
            return []

        files_info = []
        for file_obj in self.files_list.get_all():
            is_active = (self.active_file and file_obj.filename == self.active_file.filename)
            files_info.append({
                "filename": file_obj.filename,
                "is_active": is_active
            })
        return files_info

    def switch_file(self, filename):
        # Cambia el archivo activo actual
        target_file = self.files_list.find_by_name(filename)
        if target_file:
            self.active_file = target_file
            return True, f"Cambiado al archivo '{filename}'."
        return False, f"El archivo '{filename}' no fue encontrado."

    def delete_file(self, filename):
        # Elimina un archivo de la lista liberando sus referencias
        deleted = self.files_list.delete_by_name(filename)
        if deleted:
            if self.active_file and self.active_file.filename == filename:
                self.active_file = None
            return True, f"Archivo '{filename}' eliminado correctamente."
        return False, f"El archivo '{filename}' no fue encontrado."
