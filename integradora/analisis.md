# Daniel Antony Alanoca Alfaro

# I1 — Análisis y elección de estrategia

## a) Análisis de PlanificadorIngenuo

El planificador ingenuo revisa todas las combinaciones posibles de paquetes para encontrar cuál permite obtener la mayor ganancia sin superar la capacidad de la furgoneta.

Si tenemos n paquetes, existen 2ⁿ combinaciones posibles, porque cada paquete puede llevarse o dejarse.

Además, por cada combinación se revisan los paquetes para calcular el peso y la ganancia total.

Por eso, su complejidad es O(n × 2ⁿ).

Este método encuentra la respuesta correcta, pero cuando aumenta la cantidad de paquetes tarda mucho más en terminar.

## b) Análisis de la recurrencia

La versión recursiva tiene esta fórmula:

T(n) = 2T(n-1) + 1

Esto significa que por cada paquete tenemos dos opciones: llevarlo o no llevarlo. Cada opción genera un nuevo problema con un paquete menos.

El teorema maestro no se puede aplicar directamente porque utiliza problemas que se dividen en tamaños como n/b, mientras que en este caso el tamaño disminuye de n a n-1.

Al desarrollar la fórmula se observa que el crecimiento es exponencial, por lo que su complejidad es O(2ⁿ).

## c) Estrategia elegida

Un algoritmo voraz (Greedy) no siempre encuentra la mejor combinación, porque elegir primero el paquete que genera más ganancia por kilogramo no garantiza obtener la mayor ganancia total.

Por ejemplo, en el primer caso de prueba tenemos:

| Paquete | Peso | Ganancia | Ganancia por kg |
|---|---:|---:|---:|
| P1 | 10 kg | Bs 60 | 6 |
| P2 | 20 kg | Bs 100 | 5 |
| P3 | 30 kg | Bs 120 | 4 |

La capacidad de la furgoneta es de 50 kg.

Si utilizamos Greedy, primero elegiría P1 porque tiene la mayor ganancia por kilogramo. Después elegiría P2, pero ya no podría agregar P3 porque superaría la capacidad.

De esta manera obtendríamos una ganancia de Bs 160.

Sin embargo, si elegimos P2 y P3, ocupamos exactamente los 50 kg y obtenemos una ganancia de Bs 220.

Esto demuestra que Greedy no siempre da el mejor resultado.

Por este motivo, elegí programación dinámica, porque permite guardar los resultados de problemas más pequeños y utilizarlos nuevamente cuando se necesitan, evitando repetir los mismos cálculos.

La complejidad de esta solución es O(n × C), donde n es la cantidad de paquetes y C es la capacidad de la furgoneta.

## d) Estructura para consultar los paquetes seleccionados

Para la operación EstaEnElViaje utilizaría un conjunto (set), donde guardaría los códigos de los paquetes que fueron seleccionados.

Elegí esta estructura porque permite comprobar rápidamente si un código se encuentra dentro del conjunto.

La búsqueda promedio en un set tiene una complejidad O(1), mientras que en una lista se tendría que recorrer los elementos, lo que puede costar O(n).

Como esta operación se realizará muchas veces, considero que utilizar un set es una mejor opción.