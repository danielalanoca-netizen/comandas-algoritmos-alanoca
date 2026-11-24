# Representación del proceso de inventario de Coffeeology mediante un grafo dirigido.

from collections import deque


# Cada nodo representa una persona o etapa del proceso.
nodos = [
    "Turno de la mañana",
    "Turno de la tarde",
    "Encargado de la noche",
    "Personal de compras",
    "Recepción de materias primas"
]


# Las aristas representan las conexiones entre las etapas.
aristas = [
    ("Turno de la mañana", "Turno de la tarde"),
    ("Turno de la tarde", "Encargado de la noche"),
    ("Encargado de la noche", "Personal de compras"),
    ("Personal de compras", "Recepción de materias primas")
]


# Crear la lista de adyacencia.
grafo = {nodo: [] for nodo in nodos}

for origen, destino in aristas:
    grafo[origen].append(destino)


# Mostrar la lista de adyacencia.
def mostrar_lista_adyacencia():
    print("\nLISTA DE ADYACENCIA\n")

    for nodo, conexiones in grafo.items():
        print(f"{nodo}:")

        for destino in conexiones:
            print(f"  -> {destino}")


# Crear y mostrar la matriz de adyacencia.
def mostrar_matriz_adyacencia():

    # Crear una matriz de ceros.
    cantidad = len(nodos)
    matriz = [[0] * cantidad for _ in range(cantidad)]

    # Colocar un 1 cuando existe una conexión entre dos nodos.
    for origen, destino in aristas:
        fila = nodos.index(origen)
        columna = nodos.index(destino)
        matriz[fila][columna] = 1

    # Mostrar los encabezados de las columnas.
    print("\nMATRIZ DE ADYACENCIA\n")

    print(" " * 12, end="")

    for i in range(cantidad):
        print(f"{i:4}", end="")

    print()

    # Mostrar cada fila de la matriz.
    for i in range(cantidad):
        print(f"{i}: {matriz[i]}")


# Recorrer el grafo utilizando búsqueda en anchura (BFS).
def recorrido_bfs(inicio):

    # Registrar los nodos que ya fueron visitados.
    visitados = set()

    # Crear una cola para controlar el recorrido.
    cola = deque([inicio])

    visitados.add(inicio)

    print("\nRECORRIDO BFS\n")

    # Continuar mientras existan nodos pendientes.
    while cola:

        # Extraer el primer nodo de la cola.
        actual = cola.popleft()

        print(actual)

        # Revisar los vecinos del nodo actual.
        for vecino in grafo[actual]:

            # Agregar a la cola los nodos que todavía no fueron visitados.
            if vecino not in visitados:
                visitados.add(vecino)
                cola.append(vecino)


# Ejecutar todas las funciones.
if __name__ == "__main__":

    mostrar_lista_adyacencia()

    mostrar_matriz_adyacencia()

    recorrido_bfs("Turno de la mañana")