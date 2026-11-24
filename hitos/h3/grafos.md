# Representación del proceso de inventario de COFFEEOLOGY mediante grafos

## 1. Descripción del problema

En COFFEEOLOGY, el control de materias primas se realiza mediante la comunicación entre los diferentes turnos de trabajo.

El proceso comienza cuando el turno de la mañana identifica las materias primas que faltan o tienen poca cantidad. Esta información se comunica al turno de la tarde, que puede identificar otras necesidades y transmitirlas al encargado de la noche.

Posteriormente, el encargado de la noche consolida la información, prepara la lista de compras y la envía al personal de compras mediante WhatsApp. Al día siguiente se reciben las materias primas adquiridas.

Este proceso puede representarse mediante un grafo dirigido, porque las conexiones tienen un sentido determinado: representan cómo se transmite la información de una etapa a otra.

## 2. Identificación de nodos y aristas

Para representar el proceso se identificaron cinco nodos:

| Nodo | Descripción |
|---|---|
| Turno de la mañana | Identifica las materias primas faltantes. |
| Turno de la tarde | Recibe la información y comunica nuevas necesidades. |
| Encargado de la noche | Consolida los requerimientos y prepara la lista de compras. |
| Personal de compras | Recibe la lista y gestiona la compra. |
| Recepción de materias primas | Recibe los productos adquiridos al día siguiente. |

Las aristas representan la comunicación entre las etapas:

1. Turno de la mañana → Turno de la tarde.
2. Turno de la tarde → Encargado de la noche.
3. Encargado de la noche → Personal de compras.
4. Personal de compras → Recepción de materias primas.

Se trata de un grafo dirigido porque las conexiones representan un flujo de información y actividades en una dirección específica.

## 3. Lista de adyacencia

La lista de adyacencia almacena los nodos y sus conexiones. Cada nodo contiene los destinos a los que puede llegar directamente.

**Resultado obtenido al ejecutar el programa:**

```text
FLUJO DEL INVENTARIO DE COFFEEOLOGY

Turno de la mañana:
  -> Turno de la tarde
Turno de la tarde:
  -> Encargado de la noche
Encargado de la noche:
  -> Personal de compras
Personal de compras:
  -> Recepción de materias primas
Recepción de materias primas:
```

La lista muestra que cada etapa se conecta con la siguiente. El nodo de recepción de materias primas no tiene conexiones de salida, porque representa el final del proceso modelado.

## 4. Matriz de adyacencia

La matriz de adyacencia representa las conexiones mediante una tabla de filas y columnas.

- El valor **1** indica que existe una conexión dirigida entre dos nodos.
- El valor **0** indica que no existe una conexión directa.
- Las filas representan el nodo de origen y las columnas el nodo de destino.

Para este ejercicio se utilizó el siguiente orden:

| Número | Nodo |
|---|---|
| 0 | Turno de la mañana |
| 1 | Turno de la tarde |
| 2 | Encargado de la noche |
| 3 | Personal de compras |
| 4 | Recepción de materias primas |

**Resultado obtenido al ejecutar el programa:**

```text
MATRIZ DE ADYACENCIA

0   1   2   3   4
0: [0, 1, 0, 0, 0]
1: [0, 0, 1, 0, 0]
2: [0, 0, 0, 1, 0]
3: [0, 0, 0, 0, 1]
4: [0, 0, 0, 0, 0]
```

Por ejemplo, en la primera fila aparece un 1 en la columna 1. Esto indica que el turno de la mañana tiene una conexión directa con el turno de la tarde.

La última fila contiene únicamente ceros porque la recepción de materias primas no tiene conexiones posteriores dentro del modelo.

## 5. Recorrido BFS (búsqueda en anchura)

BFS (*Breadth-First Search* o búsqueda en anchura) es un algoritmo que permite recorrer los nodos de un grafo comenzando desde un nodo inicial.

En este ejercicio se utilizó como punto de partida el nodo **Turno de la mañana**.

**Resultado obtenido al ejecutar el programa:**

```text
RECORRIDO BFS:
Turno de la mañana
Turno de la tarde
Encargado de la noche
Personal de compras
Recepción de materias primas
```

El recorrido muestra que, partiendo del turno de la mañana, se pueden visitar todas las etapas del proceso siguiendo las conexiones existentes.

En este caso, BFS visita los nodos en el mismo orden en que se desarrolla el proceso de comunicación del inventario.

## 6. Comparación entre lista y matriz de adyacencia

Existen diferentes formas de representar un grafo. En este ejercicio se implementaron dos: lista de adyacencia y matriz de adyacencia.

| Característica | Lista de adyacencia | Matriz de adyacencia |
|---|---|---|
| Representación | Guarda los vecinos de cada nodo. | Utiliza filas y columnas. |
| Memoria | O(V + E) | O(V²) |
| Recorrer vecinos | O(grado del nodo) | O(V) |
| Comprobar conexión | O(grado del nodo) | O(1) |
| BFS | O(V + E) | O(V²) |

Donde:

- **V:** cantidad de vértices o nodos.
- **E:** cantidad de aristas o conexiones.

### Análisis

La lista de adyacencia permite almacenar únicamente las conexiones existentes, por lo que resulta conveniente cuando un grafo tiene pocos enlaces.

La matriz de adyacencia permite comprobar rápidamente si existe una conexión entre dos nodos, pero utiliza espacio para representar todas las combinaciones posibles entre ellos.

En el caso de COFFEEOLOGY se identificaron cinco nodos y cuatro conexiones. Por esta razón, la lista de adyacencia resulta una representación más conveniente para este modelo.

## 7. Estructura seleccionada

Para representar el proceso de inventario se seleccionó la **lista de adyacencia**.

Las razones principales son:

- El proceso tiene pocos nodos y conexiones.
- No todos los nodos necesitan conectarse entre sí.
- Permite visualizar fácilmente la comunicación entre los turnos.
- Evita almacenar conexiones que no existen.
- Facilita el recorrido del grafo mediante BFS.

Aunque también se implementó la matriz de adyacencia para comparar ambas representaciones, la lista resulta más adecuada para este caso.

## 8. Complejidad del recorrido

El algoritmo BFS tiene diferentes costos dependiendo de la representación utilizada:

- Con lista de adyacencia: O(V + E).
- Con matriz de adyacencia: O(V²).

Como el modelo utiliza una lista de adyacencia, el recorrido BFS tiene una complejidad O(V + E).

Esto significa que el tiempo de recorrido depende de la cantidad de nodos y conexiones existentes.

## 9. Conclusión

El proceso de inventario de COFFEEOLOGY puede representarse mediante un grafo dirigido, utilizando nodos para identificar las etapas del proceso y aristas para representar la comunicación entre ellas.

Se implementaron dos representaciones: lista de adyacencia y matriz de adyacencia. También se realizó un recorrido BFS desde el turno de la mañana, obteniendo como resultado las cinco etapas del proceso en el orden esperado.

Finalmente, se seleccionó la lista de adyacencia porque permite representar el proceso de manera sencilla y utiliza memoria proporcional a los nodos y conexiones existentes.

Esta implementación permite comprender cómo se relacionan las diferentes etapas del inventario mediante estructuras de grafos. Se trata de una representación académica del proceso real, no de un sistema de grafos que actualmente utilice la empresa.