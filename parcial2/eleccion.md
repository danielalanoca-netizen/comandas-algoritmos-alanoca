# Daniel Antony Alanoca Alfaro

## Problema

El receptor guarda pedidos pendientes. Cada pedido tiene un plazo en minutos y un número de llegada. Se prepara primero el pedido con menor plazo; si hay empate, se prepara primero el que llegó antes. También se consulta si un pedido concreto continúa pendiente y cuántos pedidos hay.

## Frecuencias consideradas

- **120.000** registros.
- **120.000** preparaciones.
- **40.000** consultas de pertenencia (`EstaPendiente`).

El código no fija cuántas veces se consulta `Pendientes`; por eso no le asigno una frecuencia numérica. Consultar esa propiedad debe ser O(1).

## Elección

Usaré dos estructuras coordinadas:

1. Un **min-heap** (cola de prioridad) con una entrada por pedido, ordenada por `(plazo, llegada)`. En Python, una entrada puede ser `(plazo, llegada, nombre)` y `heapq` mantiene el menor elemento en la raíz.
2. Un **set** con los nombres que siguen pendientes. Sirve para buscar un nombre sin recorrer el heap.

El contador de llegada aumenta en cada registro. Así, si dos pedidos tienen el mismo plazo, el menor número de llegada queda antes en el heap.

## Tabla de operaciones y costos

Sea **n** la cantidad actual de pedidos pendientes; en esta carga llega hasta 120.000.

| Operación | Frecuencia diaria | Estructura elegida | Costo por operación |
|---|---:|---|---|
| Registrar un pedido | 120.000 | Min-heap + set | O(log n) por insertar en el heap; O(1) promedio para añadir el nombre al set |
| Preparar el siguiente | 120.000 | Min-heap + set | O(log n) por extraer el mínimo; O(1) promedio para quitar el nombre del set |
| Consultar si un pedido está pendiente | 40.000 | Set | O(1) promedio |
| Consultar cantidad de pendientes | No especificada | Set | O(1), mediante `len(set)` |


## Por qué la lista simple resulta costosa con estos números

La lista tiene que revisar los pedidos uno por uno cada vez que se prepara uno. Si hay 120.000 pedidos, en total tendría que hacer cerca de 7.200 millones de revisiones para encontrar cuál preparar primero.

También, cada vez que se elimina un pedido de la lista, algunos pedidos pueden tener que moverse de lugar. Y para comprobar si un pedido sigue pendiente, la lista puede tener que revisarlos hasta encontrarlo. En 40.000 consultas, eso podría sumar hasta 4.800 millones de revisiones.

El min-heap encuentra y saca el pedido más urgente revisando solo unos 17 niveles cada vez. Para registrar y preparar los 120.000 pedidos, serían alrededor de 4,08 millones de pasos como máximo. El set permite comprobar si un pedido sigue pendiente en muy pocos pasos, en promedio.

Por eso, con tantos pedidos y consultas, el min-heap junto con el set evita muchísimas revisiones.

## ¿Cuándo cambiaría la elección?

Si el sistema manejara muy pocos pedidos pendientes —por ejemplo, decenas— y casi nunca preparara pedidos ni consultara pertenencia, elegiría una lista simple por su menor complejidad de implementación. En la carga indicada, con 120.000 preparaciones y muchas consultas, el heap más el set evita repetir recorridos grandes.
