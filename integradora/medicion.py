
# Daniel Antony Alanoca Alfaro

# Importamos las herramientas necesarias.
import random
from time import perf_counter

# Importamos nuestro planificador mejorado.
from planificador import Paquete, PlanificadorMejorado


# --------------------------------------------------
# 1. PLANIFICADOR INGENUO
# --------------------------------------------------

class PlanificadorIngenuo:

    def __init__(self):
        # Guardamos los códigos de los paquetes seleccionados.
        self.elegidos = set()

    def elegir(self, paquetes, capacidad_kg):

        # Obtenemos la cantidad de paquetes.
        n = len(paquetes)

        # Inicializamos la mejor ganancia.
        mejor = 0

        # Guardamos la combinación que produce la mejor ganancia.
        mejor_mascara = 0

        # Probamos todas las combinaciones posibles.
        for mascara in range(1 << n):

            # Inicializamos el peso y la ganancia de esta combinación.
            kg = 0
            ganancia = 0

            # Revisamos todos los paquetes.
            for i in range(n):

                # Comprobamos si el paquete está incluido en la combinación.
                if mascara & (1 << i):

                    # Sumamos su peso y su ganancia.
                    kg += paquetes[i].kg
                    ganancia += paquetes[i].ganancia

            # Comprobamos que no se supere la capacidad.
            if kg <= capacidad_kg and ganancia > mejor:

                # Guardamos la nueva mejor ganancia.
                mejor = ganancia

                # Guardamos la combinación correspondiente.
                mejor_mascara = mascara

        # Reiniciamos el conjunto de paquetes elegidos.
        self.elegidos = set()

        # Recuperamos los paquetes de la mejor combinación.
        for i in range(n):

            # Comprobamos si el paquete fue seleccionado.
            if mejor_mascara & (1 << i):

                # Guardamos su código.
                self.elegidos.add(paquetes[i].codigo)

        # Devolvemos la ganancia y los códigos seleccionados.
        return mejor, list(self.elegidos)

    def esta_en_el_viaje(self, codigo):

        # Consultamos si el código está en el conjunto.
        return codigo in self.elegidos


# --------------------------------------------------
# 2. GENERAR LOS DATOS DE PRUEBA
# --------------------------------------------------

def generar_carga(n):

    # Creamos un generador aleatorio con semilla fija.
    azar = random.Random(n)

    # Generamos n paquetes con pesos y ganancias aleatorias.
    paquetes = [
        Paquete(
            "C" + str(i),
            azar.randrange(5, 60),
            azar.randrange(10, 100)
        )
        for i in range(n)
    ]

    # Calculamos la capacidad como un tercio del peso total.
    capacidad = sum(p.kg for p in paquetes) // 3

    # Devolvemos los paquetes y la capacidad.
    return paquetes, capacidad


# --------------------------------------------------
# 3. MEDIR EL TIEMPO PROMEDIO
# --------------------------------------------------

def medir_promedio(planificador, paquetes, capacidad):

    # Realizamos una corrida de calentamiento.
    # Esta ejecución no se incluye en el promedio.
    plan = planificador()
    ganancia_calentamiento, _ = plan.elegir(paquetes, capacidad)

    # Guardamos los tiempos de las tres mediciones.
    tiempos = []

    # Realizamos tres ejecuciones medidas.
    for _ in range(3):

        # Creamos una nueva instancia del planificador.
        plan = planificador()

        # Registramos el tiempo inicial.
        inicio = perf_counter()

        # Ejecutamos la selección de paquetes.
        ganancia, _ = plan.elegir(paquetes, capacidad)

        # Registramos el tiempo final.
        fin = perf_counter()

        # Guardamos el tiempo en milisegundos.
        tiempos.append((fin - inicio) * 1000)

        # Comprobamos que la ganancia no cambie.
        if ganancia != ganancia_calentamiento:
            raise RuntimeError("La ganancia cambió entre ejecuciones.")

    # Calculamos el promedio de las tres mediciones.
    promedio = sum(tiempos) / len(tiempos)

    # Devolvemos la ganancia, el promedio y los tiempos individuales.
    return ganancia_calentamiento, promedio, tiempos


# --------------------------------------------------
# 4. ELEGIR EL TAMAÑO DE ENTRADA
# --------------------------------------------------

def elegir_tamano_inicial():

    # Empezamos probando con un máximo de 18 paquetes.
    maximo = 18

    # Generamos los datos para esa prueba.
    paquetes, capacidad = generar_carga(maximo)

    # Medimos una ejecución de la solución ingenua.
    inicio = perf_counter()
    PlanificadorIngenuo().elegir(paquetes, capacidad)
    tiempo = perf_counter() - inicio

    # Si tarda menos de medio segundo, probamos con 20.
    if tiempo < 0.5:
        maximo = 20

        # Generamos los nuevos datos.
        paquetes, capacidad = generar_carga(maximo)

        # Medimos nuevamente la solución ingenua.
        inicio = perf_counter()
        PlanificadorIngenuo().elegir(paquetes, capacidad)
        tiempo = perf_counter() - inicio

    # Si todavía tarda menos de medio segundo, probamos con 22.
    if tiempo < 0.5:
        maximo = 22

        # Generamos los nuevos datos.
        paquetes, capacidad = generar_carga(maximo)

        # Medimos nuevamente.
        inicio = perf_counter()
        PlanificadorIngenuo().elegir(paquetes, capacidad)
        tiempo = perf_counter() - inicio

    # Si supera los 20 segundos, reducimos el tamaño.
    if tiempo > 20:
        maximo -= 2

    # Devolvemos el tamaño inicial de las cuatro pruebas.
    return maximo - 6


