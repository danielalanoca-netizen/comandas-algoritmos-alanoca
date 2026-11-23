# Estrategia de solución — COFFEEOLOGY

## Decisión que se repite y resultado que quiero mejorar

Cuando COFFEEOLOGY repone sus materias primas, debe decidir cuáles comprar. Esa decisión se repite para cada producto: comprarlo o dejarlo para después.

El objetivo es escoger productos de alta prioridad sin superar el presupuesto disponible.

## ¿Cómo funcionaría una estrategia voraz?

Una idea sería comprar primero el producto con más prioridad por cada unidad de costo. Pero esa elección no siempre lleva al mejor resultado.

Por ejemplo, si tengo un presupuesto de 10:

| Materia prima | Costo | Prioridad |
|---|---:|---:|
| Leche | 6 | 13 |
| Café | 5 | 10 |
| Azúcar | 5 | 10 |


Pero esta elección no siempre consigue el mejor resultado total. Si el presupuesto es 10, la leche cuesta 6 y tiene prioridad 13; el café cuesta 5 y tiene prioridad 10; y el azúcar cuesta 5 y tiene prioridad 10. La regla elegiría primero la leche y dejaría 4, así que la prioridad total sería 13. En cambio, comprar café y azúcar cuesta 10 y da una prioridad total de 20.

Este ejemplo muestra que, en este problema, elegir lo mejor en cada paso no garantiza la mejor combinación final. Por eso, no conviene usar esa regla voraz para asegurar el resultado óptimo.

## ¿Cómo ayudaría la programación dinámica?

La programación dinámica revisaría las combinaciones posibles guardando resultados parciales. Para cada producto tendría en cuenta dos opciones: comprarlo o dejarlo. También guardaría cuál es la mejor prioridad posible para distintos presupuestos, para no repetir los mismos cálculos.

Así puede comparar combinaciones completas y encontrar la de mayor prioridad sin exceder el presupuesto.

## ¿Cuál estrategia usaría y por qué?

Para este problema usaría programación dinámica, porque quiero encontrar la mejor combinación de productos y el ejemplo muestra que la regla voraz puede fallar. La programación dinámica permite considerar las decisiones anteriores y comparar las combinaciones posibles.
