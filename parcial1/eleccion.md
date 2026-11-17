Alanoca Alfaro Daniel Antony
# P1.3 — Elegir

Datos: n = 300.000 historias clínicas y q = 5.000 consultas.
Usaré log₂(300.000) ≈ 18,2, es decir, unas 19 comparaciones por búsqueda binaria.

1. Recorrer la lista en cada consulta:
   En el peor caso se revisan los 300.000 números por consulta:
   5.000 × 300.000 = 1.500.000.000 comparaciones.

2. Ordenar una vez con un algoritmo O(n log n) y buscar:
   Ordenar cuesta aproximadamente n log₂(n):
   300.000 × 18,2 ≈ 5.458.000 operaciones.
   Las búsquedas cuestan como máximo 5.000 × 19 = 95.000 comparaciones.
   Total aproximado: 5.553.000 operaciones.
   Se puede ordenar in place, por ejemplo con heapsort.

3. Ordenar una vez con un algoritmo cuadrático y buscar:
   Si usamos selection sort, hace n(n−1)/2 comparaciones:
   300.000 × 299.999 / 2 = 44.999.850.000.
   Sumando las búsquedas: aproximadamente 44.999.945.000 operaciones.
   El ordenamiento puede hacerse in place, pero su costo es mucho mayor.

Elección:
Elijo la opción 2: ordenar una vez con un algoritmo O(n log n) que no duplique la lista y luego hacer búsqueda binaria. Su costo aproximado para 5.000 consultas es de 5,55 millones de operaciones, frente a 1.500 millones de la opción 1 y unos 45.000 millones de la opción 3.

Punto de cambio:
Con este modelo aproximado, la opción 1 cuesta 300.000q operaciones y la opción 2 cuesta cerca de 5.458.000 + 19q. Se igualan alrededor de 18,2 consultas; desde unas 19 consultas elegiría ordenar y usar búsqueda binaria. El umbral real puede variar según el algoritmo y el equipo.


Apoyo de P1.2:
repetido en el medio       esperado True  · por pares True  · tu cura True
sin repetidos              esperado False · por pares False · tu cura False
lista vacía                esperado False · por pares False · tu cura False
un solo elemento           esperado False · por pares False · tu cura False
repetido en los extremos   esperado True  · por pares True  · tu cura True

Medición: 1 calentamiento + 3 corridas medidas; promedio en ms
       n     por pares (ms)     cociente      cura (ms)     cociente
   1,000              9.493            —          0.042            —
   2,000             37.778        3.98x          0.118        2.80x
   4,000            164.067        4.34x          0.180        1.52x
   8,000            625.892        3.81x          0.422        2.35x

En mis mediciones, al duplicar n, la solución por pares tardó cerca de cuatro veces más, mientras que la cura con conjunto mostró crecimiento más cercano a lineal, aunque con ruido. Esto apoya evitar el crecimiento cuadrático de la opción 3. Los tiempos de P1.2 corresponden a otros algoritmos y tamaños, así que no los extrapolo directamente al hospital.