# --------------------------------------------------
# 5. COMPARAR LOS DOS PLANIFICADORES
# --------------------------------------------------

def comparar_planificadores():

    # Elegimos el tamaño inicial mediante una prueba rápida.
    n = elegir_tamano_inicial()

    # Definimos los cuatro tamaños solicitados.
    tamanos = [n, n + 2, n + 4, n + 6]

    # Guardamos los resultados anteriores para calcular el crecimiento.
    anterior_ingenuo = None
    anterior_mejorado = None

    # Mostramos el encabezado de la tabla.
    print("\nCOMPARACIÓN DE PLANIFICADORES")
    print("Tamaños utilizados:", tamanos)

    print(
        "\n n | Ganancia | Ingenuo (ms) | "
        "Mejorado (ms) | Crec. ingenuo | Crec. mejorado"
    )

    print("-" * 90)

    # Recorremos los cuatro tamaños.
    for cantidad in tamanos:

        # Generamos los mismos datos para ambos algoritmos.
        paquetes, capacidad = generar_carga(cantidad)

        # Medimos la solución ingenua.
        ganancia_i, tiempo_i, tiempos_i = medir_promedio(
            PlanificadorIngenuo,
            paquetes,
            capacidad
        )

        # Medimos la solución mejorada.
        ganancia_m, tiempo_m, tiempos_m = medir_promedio(
            PlanificadorMejorado,
            paquetes,
            capacidad
        )

        # Comprobamos que ambos algoritmos obtengan la misma ganancia.
        if ganancia_i != ganancia_m:
            raise RuntimeError(
                f"Las ganancias no coinciden para n={cantidad}"
            )

        # Calculamos cuánto creció el tiempo respecto a la fila anterior.
        if anterior_ingenuo is None:
            crecimiento_i = "-"
            crecimiento_m = "-"
        else:
            crecimiento_i = f"{tiempo_i / anterior_ingenuo:.2f}x"
            crecimiento_m = f"{tiempo_m / anterior_mejorado:.2f}x"

        # Mostramos los resultados de esta fila.
        print(
            f"{cantidad:2} | {ganancia_i:8} | "
            f"{tiempo_i:12.4f} | {tiempo_m:13.4f} | "
            f"{crecimiento_i:14} | {crecimiento_m}"
        )

        # Guardamos los tiempos para la siguiente comparación.
        anterior_ingenuo = tiempo_i
        anterior_mejorado = tiempo_m

        # Mostramos las tres mediciones para conservar los datos.
        print("   Tiempos ingenuo:", [round(t, 4) for t in tiempos_i])
        print("   Tiempos mejorado:", [round(t, 4) for t in tiempos_m])

    # Devolvemos los tamaños utilizados.
    return tamanos


# --------------------------------------------------
# 6. PRUEBA CON 1000 PAQUETES Y CAPACIDAD 10000
# --------------------------------------------------

def prueba_grande():

    # Generamos 1000 paquetes con una semilla fija.
    azar = random.Random(1000)

    paquetes = [
        Paquete(
            "C" + str(i),
            azar.randrange(5, 60),
            azar.randrange(10, 100)
        )
        for i in range(1000)
    ]

    # Establecemos la capacidad solicitada por el profesor.
    capacidad = 10000

    # Creamos el planificador mejorado.
    plan = PlanificadorMejorado()

    # Medimos el tiempo de ejecución.
    inicio = perf_counter()

    # Ejecutamos la selección de paquetes.
    ganancia, elegidos = plan.elegir(paquetes, capacidad)

    # Calculamos el tiempo final.
    fin = perf_counter()

    # Convertimos el resultado a milisegundos.
    tiempo = (fin - inicio) * 1000

    # Calculamos el peso total de los paquetes elegidos.
    peso_total = sum(
        p.kg for p in paquetes
        if p.codigo in plan.elegidos
    )

    # Mostramos los resultados.
    print("\nPRUEBA CON 1000 PAQUETES")
    print("Capacidad:", capacidad, "kg")
    print("Ganancia máxima:", ganancia)
    print("Peso utilizado:", peso_total, "kg")
    print("Paquetes seleccionados:", len(elegidos))
    print(f"Tiempo de ejecución: {tiempo:.4f} ms")


# --------------------------------------------------
# 7. PROGRAMA PRINCIPAL
# --------------------------------------------------

if __name__ == "__main__":

    # Ejecutamos la comparación de los dos planificadores.
    comparar_planificadores()

    # Ejecutamos la prueba grande.
    prueba_grande()
