Alanoca Alfaro Daniel Antony
Cura: HayRepetidosCurado
def HayRepetidosCurado(carnets: list[int]) -> bool:
    vistos: set[int] = set()

    for carnet in carnets:
        if carnet in vistos:
            return True
        vistos.add(carnet)

    return False
vistos guarda los carnets que ya recorrimos. Si el carnet actual ya está ahí, encontramos un repetido y devolvemos True. Si no, lo agregamos y seguimos. Si terminamos el recorrido, devolvemos False. La función no modifica la lista y tiene costo esperado O(n), con memoria adicional O(n).
Código lento: HayRepetidosPorPares
def HayRepetidosPorPares(carnets: list[int]) -> bool:
    for i in range(len(carnets)):
        for j in range(i + 1, len(carnets)):
            if carnets[i] == carnets[j]:
                return True
    return False
El bucle exterior elige un carnet y el interior lo compara con cada carnet que aparece después. Si encuentra dos iguales, devuelve True; si revisa todos los pares sin hallar coincidencias, devuelve False. En el peor caso, cuando no hay repetidos, compara \(n(n-1)/2\) pares, así que su costo es O(n²).

El codigo completo se encuentra acontinuacion

import random
import time


def HayRepetidosPorPares(carnets: list[int]) -> bool:
    """Solución correcta pero lenta: compara cada carnet con los siguientes."""
    for i in range(len(carnets)):
        for j in range(i + 1, len(carnets)):
            if carnets[i] == carnets[j]:
                return True
    return False


def HayRepetidosCurado(carnets: list[int]) -> bool:
    """Usa un conjunto para detectar valores vistos, sin modificar la lista."""
    vistos: set[int] = set()
    for carnet in carnets:
        if carnet in vistos:
            return True
        vistos.add(carnet)
    return False


def GenerarSinRepetidos(n: int, semilla: int = 42) -> list[int]:
    """Genera los números de 0 a n-1 en orden aleatorio, sin duplicados."""
    datos = list(range(n))
    azar = random.Random(semilla)
    for i in range(n - 1, 0, -1):
        k = azar.randrange(i + 1)
        datos[i], datos[k] = datos[k], datos[i]
    return datos


CASOS = [
    ([7, 3, 9, 3, 5], True, "repetido en el medio"),
    ([7, 3, 9, 4, 5], False, "sin repetidos"),
    ([], False, "lista vacía"),
    ([8], False, "un solo elemento"),
    ([4, 1, 2, 6, 4], True, "repetido en los extremos"),
]


def main() -> None:
    for datos, esperado, descripcion in CASOS:
        lenta = HayRepetidosPorPares(datos)
        curada = HayRepetidosCurado(datos)
        print(
            f"{descripcion:<26} esperado {str(esperado):<5} · "
            f"por pares {str(lenta):<5} · tu cura {curada}"
        )

    print("\nMedición: 1 calentamiento + 3 corridas medidas; promedio en ms")
    print(f"{'n':>8} {'por pares (ms)':>18} {'cociente':>12} "
          f"{'cura (ms)':>14} {'cociente':>12}")

    tamaños = (1_000, 2_000, 4_000, 8_000)
    anterior_lenta = None
    anterior_curada = None

    for n in tamaños:
        # La generación queda fuera del cronómetro y las dos funciones reciben
        # exactamente la misma lista sin valores repetidos.
        datos = GenerarSinRepetidos(n)
        promedios = {}

        for nombre, funcion in (
            ("por pares", HayRepetidosPorPares),
            ("cura", HayRepetidosCurado),
        ):
            funcion(datos)  # una corrida de calentamiento
            corridas_ms = []
            for _ in range(3):
                inicio = time.perf_counter()
                funcion(datos)
                corridas_ms.append((time.perf_counter() - inicio) * 1_000)
            promedios[nombre] = sum(corridas_ms) / len(corridas_ms)

        lenta = promedios["por pares"]
        curada = promedios["cura"]
        cociente_lenta = "—" if anterior_lenta is None else f"{lenta / anterior_lenta:.2f}x"
        cociente_curada = "—" if anterior_curada is None else f"{curada / anterior_curada:.2f}x"
        print(f"{n:8,d} {lenta:18.3f} {cociente_lenta:>12} "
              f"{curada:14.3f} {cociente_curada:>12}")
        anterior_lenta = lenta
        anterior_curada = curada


if __name__ == "__main__":
    main()
