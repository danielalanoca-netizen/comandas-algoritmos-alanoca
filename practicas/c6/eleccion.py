
import random
import time


# ==========================================
# 1. BUSQUEDA LINEAL
# ==========================================

# Busca un numero revisando los datos uno por uno
def busqueda_lineal(datos, buscado):

    comparaciones = 0

    for i in range(len(datos)):

        comparaciones += 1

        if datos[i] == buscado:
            return i, comparaciones

    return -1, comparaciones


# ==========================================
# 2. BUSQUEDA BINARIA
# ==========================================

# Busca un numero dividiendo la lista por la mitad
# IMPORTANTE: los datos deben estar ordenados
def busqueda_binaria(datos, buscado):

    inicio = 0
    fin = len(datos) - 1
    comparaciones = 0

    while inicio <= fin:

        medio = inicio + (fin - inicio) // 2

        comparaciones += 1

        if datos[medio] == buscado:
            return medio, comparaciones

        if datos[medio] < buscado:
            inicio = medio + 1
        else:
            fin = medio - 1

    return -1, comparaciones


# ==========================================
# 3. MERGESORT
# ==========================================

# Ordena la lista dividiendola en dos partes
def merge_sort(datos):

    if len(datos) <= 1:
        return datos, 0

    medio = len(datos) // 2

    # Dividimos la lista en dos mitades
    izquierda, comp_izq = merge_sort(datos[:medio])
    derecha, comp_der = merge_sort(datos[medio:])

    # Unimos las dos mitades ordenadas
    resultado = []
    i = 0
    j = 0
    comparaciones = comp_izq + comp_der

    while i < len(izquierda) and j < len(derecha):

        comparaciones += 1

        if izquierda[i] <= derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1

    # Agregamos los elementos que quedaron pendientes
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])

    return resultado, comparaciones


# ==========================================
# 4. CANDIDATO A: LINEAL CON VARIAS CONSULTAS
# ==========================================

def probar_lineal(datos, consultas):

    total_comparaciones = 0

    for clave in consultas:

        posicion, comparaciones = busqueda_lineal(datos, clave)

        total_comparaciones += comparaciones

        if posicion == -1:
            raise ValueError("No se encontro un registro")

    return total_comparaciones


# ==========================================
# 5. CANDIDATO B: MERGESORT + BINARIA
# ==========================================

def probar_binaria(datos, consultas):

    # Primero ordenamos el inventario
    ordenados, comparaciones_orden = merge_sort(datos)

    total_comparaciones = 0

    # Despues buscamos cada materia prima
    for clave in consultas:

        posicion, comparaciones = busqueda_binaria(
            ordenados, clave
        )

        total_comparaciones += comparaciones

        if posicion == -1:
            raise ValueError("No se encontro un registro")

    return total_comparaciones, comparaciones_orden


# ==========================================
# 6. MEDIR LOS TIEMPOS
# ==========================================

def medir_lineal(datos, consultas):

    inicio = time.perf_counter()

    probar_lineal(datos, consultas)

    fin = time.perf_counter()

    return (fin - inicio) * 1000


def medir_binaria(datos, consultas):

    inicio = time.perf_counter()

    probar_binaria(datos, consultas)

    fin = time.perf_counter()

    return (fin - inicio) * 1000


# ==========================================
# 7. CONFIGURACION DEL EXPERIMENTO
# ==========================================

# Cantidades de registros que vamos a probar
cantidades = [450, 900, 1800, 3600]

# Consultas estimadas durante una jornada
consultas_por_dia = [100, 150, 200, 250]

# Guardaremos los resultados de todas las pruebas
resultados = []


# ==========================================
# 8. EJECUCION DEL EXPERIMENTO
# ==========================================

print("\n==============================================================")
print("       COMPARACION DE BUSQUEDA DE INVENTARIO")
print("                  CASO COFFEOLOGY")
print("==============================================================")

