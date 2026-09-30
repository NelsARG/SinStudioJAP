from commands.command_base import Command


class CreateFileCommand(Command):
    #comando para crear un nuevo archivo de codigo en memoria
    def __init__(self, file_manager, history_manager):
        self.file_manager = file_manager
        self.history_manager = history_manager

    def execute(self, *args):
        if not args or not args[0]:
            return False, "Error: Debe especificar un nombre para el archivo."
        filename = args[0]
        initial_content = args[1] if len(args) > 1 else ""
        
        success, msg = self.file_manager.create_file(filename, initial_content)
        if success:
            self.history_manager.clear_history()
            self.history_manager.record_state(initial_content)
        return success, msg


class ListFilesCommand(Command):
    #Comando para listar todos los archivos cargados
    def __init__(self, file_manager):
        self.file_manager = file_manager

    def execute(self, *args):
        files = self.file_manager.list_files()
        if not files:
            return True, "No hay archivos abiertos en memoria."
        
        result = "Archivos cargados:\n"
        for f in files:
            status = " (Activo)" if f["is_active"] else ""
            result += f" - {f['filename']}{status}\n"
        return True, result.strip()


class SwitchFileCommand(Command):
    #Comando para cambiar el archivo activo actual
    def __init__(self, file_manager, history_manager):
        self.file_manager = file_manager
        self.history_manager = history_manager

    def execute(self, *args):
        if not args or not args[0]:
            return False, "Error: Debe especificar el nombre del archivo activo."
        filename = args[0]
        
        success, msg = self.file_manager.switch_file(filename)
        if success and self.file_manager.active_file:
            self.history_manager.clear_history()
            self.history_manager.record_state(self.file_manager.active_file.content)
        return success, msg


class WriteCodeCommand(Command):
    #comando para sobreescribir o anexar contenido al archivo activo
    def __init__(self, file_manager, history_manager):
        self.file_manager = file_manager
        self.history_manager = history_manager

    def execute(self, *args):
        if not self.file_manager.active_file:
            return False, "Error: No hay ningun archivo activo seleccionado."
        if not args or not args[0]:
            return False, "Error: Debe proporcionar el contenido a escribir."
        
        new_content = args[0]
        self.file_manager.active_file.content = new_content
        self.history_manager.record_state(new_content)
        return True, f"Contenido actualizado en '{self.file_manager.active_file.filename}'."


class CheckSyntaxCommand(Command):
    #comando para validar delimitadores mediante Pila
    def __init__(self, file_manager, syntax_validator):
        self.file_manager = file_manager
        self.syntax_validator = syntax_validator

    def execute(self, *args):
        if not self.file_manager.active_file:
            return False, "Error: No hay ningun archivo activo para validar."
        
        code = self.file_manager.active_file.content
        return self.syntax_validator.validate(code)


class UndoCommand(Command):
    #Comando para deshacer modificaciones en el archivo activo
    def __init__(self, file_manager, history_manager):
        self.file_manager = file_manager
        self.history_manager = history_manager

    def execute(self, *args):
        if not self.file_manager.active_file:
            return False, "Error: No hay un archivo activo para deshacer cambios."
        
        current_content = self.file_manager.active_file.content
        success, msg, prev_content = self.history_manager.undo(current_content)
        if success:
            self.file_manager.active_file.content = prev_content
        return success, msg


class RedoCommand(Command):
    #Comando para rehacer modificaciones previamente deshechas
    def __init__(self, file_manager, history_manager):
        self.file_manager = file_manager
        self.history_manager = history_manager

    def execute(self, *args):
        if not self.file_manager.active_file:
            return False, "Error: No hay un archivo activo para rehacer cambios."
        
        current_content = self.file_manager.active_file.content
        success, msg, next_content = self.history_manager.redo(current_content)
        if success:
            self.file_manager.active_file.content = next_content
        return success, msg


class AnalyzeIACommand(Command):
    # comando para encolar la peticion de analisis hacia la IA
    def __init__(self, file_manager, ia_manager):
        self.file_manager = file_manager
        self.ia_manager = ia_manager

    def execute(self, *args):
        if not self.file_manager.active_file:
            return False, "Error: No hay un archivo activo para analizar."
        
        filename = self.file_manager.active_file.filename
        content = self.file_manager.active_file.content
        return self.ia_manager.enqueue_request(filename, content)


class ProcessIACommand(Command):
    #comando para procesar la siguiente peticion en la cola FIFO de la IA
    def __init__(self, ia_manager):
        self.ia_manager = ia_manager

    def execute(self, *args):
        success, msg, result = self.ia_manager.process_next_request()
        if not success:
            return False, msg
        
        output = f"{msg}\n"
        output += f" - Complejidad estimada: {result['complexity']}\n"
        output += f" - Sugerencia: {result['refactoring_suggestion']}\n"
        output += f" - Endpoint: {result['endpoint_used']}\n"
        output += f" - API Key configurada: {'Si' if result['key_configured'] else 'No'}"
        return True, output


class SortDiagnosticsCommand(Command):
    #Comando para ordenar diagnosticos ficticios con Mergesort o Shellsort
    def __init__(self, sorting_engine):
        self.sorting_engine = sorting_engine

    def execute(self, *args):
        #muestra de diagnosticos para simular la ordenacion
        sample_diagnostics = [
            {"line": 15, "severity": "Warning", "msg": "Variable sin usar"},
            {"line": 3, "severity": "Error", "msg": "Error de delimitador"},
            {"line": 42, "severity": "Info", "msg": "Comentario detectado"},
            {"line": 8, "severity": "Error", "msg": "Indentacion invalida"}
        ]
        
        algorithm = args[0] if args and args[0] in ["mergesort", "shellsort"] else "mergesort"
        
        if algorithm == "mergesort":
            sorted_list = self.sorting_engine.mergesort(sample_diagnostics, key_func=lambda x: x["line"])
        else:
            sorted_list = self.sorting_engine.shellsort(sample_diagnostics, key_func=lambda x: x["line"])
            
        output = f"Diagnosticos ordenados por linea ({algorithm}):\n"
        for item in sorted_list:
            output += f" - Linea {item['line']} [{item['severity']}]: {item['msg']}\n"
        return True, output.strip()
