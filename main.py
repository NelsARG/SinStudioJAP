import sys
from core.config_loader import ConfigLoader
from core.file_manager import FileManager
from core.syntax_validator import SyntaxValidator
from core.history_manager import HistoryManager
from core.sorting_engine import SortingEngine
from core.ia_manager import IAManager
from commands.command_base import CommandInvoker
from commands.concrete_commands import (
    CreateFileCommand,
    ListFilesCommand,
    SwitchFileCommand,
    WriteCodeCommand,
    CheckSyntaxCommand,
    UndoCommand,
    RedoCommand,
    AnalyzeIACommand,
    ProcessIACommand,
    SortDiagnosticsCommand
)


def print_help():
    # Muestra los comandos disponibles en el CLI
    help_text = """
======================================================================
                     SYNTHETIX STUDIO CLI MINI IDE
======================================================================
Comandos de Archivos:
  create <nombre> [contenido]  Crea un nuevo archivo en memoria
  list                         Lista todos los archivos abiertos
  switch <nombre>              Cambia el archivo activo actual
  write <texto>                Escribe o actualiza texto en el archivo activo

Comandos de Analisis y Edicion:
  check                        Valida delimitadores ({[],()}) con Pila LIFO
  undo                         Deshace la ultima modificacion (Undo)
  redo                         Rehace la ultima modificacion deshecha (Redo)

Comandos de Inteligencia Artificial (Buffer FIFO):
  analyze                      Encola el archivo activo en la cola FIFO de IA
  process                      Procesa la siguiente peticion encolada

Comandos de Utilidad:
  sort [mergesort|shellsort]   Ordena diagnosticos simulados por numero de linea
  help                         Muestra este mensaje de ayuda
  exit                         Cierra Synthetix Studio
======================================================================
"""
    print(help_text.strip())


def main():
    # Inicializacion de configuracion
    config = ConfigLoader("config.json")
    
    # Inicializacion del nucleo (Core)
    file_mgr = FileManager()
    syntax_val = SyntaxValidator()
    history_mgr = HistoryManager()
    sort_engine = SortingEngine()
    ia_mgr = IAManager(
        api_endpoint=config.get("api_endpoint"),
        api_key=config.get("api_key")
    )

    # Registro de comandos en el CommandInvoker
    invoker = CommandInvoker()
    invoker.register_command("create", CreateFileCommand(file_mgr, history_mgr))
    invoker.register_command("list", ListFilesCommand(file_mgr))
    invoker.register_command("switch", SwitchFileCommand(file_mgr, history_mgr))
    invoker.register_command("write", WriteCodeCommand(file_mgr, history_mgr))
    invoker.register_command("check", CheckSyntaxCommand(file_mgr, syntax_val))
    invoker.register_command("undo", UndoCommand(file_mgr, history_mgr))
    invoker.register_command("redo", RedoCommand(file_mgr, history_mgr))
    invoker.register_command("analyze", AnalyzeIACommand(file_mgr, ia_mgr))
    invoker.register_command("process", ProcessIACommand(ia_mgr))
    invoker.register_command("sort", SortDiagnosticsCommand(sort_engine))

    print("Bienvenido a Synthetix Studio CLI Mini IDE.")
    print("Digite 'help' para ver los comandos disponibles o 'exit' para salir.\n")

    # Bucle REPL principal
    while True:
        try:
            active_name = file_mgr.active_file.filename if file_mgr.active_file else "ninguno"
            user_input = input(f"SynthetixStudio [{active_name}]> ").strip()

            if not user_input:
                continue

            parts = user_input.split(" ", 1)
            cmd_name = parts[0].lower()
            cmd_args = parts[1] if len(parts) > 1 else ""

            if cmd_name == "exit":
                print("Saliendo de Synthetix Studio. ¡Hasta pronto!")
                sys.exit(0)

            if cmd_name == "help":
                print_help()
                continue

            # Ejecucion mediante Command Pattern
            if cmd_args:
                success, response = invoker.execute_command(cmd_name, cmd_args)
            else:
                success, response = invoker.execute_command(cmd_name)

            print(response)
            print()

        except (KeyboardInterrupt, EOFError):
            print("\nSaliendo de Synthetix Studio. Hasta pronto!")
            sys.exit(0)


if __name__ == "__main__":
    main()

