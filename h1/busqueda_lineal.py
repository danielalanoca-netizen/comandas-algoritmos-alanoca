
import time
import statistics


# ==========================================
# 1. BUSQUEDA LINEAL
# ==========================================

def buscar_producto(catalogo, codigo_buscado):
    for codigo in catalogo:
        if codigo == codigo_buscado:
            return True

    return False


# ==========================================
# 2. GENERAR CATALOGO DE PRUEBA
# ==========================================

def generar_catalogo(cantidad):
    # Datos simulados para el experimento
    return list(range(cantidad))


# ==========================================
# 3. MEDIR TIEMPOS DE EJECUCION
# ==========================================

def medir_busqueda(catalogo, codigo_buscado, repeticiones=5):

    # Calentamiento: descartamos la primera ejecución
    buscar_producto(catalogo, codigo_buscado)

    tiempos = []

    for i in range(repeticiones):

        inicio = time.perf_counter()

        buscar_producto(catalogo, codigo_buscado)

        fin = time.perf_counter()

        tiempo_ms = (fin - inicio) * 1000

        tiempos.append(tiempo_ms)

    promedio = statistics.mean(tiempos)

    return tiempos, promedio


# ==========================================
# 4. EXPERIMENTO
# ==========================================

def ejecutar_experimento():

    n = 100_000

    tamanos = [
        n,
        4 * n,
        16 * n
    ]

    resultados = []

    print("\nEXPERIMENTO: BUSQUEDA LINEAL")
    print("=" * 65)

    for cantidad in tamanos:

        catalogo = generar_catalogo(cantidad)

        # Código inexistente: obliga a recorrer todo el catálogo
        codigo_buscado = -1

        tiempos, promedio = medir_busqueda(
            catalogo,
            codigo_buscado
        )

        resultados.append(promedio)

        print(f"\nCantidad de productos: {cantidad:,}")
        print("Tiempos de ejecución:")

        for numero, tiempo in enumerate(tiempos, start=1):
            print(f"  Corrida {numero}: {tiempo:.4f} ms")

        print(f"Promedio: {promedio:.4f} ms")

    # ======================================
    # 5. CALCULAR RATIOS
    # ======================================

    tiempo_n = resultados[0]
    tiempo_4n = resultados[1]
    tiempo_16n = resultados[2]

    print("\nRATIOS DE CRECIMIENTO")
    print("=" * 65)

    print(f"Ratio 4n / n: {tiempo_4n / tiempo_n:.2f}x")
    print(f"Ratio 16n / n: {tiempo_16n / tiempo_n:.2f}x")

    print("\nExperimento finalizado.")


# ==========================================
# 6. EJECUTAR PROGRAMA
# ==========================================

if __name__ == "__main__":
    ejecutar_experimento()
