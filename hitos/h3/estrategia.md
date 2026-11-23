# Estrategia de solución — COFFEEOLOGY

## Problema que quiero resolver

COFFEEOLOGY necesita comprar materias primas, pero tiene un presupuesto limitado. Cada producto tiene un costo y una prioridad. El objetivo es elegir qué comprar sin pasar el presupuesto y conseguir la mayor prioridad posible.

Este es un ejemplo relacionado con el inventario de COFFEEOLOGY.

## ¿Sirve usar un algoritmo voraz?

Una idea sería comprar primero el producto con más prioridad por cada unidad de costo. Pero esa regla no siempre da el mejor resultado.

Por ejemplo, tengo 10 unidades de presupuesto:

| Materia prima | Costo | Prioridad |
|---|---:|---:|
| Leche | 6 | 12 |
| Café | 5 | 10 |
| Azúcar | 5 | 10 |

Si compro leche, gasto 6 y me quedan 4. Ya no me alcanza para comprar café o azúcar. Mi prioridad total sería 12.

Pero si compro café y azúcar, gasto 10 y consigo una prioridad total de 20. Entonces, elegir primero lo que parece mejor puede hacer que al final consiga menos.

Por eso, este problema no siempre se resuelve bien con esa regla voraz. Después de ver programación dinámica en clase, completaré qué estrategia conviene usar y cómo se puede encontrar la mejor combinación.
