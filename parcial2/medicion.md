# Daniel Antony Alanoca Alfaro
## Protocolo

Se compararon la solución ingenua, que usa una lista simple, y la solución mejorada, que usa un min-heap y un set. Para cada tamaño se usaron los mismos datos en ambas soluciones: registrar todos los pedidos, consultar si están pendientes y preparar todos los pedidos. La cantidad de consultas fue un tercio del tamaño de la carga.

Antes de medir se hizo una corrida de calentamiento. Luego se hicieron tres corridas y se informó el promedio. Los tamaños se duplicaron: 2.000, 4.000 y 8.000 pedidos.

## Resultados

| Pedidos | Ingenua (s) | Mejorada (s) | Relación |
|---:|---:|---:|---:|
| 2.000 | 0,085967 | 0,000880 | 97,67× |
| 4.000 | 0,398575 | 0,001943 | 205,16× |
| 8.000 | 1,384852 | 0,005304 | 261,08× |

La relación indica cuántas veces tardó la solución ingenua respecto de la mejorada. Por ejemplo, en 8.000 pedidos, la ingenua tardó aproximadamente 261 veces más.

## Conclusión

En las tres mediciones, el receptor mejorado terminó antes. Al duplicar la cantidad de pedidos, el tiempo de la lista aumentó más que el del min-heap con set, y la ventaja observada del receptor mejorado creció. Esto coincide con los costos esperados: la lista vuelve a recorrer muchos elementos para preparar cada pedido, mientras que el heap trabaja por niveles y el set permite consultar nombres rápidamente.

Los tiempos pueden variar por la computadora, otros programas en ejecución y el ruido normal de las mediciones. Por eso importan más la tendencia y el protocolo que los milisegundos exactos. La medición llegó hasta 8.000 pedidos, una carga menor que las 120.000 operaciones diarias usadas en P2.1; estos resultados no son una medición directa de la jornada completa.
