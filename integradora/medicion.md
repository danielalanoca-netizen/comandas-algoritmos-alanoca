# Daniel Antony Alanoca Alfaro

# I3 — Medición y comparación de rendimiento

## 1. Protocolo de medición

Para realizar las pruebas se utilizó el siguiente procedimiento:

1. Se generaron paquetes con pesos y ganancias aleatorias.
2. Se utilizó una semilla fija para generar los mismos datos en ambos algoritmos.
3. La capacidad de la furgoneta se calculó como un tercio del peso total de los paquetes.
4. Se realizó una ejecución de calentamiento que no se incluyó en los resultados.
5. Después se realizaron tres ejecuciones medidas para cada algoritmo.
6. Se calculó el promedio de los tres tiempos.
7. Se comprobó que ambos algoritmos obtuvieran la misma ganancia máxima.

Para medir el tiempo se utilizó `perf_counter()` de Python y los resultados se expresaron en milisegundos.

Se utilizaron cuatro tamaños: 14, 16, 18 y 20 paquetes.

## 2. Resultados de las mediciones

| Paquetes | Ganancia máxima | Ingenuo (ms) | Mejorado (ms) |
|---:|---:|---:|---:|
| 14 | 420 | 26.0066 | 0.1302 |
| 16 | 431 | 49.4621 | 0.0812 |
| 18 | 648 | 190.8718 | 0.0900 |
| 20 | 663 | 819.0576 | 0.0921 |

Los dos algoritmos obtuvieron las mismas ganancias máximas en todas las pruebas.

### Tiempos de las tres ejecuciones

| Paquetes | Ingenuo (ms) | Mejorado (ms) |
|---:|---|---|
| 14 | 25.6913 / 25.5703 / 26.7581 | 0.1609 / 0.1289 / 0.1007 |
| 16 | 58.7898 / 46.1062 / 43.4902 | 0.0697 / 0.0931 / 0.0809 |
| 18 | 190.1674 / 191.6601 / 190.7880 | 0.0989 / 0.0861 / 0.0851 |
| 20 | 820.2078 / 813.8456 / 823.1193 | 0.0928 / 0.0919 / 0.0917 |

## 3. Crecimiento del tiempo

También se comparó cuánto aumentó el tiempo de ejecución respecto a la prueba anterior.

| Paquetes | Crecimiento ingenuo | Crecimiento mejorado |
|---:|---:|---:|
| 14 | — | — |
| 16 | 1.90x | 0.62x |
| 18 | 3.86x | 1.11x |
| 20 | 4.29x | 1.02x |

Se puede observar que el algoritmo ingenuo aumenta considerablemente su tiempo cuando se agregan más paquetes. Entre las pruebas de 16 y 18 paquetes, el tiempo casi se cuadruplicó.

En cambio, el algoritmo mejorado mantuvo tiempos muy bajos y bastante estables. Las pequeñas variaciones se pueden deber a las condiciones de ejecución de la computadora.

## 4. Prueba con 1000 paquetes

También se realizó una prueba utilizando 1000 paquetes y una capacidad de 10000 kg, como solicita el ejercicio.

| Característica | Resultado |
|---|---:|
| Cantidad de paquetes | 1000 |
| Capacidad | 10000 kg |
| Ganancia máxima | 31337 Bs |
| Peso utilizado | 10000 kg |
| Paquetes seleccionados | 459 |
| Tiempo de ejecución | 373.2760 ms |

El programa consiguió seleccionar 459 paquetes, utilizando los 10000 kg disponibles y obteniendo una ganancia máxima de 31337 Bs.

El tiempo de ejecución fue aproximadamente 0.37 segundos.

## 5. ¿Qué pasaría con una capacidad de 1000000000 kg?

Si la capacidad fuera de 1000000000 kg, nuestro algoritmo necesitaría demasiada memoria y tiempo, porque las tablas de programación dinámica dependen directamente de la capacidad. Por eso, aunque funciona bien con capacidades más pequeñas, no resulta práctico cuando la capacidad es demasiado grande.

## 6. Conclusión

En las pruebas realizadas, el planificador mejorado obtuvo tiempos mucho menores que el ingenuo, y ambos encontraron la misma ganancia máxima. También se observó que el algoritmo ingenuo tarda más a medida que aumentan los paquetes.

Finalmente, la prueba con 1000 paquetes demostró que la programación dinámica puede trabajar con una mayor cantidad de datos. Por estos resultados, considero que el planificador mejorado es una mejor alternativa para este problema.