
import random  # Para generar numeros aleatorios
import time    # Para medir el tiempo de ejecucion


# ==========================================
# 1. ORDENAMIENTO POR INSERCION
# ==========================================

def insertion_sort(lista):

    # Recorremos la lista desde el segundo elemento
    for i in range(1, len(lista)):

        actual = lista[i]  # Guardamos el numero que vamos a ordenar
        j = i - 1  # Empezamos a comparar con el numero anterior

        # Movemos los numeros mayores hacia la derecha
        while j >= 0 and lista[j] > actual:
            lista[j + 1] = lista[j]
            j -= 1

        # Colocamos el numero en su posicion correcta
        lista[j + 1] = actual


# ==========================================
# 2. QUICKSORT
# ==========================================

def quick_sort(lista, inicio, fin):

    # Si ya no hay elementos para ordenar, terminamos
    if inicio >= fin:
        return

    # Elegimos el numero del medio como pivote
    pivote = lista[(inicio + fin) // 2]

    i = inicio
    j = fin

    # Comparamos los numeros hasta que los indices se crucen
    while i <= j:

        # Buscamos un numero mayor o igual al pivote
        while lista[i] < pivote:
            i += 1

        # Buscamos un numero menor o igual al pivote
        while lista[j] > pivote:
            j -= 1

        # Si todavia no se cruzaron, intercambiamos los numeros
        if i <= j:
            lista[i], lista[j] = lista[j], lista[i]

            i += 1
            j -= 1

    # Ordenamos nuevamente la parte izquierda
    if inicio < j:
        quick_sort(lista, inicio, j)

    # Ordenamos nuevamente la parte derecha
    if i < fin:
        quick_sort(lista, i, fin)


# ==========================================
# 3. SORT NATIVO DE PYTHON
# ==========================================

def python_sort(lista):

    # Ordenamos los numeros automaticamente
    lista.sort()


# ==========================================
# 4. MEDIR TIEMPO DE EJECUCION
# ==========================================

def medir_tiempo(funcion, datos):

    # Hacemos una copia para no modificar los datos originales
    copia = datos.copy()

    # Guardamos el tiempo inicial
    inicio = time.perf_counter()

    # Ejecutamos el algoritmo
    funcion(copia)

    # Guardamos el tiempo final
    fin = time.perf_counter()

    # Convertimos el tiempo a milisegundos
    tiempo_ms = (fin - inicio) * 1000

    # Comprobamos que los numeros hayan quedado ordenados
    if copia != sorted(datos):
        raise ValueError("El algoritmo no ordeno correctamente")

    return tiempo_ms


# ==========================================
# 5. CONFIGURACION DEL TORNEO
# ==========================================

# Cantidades de numeros que vamos a utilizar
cantidades = [10000, 20000, 40000, 80000]

# Guardamos los tres algoritmos que vamos a comparar
algoritmos = {
    "Insercion": insertion_sort,
    "QuickSort": lambda lista: quick_sort(lista, 0, len(lista) - 1),
    "Python sort": python_sort
}

# Aqui guardaremos los resultados de las pruebas
resultados = []


# ==========================================
# 6. EJECUTAR EL TORNEO
# ==========================================

print("\n==============================================")
print("          TORNEO DE ORDENAMIENTOS")
print("==============================================")

# Repetimos las pruebas con cada cantidad de numeros
for cantidad in cantidades:

    print(f"\nCANTIDAD DE DATOS: {cantidad:,}")
    print("----------------------------------------------")

    # Generamos numeros aleatorios sin repetir
    datos = random.sample(range(1, cantidad * 10 + 1), cantidad)

    # Probamos cada uno de los algoritmos
    for nombre, algoritmo in algoritmos.items():

        print(f"\nAlgoritmo: {nombre}")

        # Ejecutamos una primera vez como calentamiento
        medir_tiempo(algoritmo, datos)

        # Aqui guardaremos los tiempos de las tres corridas
        tiempos = []

        # Realizamos tres pruebas para cada algoritmo
        for corrida in range(1, 4):

            # Medimos el tiempo de ejecucion
            tiempo = medir_tiempo(algoritmo, datos)

            # Guardamos el tiempo obtenido
            tiempos.append(tiempo)

            print(f"Corrida {corrida}: {tiempo:.3f} ms")

        # Calculamos el promedio de las tres corridas
        promedio = sum(tiempos) / len(tiempos)

        print(f"PROMEDIO: {promedio:.3f} ms")

        # Guardamos los resultados de esta prueba
        resultados.append((cantidad, nombre, tiempos, promedio))


# ==========================================
# 7. MOSTRAR TABLA FINAL EN TERMINAL
# ==========================================

print("\n")
print("=" * 72)
print("             RESULTADOS DEL TORNEO")
print("=" * 72)

# Mostramos los encabezados de la tabla
print(
    f"{'n':>12} | "
    f"{'Insercion':>13} | "
    f"{'QuickSort':>13} | "
    f"{'Python sort':>13}"
)

print("-" * 72)

# Recorremos cada cantidad de datos
for cantidad in cantidades:

    # Aqui guardaremos los promedios de cada algoritmo
    promedios = {}

    # Buscamos los resultados correspondientes a esa cantidad
    for n, nombre, tiempos, promedio in resultados:

        if n == cantidad:
            promedios[nombre] = promedio

    # Mostramos los promedios en una sola fila
    print(
        f"{cantidad:>12,} | "
        f"{promedios['Insercion']:>10.3f} ms | "
        f"{promedios['QuickSort']:>10.3f} ms | "
        f"{promedios['Python sort']:>10.3f} ms"
    )

print("=" * 72)

print("\nTORNEO FINALIZADO")
