# Estrategia de solución — COFFEEOLOGY

## 1. Problema identificado

En COFFEEOLOGY, el control del inventario se realiza mediante revisiones manuales de las materias primas. El inventario puede alcanzar aproximadamente 450 registros y su revisión diaria puede tomar entre 30 minutos y una hora.

Durante los diferentes turnos se identifican las materias primas que necesitan reposición. Posteriormente, el encargado del turno de la noche reúne la información, prepara una lista de compra y la envía al personal encargado de realizar las compras.

A partir de este proceso identificamos una decisión que puede estudiarse mediante un problema de optimización: cuando existe un presupuesto limitado, ¿qué materias primas conviene comprar?

## 2. Decisión que queremos optimizar

Cada materia prima tiene dos datos:

- **Costo:** cuánto dinero se necesita para comprarla.
- **Prioridad:** qué tan importante es adquirirla.

El objetivo es seleccionar las materias primas que tengan la mayor prioridad posible sin superar el presupuesto disponible.

Para este ejercicio, cada materia prima solamente puede comprarse una vez o dejarse para después.

Este problema se puede representar mediante el modelo de mochila 0/1.

Los costos y prioridades utilizados son datos simulados para el ejercicio académico. No representan precios ni prioridades reales de las compras de COFFEEOLOGY.

## 3. ¿Cómo funcionaría la fuerza bruta?

La fuerza bruta consiste en probar todas las combinaciones posibles de compra.

Para cada materia prima se consideran dos opciones:

- Comprar la materia prima.
- Dejarla para después.

Después de evaluar todas las posibilidades, se selecciona la combinación que tenga la mayor prioridad sin superar el presupuesto disponible.

Su complejidad temporal es O(2ⁿ), donde n representa la cantidad de materias primas.

Esta estrategia permite encontrar la solución óptima, pero su tiempo de ejecución aumenta considerablemente cuando se agregan más productos.

## 4. ¿Cómo funcionaría una estrategia voraz?

Una posible estrategia sería comprar primero la materia prima que tenga la mayor prioridad por cada unidad de costo.

Sin embargo, esta elección no siempre permite obtener el mejor resultado total.

Por ejemplo, si tenemos un presupuesto de 10:

| Materia prima | Costo | Prioridad |
|---|---:|---:|
| Leche | 6 | 13 |
| Café | 5 | 10 |
| Azúcar | 5 | 10 |

La leche tiene una relación de prioridad por costo de aproximadamente 2.17, mientras que el café y el azúcar tienen una relación de 2.

Si aplicamos la estrategia voraz, elegiríamos primero la leche porque tiene la mayor relación de prioridad por costo. Después de comprarla quedarían 4 unidades de presupuesto, por lo que no podríamos comprar el café ni el azúcar.

El resultado sería una prioridad total de 13.

En cambio, si compramos el café y el azúcar, gastaríamos las 10 unidades del presupuesto y obtendríamos una prioridad total de 20.

Este ejemplo demuestra que elegir la mejor opción en cada paso no garantiza conseguir la mejor combinación final.

Por esta razón, una estrategia voraz no resulta adecuada para garantizar el resultado óptimo de este problema.

## 5. ¿Cómo ayudaría la programación dinámica?

La programación dinámica permite resolver este problema guardando resultados parciales para evitar repetir cálculos.

Para cada materia prima considera dos posibilidades:

- Comprar la materia prima si alcanza el presupuesto.
- Dejarla para después y conservar el presupuesto.

El algoritmo utiliza una tabla donde guarda la mejor prioridad que se puede obtener según los productos revisados y el presupuesto disponible.

De esta manera, puede comparar las diferentes posibilidades y encontrar la combinación con mayor prioridad sin superar el presupuesto.

Su complejidad temporal es O(n × P), donde:

- n representa la cantidad de materias primas.
- P representa el presupuesto disponible.

Su ventaja es que aprovecha los resultados calculados anteriormente, evitando repetir los mismos cálculos.

## 6. ¿Cuál estrategia utilizaría y por qué?

Para este problema utilizaría programación dinámica.

La razón es que necesitamos encontrar la mejor combinación de materias primas cuando el presupuesto es limitado.

La fuerza bruta permite encontrar la solución óptima, pero revisa todas las combinaciones posibles y su tiempo de ejecución aumenta rápidamente.

Por otro lado, el ejemplo anterior demuestra que una estrategia voraz puede tomar una decisión que parece conveniente al principio, pero que termina dando un resultado inferior.

En cambio, la programación dinámica permite comparar las decisiones posibles y encontrar la prioridad máxima aprovechando los resultados anteriores.

Por lo tanto, considero que es una alternativa más adecuada para resolver este modelo de optimización.