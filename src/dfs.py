""""
===========================================================================
UNIVERSIDAD NACIONAL AUTÓNOMA DE MÉXICO (UNAM)
Facultad de Ciencias
Materia: Inteligencia Artificial
Docente: Dra. Jessica Sarahí Mendez Rincon
Ayduante de Laboratorio: Diego Eduardo Peña Villegas
Alumno: Erick Luis Juárez
Año escolar: 2026-2
Copyright (c) 2025 UNAM - MIT License
Version: 1.0
This software is for educational purposes.
The accuracy of the models depends strictly on the quality
and preocessing of the input data.
-----------------------------------------------------------------
UNAM IA Library: A professional toolkit for AI develped at UNAM.
============================================================================
"""

import time

def dfs(grafo, nodo, visitados=None):
    """
    Implementación del algoritmo Depth-First Search (DFS).

    Parámetros:
    grafo: diccionario que representa el grafo (lista de adyacencia)
    nodo: nodo inicial desde donde comienza la búsqueda
    visitados: conjunto de nodos ya visitados

    Retorna:
    conjunto de nodos visitados
    """

    if visitados is None: #Si no hay ningun nodo visitado, se crea el conjunto de nodos visitados
        visitados = set()

    # Marcar nodo como visitado
    visitados.add(nodo)
    print(nodo, end=" ")

    #Explora vecinos
    for vecino in grafo.get(nodo, []):
        if vecino not in visitados:
            dfs(grafo, vecino, visitados) #Se llama recursivamente dfs haciendo bactraking para explorar profundamente

    return visitados #Devuelve le conunto de nodos visitados en orden


# Ejemplo de grafo
grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

inicio_tiempo = time.time()

print("Recorrido DFS:")
dfs(grafo, 'A')

fin_tiempo = time.time()

print("\n")
print("Tiempo de ejecución:", fin_tiempo - inicio_tiempo, "segundos")
