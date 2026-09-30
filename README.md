# Synthetix Studio - Mini IDE CLI

#Descripción del Proyecto
Synthetix Studio es un entorno de desarrollo minimalista basado en línea de comandos desarrollado en Python bajo el paradigma de 
Programación Orientada a Objetos. El sistema integra estructuras de datos lineales y no lineales desarrolladas desde cero, un motor de ordenamiento propio, validación de sintaxis, historial de cambios y procesamiento encolado de análisis 
de código mediante una API de IA

---

#Estructuras de Datos e Implementación 
En cumplimiento estricto con los requerimientos del proyecto, no se utilizaron estructuras o métodos nativos de Python:

- Lista Enlazada (LinkedList): Gestiona los archivos de código abiertos en la sesión en memoria.
- Pila (Stack):
  - Validación de balanceo de símbolos de agrupación (`()`, `{}`, `[]`).
  - Sistema de historial de cambios mediante dos pilas independientes (`Undo` / `Redo`).
- Cola FIFO (Queue): Buffer de peticiones para administrar y despachar de forma secuencial las solicitudes hacia la API de IA.
- Árbol Binario (BinaryTree): Estructura jerárquica con recorridos Preorden, Inorden y Postorden, además de la lógica para serializar y deserializar datos.
- Algoritmos de Ordenamiento: Implementación desde cero de Mergesort y/o Shellsor para ordenar alertas y diagnósticos por número de línea o severidad.

---


## Requisitos de Ejecución

### Pre-requisitos
- Python 3.8 o superior instalado.


Autor
Nombre: Nelson Rodriguez
