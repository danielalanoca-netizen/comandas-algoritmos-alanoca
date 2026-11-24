# Comparación de algoritmos — COFFEEOLOGY

## 1. ¿Qué problema queremos resolver?

En COFFEEOLOGY se necesita decidir qué materias primas comprar cuando tenemos un presupuesto limitado.

Cada materia prima tiene dos datos:

- **Costo:** cuánto dinero necesitamos para comprarla.
- **Prioridad:** qué tan importante es comprarla.

El objetivo es elegir las materias primas que tengan la mayor prioridad posible sin gastar más del presupuesto disponible.

Para este ejercicio, cada producto solamente se puede comprar una vez o dejar para después.

Este problema se conoce como **mochila 0/1**.

Los costos y prioridades son datos de prueba generados por el programa, no son datos reales de las compras de COFFEEOLOGY.

## 2. Algoritmos que vamos a comparar

### 2.1. Fuerza bruta

Este algoritmo prueba todas las posibilidades.

Para cada materia prima revisa dos opciones:

- Comprar el producto.
- No comprar el producto.

Después compara los resultados y se queda con la combinación que tenga la mayor prioridad sin superar el presupuesto.

Su costo de tiempo es **O(2ⁿ)**, porque la cantidad de combinaciones aumenta mucho cuando agregamos más productos.

### 2.2. Programación dinámica

Este algoritmo también revisa las opciones de comprar o no comprar, pero guarda los resultados que ya calculó.

Así evita repetir el mismo trabajo muchas veces.

Al final, encuentra la combinación con mayor prioridad sin superar el presupuesto.

Su costo de tiempo es **O(n × P)**, donde:

- n es la cantidad de productos.
- P es el presupuesto disponible.

## 3. ¿Cómo realizamos las pruebas?

Para comparar los dos algoritmos seguimos estos pasos:

1. Probamos con 8, 12, 16 y 20 productos.
2. Generamos productos con costos entre 1 y 10.
3. Asignamos prioridades entre 5 y 30.
4. El presupuesto se calcula multiplicando la cantidad de productos por 5.
5. Utilizamos los mismos productos y el mismo presupuesto para los dos algoritmos.
6. Ejecutamos una prueba inicial para preparar el programa. Esta prueba no se cuenta.
7. Medimos cada algoritmo tres veces y calculamos el promedio.
8. Utilizamos `perf_counter()` para medir el tiempo en milisegundos.

También comprobamos que los dos algoritmos encontraran la misma prioridad máxima.

## 4. Resultados de las pruebas

| Productos | Presupuesto | Prioridad máxima | Fuerza bruta (ms) | Dinámica (ms) |
|---:|---:|---:|---:|---:|
| 8 | 40 | 126 | 0.0365 | 0.0233 |
| 12 | 60 | 156 | 0.3859 | 0.0471 |
| 16 | 80 | 281 | 7.2376 | 0.0866 |
| 20 | 100 | 267 | 118.0788 | 0.1342 |

### Comprobación

Los dos algoritmos encontraron la misma prioridad máxima en los cuatro tamaños:

- 8 productos: 126.
- 12 productos: 156.
- 16 productos: 281.
- 20 productos: 267.

Esto demuestra que ambos resolvieron correctamente los mismos casos de prueba.

## 5. ¿Qué observamos?

Al revisar los resultados vemos que la fuerza bruta necesita cada vez más tiempo cuando aumenta la cantidad de productos.

Por ejemplo, con 20 productos tardó 118.0788 ms, mientras que la programación dinámica tardó 0.1342 ms.

Esto sucede porque la fuerza bruta revisa muchas combinaciones, mientras que la programación dinámica guarda resultados anteriores y evita repetir cálculos.

Los tiempos pueden variar un poco dependiendo de las condiciones de la computadora y de otros procesos que estén funcionando. Por eso realizamos tres mediciones y calculamos el promedio.

## 6. Conclusión

Con esta práctica comprobamos que los dos algoritmos pueden encontrar la misma prioridad máxima.

Sin embargo, la fuerza bruta tarda mucho más cuando aumenta la cantidad de productos, porque debe revisar muchas combinaciones.

La programación dinámica aprovecha los resultados que ya calculó y evita repetir trabajo.

Por eso elegiría la programación dinámica para este problema, ya que en nuestras pruebas encontró los mismos resultados en mucho menos tiempo.