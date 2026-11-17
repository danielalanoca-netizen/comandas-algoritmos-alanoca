# Alanoca Alfaro Daniel Antony.


"""Parcial 1, Variante A: detectar carnets repetidos."""

import random  # Se usa para mezclar la lista de datos de prueba.
import time    # Se usa para medir cuánto tarda cada función.


def HayRepetidosPorPares(carnets: list[int]) -> bool:
    """Compara cada carnet con los que aparecen después."""

    # El primer bucle elige la posición del carnet que se va a comparar.
    for i in range(len(carnets)):

        # El segundo bucle compara ese carnet con los siguientes.
        # Empieza en i + 1 para no compararlo consigo mismo ni repetir pares.
        for j in range(i + 1, len(carnets)):

            # Si los dos valores son iguales, encontramos un repetido.
            if carnets[i] == carnets[j]:
                return True  # Termina la función inmediatamente.

    # Si se revisaron todos los pares sin coincidencias, no hay repetidos.
    return False


def HayRepetidosCurado(carnets: list[int]) -> bool:
    """Detecta repetidos usando un conjunto de valores ya vistos."""

    # Un conjunto guarda valores únicos y permite consultar pertenencia
    # rápidamente en promedio. No modifica la lista original.
    vistos: set[int] = set()

    # Recorre cada carnet una sola vez.
    for carnet in carnets:

        # Si ya está en el conjunto, ese valor apareció antes.
        if carnet in vistos:
            return True  # Encontramos una repetición.

        # Si es la primera vez que aparece, lo guardamos para futuras consultas.
        vistos.add(carnet)

    # Si termina el recorrido, todos los valores eran distintos.
    return False


def GenerarSinRepetidos(n: int, semilla: int = 42) -> list[int]:
    """Crea n números distintos y los devuelve en orden aleatorio."""

    # range(n) produce 0, 1, ..., n-1; todos son distintos.
    datos = list(range(n))

    # Crear un generador aleatorio con semilla fija hace que la mezcla
    # se pueda repetir en otra ejecución.
    azar = random.Random(semilla)

    # Fisher-Yates mezcla la lista intercambiando posiciones.
    # Recorre desde el último índice hasta el segundo.
    for i in range(n - 1, 0, -1):

        # Elige al azar una posición entre 0 e i, inclusive.
        k = azar.randrange(i + 1)

        # Intercambia los elementos de las posiciones i y k.
        datos[i], datos[k] = datos[k], datos[i]

    # Devuelve la lista mezclada, todavía sin valores repetidos.
    return datos


# Cada caso contiene: la lista, el resultado esperado y una descripción.
# Se usan para comprobar los cinco escenarios indicados en el enunciado.
CASOS = [
    ([7, 3, 9, 3, 5], True, "repetido en el medio"),
    ([7, 3, 9, 4, 5], False, "sin repetidos"),
    ([], False, "lista vacía"),
    ([8], False, "un solo elemento"),
    ([4, 1, 2, 6, 4], True, "repetido en los extremos"),
]


def main() -> None:
    """Ejecuta los casos de ejemplo y las mediciones de tiempo."""

    # Primero muestra el resultado de cada función en los cinco casos.
    for datos, esperado, descripcion in CASOS:

        # Ejecuta la solución lenta y guarda el resultado.
        lenta = HayRepetidosPorPares(datos)

        # Ejecuta la cura y guarda el resultado.
        curada = HayRepetidosCurado(datos)

        # Imprime la descripción, el resultado esperado y los dos resultados.
        print(
            f"{descripcion:<26} esperado {str(esperado):<5} · "
            f"por pares {str(lenta):<5} · tu cura {curada}"
        )

    # Indica el protocolo y la unidad que se usará en la tabla.
    print("\nMedición: 1 calentamiento + 3 corridas medidas; promedio en ms")

    # Imprime los títulos de las columnas.
    # >8 y >18 alinean a la derecha dentro del espacio indicado.
    print(
        f"{'n':>8} {'por pares (ms)':>18} {'cociente':>12} "
        f"{'cura (ms)':>14} {'cociente':>12}"
    )

    # Los cuatro tamaños se duplican: n, 2n, 4n y 8n.
    tamaños = (1_000, 2_000, 4_000, 8_000)

    # Estas variables recuerdan el promedio de la fila anterior
    # para poder calcular los cocientes.
    anterior_lenta = None
    anterior_curada = None

    # Repite la medición para cada tamaño.
    for n in tamaños:

        # Genera los datos antes de iniciar los cronómetros.
        # Así se mide el trabajo de las funciones, no el de crear la lista.
        datos = GenerarSinRepetidos(n)

        # Aquí se guardará el promedio de cada función para este tamaño.
        promedios = {}

        # Recorre las dos funciones junto con sus nombres para la tabla.
        for nombre, funcion in (
            ("por pares", HayRepetidosPorPares),
            ("cura", HayRepetidosCurado),
        ):
            # Corrida de calentamiento: se ejecuta, pero no se cronometra.
            funcion(datos)

            # Aquí se guardan las tres duraciones medidas.
            corridas_ms = []

            # Hace exactamente tres corridas medidas.
            for _ in range(3):

                # perf_counter ofrece un reloj adecuado para medir duraciones.
                inicio = time.perf_counter()

                # Ejecuta la función sobre la lista sin repetidos.
                funcion(datos)

                # Resta el tiempo inicial al final.
                # El reloj está en segundos; multiplicamos por 1.000
                # para guardar el resultado en milisegundos.
                corridas_ms.append(
                    (time.perf_counter() - inicio) * 1_000
                )

            # Promedia las tres duraciones y guarda el resultado.
            promedios[nombre] = sum(corridas_ms) / len(corridas_ms)

        # Recupera los promedios de cada función para imprimirlos.
        lenta = promedios["por pares"]
        curada = promedios["cura"]

        # La primera fila no tiene una anterior con la cual compararse.
        # En las demás filas se divide el promedio actual por el anterior.
        cociente_lenta = (
            "—" if anterior_lenta is None
            else f"{lenta / anterior_lenta:.2f}x"
        )
        cociente_curada = (
            "—" if anterior_curada is None
            else f"{curada / anterior_curada:.2f}x"
        )

        # Imprime tamaño, promedios y cocientes.
        # :.3f muestra los tiempos con tres decimales.
        # :, separa los miles en el tamaño.
        print(
            f"{n:8,d} {lenta:18.3f} {cociente_lenta:>12} "
            f"{curada:14.3f} {cociente_curada:>12}"
        )

        # Guarda estos promedios para usarlos al calcular la fila siguiente.
        anterior_lenta = lenta
        anterior_curada = curada


# Esta condición ejecuta main() solo cuando corres este archivo directamente.
# Si otro archivo lo importa, main() no se ejecuta automáticamente.
if __name__ == "__main__":
    main()