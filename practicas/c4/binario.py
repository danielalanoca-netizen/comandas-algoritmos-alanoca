
import random
import time


# ==========================================
# 1. GENERAR UN MILLON DE DATOS ALEATORIOS
# ==========================================

print("Generando datos...")

datos = random.sample(range(1, 10_000_001), 1_000_000)

# Ordenamos los datos para permitir la busqueda binaria
datos.sort()

# Generamos 1000 consultas aleatorias
consultas = random.choices(datos, k=1000)

print("Datos generados correctamente.")
print("Cantidad de datos:", len(datos))
print("Cantidad de consultas:", len(consultas))


# ==========================================
# 2. BUSQUEDA LINEAL
# ==========================================

def busqueda_lineal(lista, objetivo):

    for elemento in lista:

        if elemento == objetivo:
            return True

    return False


# ==========================================
# 3. BUSQUEDA BINARIA
# ==========================================

def busqueda_binaria(lista, objetivo):

    inicio = 0
    fin = len(lista) - 1

    while inicio <= fin:

        medio = (inicio + fin) // 2

        if lista[medio] == objetivo:
            return True

        elif objetivo < lista[medio]:
            fin = medio - 1

        else:
            inicio = medio + 1

    return False


# ==========================================
# 4. FUNCION PARA MEDIR EL TIEMPO
# ==========================================

def medir_tiempo(funcion, lista, consultas):

    inicio = time.perf_counter()

    for numero in consultas:
        funcion(lista, numero)

    fin = time.perf_counter()

    tiempo_ms = (fin - inicio) * 1000

    return tiempo_ms


# ==========================================
# 5. CALENTAMIENTO
# ==========================================

print("\nRealizando calentamiento...")

medir_tiempo(busqueda_lineal, datos, consultas)
medir_tiempo(busqueda_binaria, datos, consultas)


# ==========================================
# 6. TRES CORRIDAS MEDIDAS
# ==========================================

resultados_lineal = []
resultados_binaria = []

print("\nIniciando mediciones...\n")

for corrida in range(1, 4):

    tiempo_lineal = medir_tiempo(
        busqueda_lineal, datos, consultas
    )

    tiempo_binaria = medir_tiempo(
        busqueda_binaria, datos, consultas
    )

    resultados_lineal.append(tiempo_lineal)
    resultados_binaria.append(tiempo_binaria)

    print("Corrida", corrida)
    print(f"Lineal:  {tiempo_lineal:.3f} ms")
    print(f"Binaria: {tiempo_binaria:.3f} ms")
    print()


# ==========================================
# 7. CALCULAR PROMEDIOS
# ==========================================

promedio_lineal = sum(resultados_lineal) / 3
promedio_binaria = sum(resultados_binaria) / 3

# ==========================================
# 8. MOSTRAR RESULTADOS
# ==========================================

print("===================================")
print("          RESULTADOS FINALES")
print("===================================")

print(f"Lineal:  {promedio_lineal:.3f} ms")
print(f"Binaria: {promedio_binaria:.3f} ms")

if promedio_binaria > 0:
    diferencia = promedio_lineal / promedio_binaria
    print(f"\nLa busqueda binaria fue {diferencia:.2f} veces mas rapida.")

print("\nExperimento finalizado.")