# Repetimos las pruebas con cada cantidad de registros
for cantidad in cantidades:

    # Creamos materias primas con codigos numericos
    datos = random.sample(
        range(1, cantidad * 10 + 1),
        cantidad
    )

    print(f"\nCANTIDAD DE REGISTROS: {cantidad:,}")
    print("-" * 62)

    # Probamos diferentes cantidades de consultas
    for cantidad_consultas in consultas_por_dia:

        # Elegimos registros existentes para buscar
        consultas = random.choices(
            datos,
            k=cantidad_consultas
        )

        print(f"\nConsultas realizadas: {cantidad_consultas}")

        # --------------------------------------
        # CALENTAMIENTO
        # --------------------------------------

        medir_lineal(datos, consultas)
        medir_binaria(datos, consultas)

        tiempos_lineal = []
        tiempos_binaria = []

        # --------------------------------------
        # TRES CORRIDAS MEDIDAS
        # --------------------------------------

        for corrida in range(1, 4):

            tiempo_l = medir_lineal(datos, consultas)
            tiempo_b = medir_binaria(datos, consultas)

            tiempos_lineal.append(tiempo_l)
            tiempos_binaria.append(tiempo_b)

            print(
                f"Corrida {corrida}: "
                f"Lineal = {tiempo_l:.3f} ms | "
                f"MergeSort + Binaria = {tiempo_b:.3f} ms"
            )

        # Calculamos los promedios
        promedio_l = sum(tiempos_lineal) / 3
        promedio_b = sum(tiempos_binaria) / 3

        # Contamos las comparaciones de ambos candidatos
        comparaciones_l = probar_lineal(datos, consultas)

        comparaciones_b, comparaciones_merge = probar_binaria(
            datos, consultas
        )

        # Determinamos cual tuvo menor tiempo
        if promedio_l < promedio_b:
            ganador = "Lineal"
        elif promedio_b < promedio_l:
            ganador = "MergeSort + Binaria"
        else:
            ganador = "Empate"

        print(f"Promedio lineal: {promedio_l:.3f} ms")
        print(f"Promedio MergeSort + Binaria: {promedio_b:.3f} ms")
        print(f"Ganador: {ganador}")

        # Guardamos los resultados
        resultados.append({
            "n": cantidad,
            "q": cantidad_consultas,
            "lineal": promedio_l,
            "binaria": promedio_b,
            "comp_lineal": comparaciones_l,
            "comp_merge": comparaciones_merge,
            "comp_binaria": comparaciones_b,
            "ganador": ganador
        })


# ==========================================
# 9. TABLA FINAL DE TIEMPOS
# ==========================================

print("\n\n")
print("=" * 90)
print("                 TABLA FINAL DE TIEMPOS")
print("=" * 90)

print(
    f"{'n':>8} | {'Consultas':>10} | "
    f"{'Lineal':>16} | {'MergeSort + Binaria':>23} | {'Ganador':>18}"
)

print("-" * 90)

for r in resultados:

    print(
        f"{r['n']:>8,} | "
        f"{r['q']:>10,} | "
        f"{r['lineal']:>12.3f} ms | "
        f"{r['binaria']:>19.3f} ms | "
        f"{r['ganador']:>18}"
    )

print("=" * 90)


# ==========================================
# 10. TABLA DE COMPARACIONES
# ==========================================

print("\n")
print("=" * 90)
print("              TABLA DE COMPARACIONES")
print("=" * 90)

print(
    f"{'n':>8} | {'Consultas':>10} | "
    f"{'Lineal':>14} | {'MergeSort':>14} | "
    f"{'Binaria':>14} | {'Total B':>14}"
)

print("-" * 90)

for r in resultados:

    total_b = r["comp_merge"] + r["comp_binaria"]

    print(
        f"{r['n']:>8,} | "
        f"{r['q']:>10,} | "
        f"{r['comp_lineal']:>14,} | "
        f"{r['comp_merge']:>14,} | "
        f"{r['comp_binaria']:>14,} | "
        f"{total_b:>14,}"
    )

print("=" * 90)


# ==========================================
# 11. FINAL DEL EXPERIMENTO
# ==========================================

print("\nEXPERIMENTO FINALIZADO")
print("Se verificaron las busquedas y se compararon ambos candidatos.")
