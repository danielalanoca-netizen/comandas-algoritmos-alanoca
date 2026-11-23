## 1. Objetivo del experimento

Comparar el rendimiento de dos estructuras de datos al realizar búsquedas de materias primas por código dentro del inventario de COFFEEOLOGY.

Se comparan dos alternativas:

- **Lista (`list`):** solución ingenua que recorre los registros hasta encontrar el código solicitado.
- **Diccionario (`dict`):** solución mejorada que utiliza el código como clave para acceder directamente al registro.

El objetivo es observar cómo cambia el tiempo de búsqueda cuando aumenta la cantidad de materias primas.

## 2. Configuración del experimento

Para realizar la comparación se establecieron las siguientes condiciones:

| Parámetro | Configuración |
|---|---|
| Operación evaluada | Buscar materia prima por código |
| Estructura ingenua | Lista (`list`) |
| Estructura mejorada | Diccionario (`dict`) |
| Tamaños del inventario | 50, 100, 200 y 400 |
| Consultas por ejecución | 1000 |
| Calentamiento | 1 ejecución por estructura |
| Repeticiones medidas | 3 |
| Resultado presentado | Promedio de las tres repeticiones |
| Unidad de tiempo | Microsegundos por búsqueda |

Los tamaños del inventario se duplican en cada prueba: 50, 100, 200 y 400 registros.

Ambas estructuras utilizan los mismos registros y reciben exactamente los mismos códigos de consulta. Las consultas corresponden a códigos existentes en el inventario.

## 3. Protocolo de medición

El experimento se realizó siguiendo estos pasos:

1. Se generó un inventario con la cantidad de materias primas correspondiente a cada prueba.
2. Se construyó una lista con los registros y un diccionario utilizando los códigos como claves.
3. Se generaron 1000 códigos aleatorios existentes en el inventario.
4. Se realizó una ejecución de calentamiento para cada estructura, sin registrar esos tiempos.
5. Se realizaron tres repeticiones medidas para cada estructura.
6. Se alternó el orden de medición entre la lista y el diccionario para reducir posibles sesgos por el orden de ejecución.
7. Se calculó el tiempo promedio por búsqueda en microsegundos.
8. Se calculó el factor de crecimiento respecto al tamaño anterior y la relación entre el tiempo de la lista y el diccionario.

El tiempo promedio por búsqueda se calculó dividiendo el tiempo total de las 1000 consultas entre la cantidad de consultas.

El promedio final corresponde a:

**Promedio = (Repetición 1 + Repetición 2 + Repetición 3) / 3**

## 4. Resultados de las mediciones

Los siguientes resultados corresponden a la ejecución del programa `medicion.py`.

### 4.1. Tabla comparativa

| N | Lista (µs) | Dict (µs) | Lista / Dict | Crec. Lista | Crec. Dict |
|---:|---:|---:|---:|---:|---:|
| 50 | 1.1039 | 0.0531 | 20.80x | - | - |
| 100 | 2.0287 | 0.0460 | 44.10x | 1.84x | 0.87x |
| 200 | 4.4808 | 0.0444 | 100.99x | 2.21x | 0.96x |
| 400 | 7.0131 | 0.0481 | 145.70x | 1.57x | 1.08x |

**Interpretación de las columnas:**

- **Lista / Dict:** indica cuántas veces más lenta fue la búsqueda mediante lista respecto al diccionario.
- **Crec. Lista:** compara el tiempo de la lista con el de la fila anterior.
- **Crec. Dict:** compara el tiempo del diccionario con el de la fila anterior.
- Un factor menor que 1 indica que el tiempo medido disminuyó respecto a la prueba anterior.

### 4.2. Mediciones individuales

Para mostrar cómo se obtuvieron los promedios, se presentan los tiempos de las tres repeticiones.

**Inventario de 50 materias primas**

| Repetición | Lista (µs) | Dict (µs) |
|---:|---:|---:|
| 1 | 1.2856 | 0.0629 |
| 2 | 1.1196 | 0.0586 |
| 3 | 0.9066 | 0.0377 |

**Inventario de 100 materias primas**

| Repetición | Lista (µs) | Dict (µs) |
|---:|---:|---:|
| 1 | 2.1293 | 0.0409 |
| 2 | 2.2635 | 0.0393 |
| 3 | 1.6934 | 0.0578 |

**Inventario de 200 materias primas**

| Repetición | Lista (µs) | Dict (µs) |
|---:|---:|---:|
| 1 | 5.8900 | 0.0482 |
| 2 | 3.7710 | 0.0425 |
| 3 | 3.7813 | 0.0424 |

**Inventario de 400 materias primas**

| Repetición | Lista (µs) | Dict (µs) |
|---:|---:|---:|
| 1 | 7.6906 | 0.0424 |
| 2 | 6.4075 | 0.0391 |
| 3 | 6.9412 | 0.0629 |

## 5. Análisis de los resultados

Los resultados muestran que la búsqueda mediante lista aumenta su tiempo conforme crece la cantidad de materias primas. Al pasar de 50 a 400 registros, el promedio aumenta de 1.1039 µs a 7.0131 µs.

En cambio, el diccionario mantiene tiempos relativamente estables. Sus promedios se encuentran entre 0.0444 µs y 0.0531 µs durante las cuatro pruebas.

La diferencia también se observa en la columna Lista / Dict. Con 50 registros, la lista tarda 20.80 veces más que el diccionario; con 400 registros, la diferencia llega a 145.70 veces.

El crecimiento de la lista se relaciona con su complejidad temporal O(n), porque necesita recorrer los registros hasta encontrar el código. En el diccionario, la búsqueda tiene una complejidad promedio O(1), por lo que el tiempo no aumenta proporcionalmente con el tamaño del inventario.

## 6. Conclusión

El experimento muestra que el diccionario es más eficiente que la lista para buscar materias primas por código. Al aumentar el inventario, el tiempo de la lista creció, mientras que el del diccionario se mantuvo relativamente estable. Sin embargo, hubo variaciones entre las tres repeticiones, especialmente en algunas mediciones del diccionario, posiblemente por ruido del sistema y las condiciones de ejecución. Estos resultados respaldan la elección de un diccionario para las búsquedas frecuentes por código, aunque las mediciones representan una prueba controlada y no el rendimiento de un sistema completo en producción.