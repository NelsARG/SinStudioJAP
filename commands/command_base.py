from abc import ABC, abstractmethod


class Command(ABC):
    # Interfaz abstracta base para la implementacion del Patron Command
    @abstractmethod
    def execute(self, *args):
        # Metodo abstracto que debe ser implementado por cada comando concreto
        pass


class CommandInvoker:
    # Invocador que registra y ejecuta comandos mediante mapeo de cadenas
    def __init__(self):
        self._commands = {}

    def register_command(self, command_name, command_obj):
        # Registra un comando asociandolo a una palabra clave
        self._commands[command_name] = command_obj

    def execute_command(self, command_name, *args):
        # Ejecuta el comando registrado correspondiente
        if command_name not in self._commands:
            return False, f"Comando '{command_name}' no reconocido. Digite 'help' para ver los comandos disponibles."
        
        return self._commands[command_name].execute(*args)

    def get_registered_commands(self):
        # Retorna la lista de comandos disponibles
        return list(self._commands.keys())
