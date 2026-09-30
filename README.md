Documentación para cada archivo, explicación breve de lo ue son

data_structures node.py
Implementa la clase Node para la construccion de nodos simples y dobles utilizados en estructuras enlazadas.

data_structures linked_list.py
Implementa la estructura LinkedList para la administracion dinamica de archivos abiertos en la sesion de memoria.

data_structures stack.py
Implementa la estructura Stack para el control LIFO del validador sintactico y del historial Undo y Redo.

data_structures queue.py
Implementa la estructura Queue para la cola FIFO de solicitudes hacia la API de inteligencia artificial.

data_structures binary_tree.py
Implementa la estructura BinaryTree para la organizacion jerarquica del proyecto.

# Modulos de Logica Core

core file_manager.py
Administra los archivos abiertos en la sesion mediante la lista enlazada LinkedList.

core syntax_validator.py
Valida el balanceo de delimitadores agrupadores en el codigo activo utilizando la pila Stack.

core history_manager.py
Controla el historial de cambios del archivo activo utilizando dos pilas Stack independientes para las operaciones Undo y Redo.

core sorting_engine.py
Implementa los algoritmos Mergesort y Shellsort desde cero para ordenar los reportes de diagnostico por numero de linea.

core ia_manager.py
Gestiona la cola FIFO de peticiones de analisis hacia la API externa y simula la evaluacion de complejidad algoritmica.

core config_loader.py
Carga la configuracion externa del entorno y la clave API key desde el archivo config.json garantizando seguridad.

# Patrones de Diseño y Capa de Comandos

El proyecto implementa el Patron de Diseno Command para evitar el uso de menus CLI tradicionales basados en opciones numericas.

commands command_base.py
Define la interfaz abstracta Command y la clase CommandInvoker encargada de registrar y despachar las acciones del usuario.

commands concrete_commands.py
Implementa los comandos concretos para crear archivos, listar, cambiar de archivo activo, editar codigo, validar sintaxis, deshacer, rehacer, encolar peticiones de IA, procesar la cola y ordenar diagnosticos.


# Comandos Disponibles en la CLI

create
Crea un nuevo archivo en memoria.
Ejemplo: create index.py print("Hola")

list
Muestra la lista de todos los archivos abiertos en la sesion.

switch
Cambia el archivo activo actual.
Ejemplo: switch index.py

write
Escribe o actualiza el texto en el archivo activo actual.
Ejemplo: write print("Nuevo codigo")

check
Valida la sintaxis de los delimitadores en el archivo activo.

undo
Deshace la ultima modificacion realizada en el archivo activo.

redo
Rehace la ultima modificacion deshecha en el archivo activo.

analyze
Encola el archivo activo en la cola FIFO para analisis de la IA.

process
Despacha y procesa la siguiente peticion en la cola FIFO de la IA.

sort
Ordena los diagnosticos de codigo utilizando mergesort o shellsort.
Ejemplo: sort mergesort

help
Muestra la lista de comandos disponibles en pantalla.

exit
Cierra la aplicacion Synthetix Studio.
