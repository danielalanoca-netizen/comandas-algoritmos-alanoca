
import random  # Permite generar datos y consultas aleatorias.
import time    # Permite medir el tiempo de ejecución.

# ------------------------------------------------------------
# 1. CONFIGURACIÓN DEL EXPERIMENTO
# ------------------------------------------------------------

# Cantidades de materias primas que tendrá cada inventario.
# Cada tamaño duplica al anterior.
TAMANOS = [50, 100, 200, 400]

# Cantidad de búsquedas que se realizarán en cada repetición.
NUM_CONSULTAS = 1000

# Cantidad de repeticiones que se medirán.
REPETICIONES = 3


# ------------------------------------------------------------
# 2. CREACIÓN DEL INVENTARIO
# ------------------------------------------------------------

def crear_inventario(n):
    """
    Genera un inventario con n materias primas.

    Cada materia prima contiene:
    - Código único.
    - Nombre.
    - Cantidad disponible.

    Devuelve una lista con todos los registros.
    """

    # Creamos una lista vacía para almacenar las materias primas.
    inventario = []

    # Generamos los registros uno por uno.
    for i in range(n):

        # Representamos cada materia prima mediante un diccionario.
        materia = {
            "codigo": f"MP-{i:04d}",
            "nombre": f"Materia prima {i}",
            "cantidad": random.randint(1, 100)
        }

        # Agregamos el registro al inventario.
        inventario.append(materia)

    # Devolvemos el inventario completo.
    return inventario


# ------------------------------------------------------------
# 3. BÚSQUEDA UTILIZANDO UNA LISTA
# ------------------------------------------------------------

def buscar_lista(inventario, consultas):
    """
    Busca los códigos recorriendo la lista desde el principio.

    Esta es la solución ingenua porque debe revisar los
    registros hasta encontrar cada código solicitado.
    """

    # Recorremos todos los códigos que debemos buscar.
    for codigo in consultas:

        # Recorremos la lista hasta encontrar el código.
        resultado = next(
            (
                materia
                for materia in inventario
                if materia["codigo"] == codigo
            ),
            None
        )

        # Comprobamos que el registro haya sido encontrado.
        if resultado is None:
            raise ValueError(f"No se encontró el código {codigo}")


# ------------------------------------------------------------
# 4. BÚSQUEDA UTILIZANDO UN DICCIONARIO
# ------------------------------------------------------------

def buscar_diccionario(inventario, consultas):
    """
    Busca los códigos utilizando un diccionario.

    El código funciona como clave para acceder directamente
    al registro correspondiente.
    """

    # Recorremos los mismos códigos utilizados en la lista.
    for codigo in consultas:

        # Consultamos directamente mediante la clave.
        resultado = inventario.get(codigo)

        # Comprobamos que el registro haya sido encontrado.
        if resultado is None:
            raise ValueError(f"No se encontró el código {codigo}")


# ------------------------------------------------------------
# 5. FUNCIÓN PARA MEDIR UNA EJECUCIÓN
# ------------------------------------------------------------

def medir_ejecucion(funcion, estructura, consultas):
    """
    Mide el tiempo que tarda una función en realizar las búsquedas.

    Devuelve el tiempo promedio por búsqueda en microsegundos.
    """

    # Registramos el instante inicial en nanosegundos.
    inicio = time.perf_counter_ns()

    # Ejecutamos todas las búsquedas.
    funcion(estructura, consultas)

    # Registramos el instante final.
    fin = time.perf_counter_ns()

    # Calculamos el tiempo total de las consultas.
    tiempo_total = fin - inicio

    # Calculamos el promedio de tiempo por búsqueda.
    tiempo_por_busqueda = tiempo_total / len(consultas)

    # Convertimos nanosegundos a microsegundos.
    tiempo_microsegundos = tiempo_por_busqueda / 1000

    # Devolvemos el tiempo obtenido.
    return tiempo_microsegundos


# ------------------------------------------------------------
# 6. EJECUCIÓN DEL EXPERIMENTO
# ------------------------------------------------------------

def ejecutar_experimento():
    """
    Compara la búsqueda mediante lista y diccionario.

    Realiza:
    - Una ejecución de calentamiento por estructura.
    - Tres repeticiones medidas.
    - Cálculo del promedio.
    - Cálculo del crecimiento de los tiempos.
    """

    # Aquí almacenaremos los resultados de todos los tamaños.
    resultados = []

    # Mostramos la información general del experimento.
    print("\n========== EXPERIMENTO COFFEEOLOGY ==========")
    print("Operación: Buscar materia prima por código")
    print("Consultas por repetición:", NUM_CONSULTAS)
    print("Repeticiones medidas:", REPETICIONES)
    print("Calentamiento: 1 ejecución por estructura")
    print("-" * 90)

    # Recorremos los diferentes tamaños de inventario.
    for n in TAMANOS:

        # Creamos el inventario original en forma de lista.
        inventario_lista = crear_inventario(n)

        # Construimos el diccionario usando los mismos registros.
        # El código de cada materia prima será la clave.
        inventario_dict = {
            materia["codigo"]: materia
            for materia in inventario_lista
        }

        # Creamos un generador aleatorio con una semilla fija.
        # Esto permite reproducir las mismas consultas para cada n.
        rng = random.Random(42 + n)

        # Generamos códigos aleatorios que existen en el inventario.
        consultas = [
            f"MP-{rng.randrange(n):04d}"
            for _ in range(NUM_CONSULTAS)
        ]

        # ----------------------------------------------------
        # 6.1. PRUEBAS DE CALENTAMIENTO
        # ----------------------------------------------------

        # Ejecutamos la búsqueda con lista sin guardar el tiempo.
        buscar_lista(inventario_lista, consultas)

        # Ejecutamos la búsqueda con diccionario sin guardar el tiempo.
        buscar_diccionario(inventario_dict, consultas)

        # ----------------------------------------------------
        # 6.2. TRES REPETICIONES MEDIDAS
        # ----------------------------------------------------

        # Creamos listas para guardar cada medición individual.
        tiempos_lista = []
        tiempos_dict = []

        # Realizamos las tres repeticiones.
        for repeticion in range(REPETICIONES):

            # Alternamos qué estructura se mide primero.
            # En repeticiones pares comienza la lista.
            # En repeticiones impares comienza el diccionario.
            if repeticion % 2 == 0:

                # Medimos primero la búsqueda con lista.
                tiempo_lista = medir_ejecucion(
                    buscar_lista,
                    inventario_lista,
                    consultas
                )

                # Medimos después la búsqueda con diccionario.
                tiempo_dict = medir_ejecucion(
                    buscar_diccionario,
                    inventario_dict,
                    consultas
                )

            else:

                # Medimos primero la búsqueda con diccionario.
                tiempo_dict = medir_ejecucion(
                    buscar_diccionario,
                    inventario_dict,
                    consultas
                )

                # Medimos después la búsqueda con lista.
                tiempo_lista = medir_ejecucion(
                    buscar_lista,
                    inventario_lista,
                    consultas
                )

            # Guardamos los tiempos individuales de cada estructura.
            tiempos_lista.append(tiempo_lista)
            tiempos_dict.append(tiempo_dict)

        # ----------------------------------------------------
        # 6.3. CÁLCULO DE LOS PROMEDIOS
        # ----------------------------------------------------

        # Sumamos las tres mediciones y dividimos entre tres.
        promedio_lista = sum(tiempos_lista) / REPETICIONES
        promedio_dict = sum(tiempos_dict) / REPETICIONES

        # Calculamos cuántas veces más lenta fue la lista.
        diferencia = promedio_lista / promedio_dict

        # Guardamos todos los resultados del tamaño actual.
        resultados.append({
            "n": n,
            "lista": promedio_lista,
            "dict": promedio_dict,
            "diferencia": diferencia,
            "tiempos_lista": tiempos_lista,
            "tiempos_dict": tiempos_dict
        })

    # --------------------------------------------------------
    # 7. PRESENTACIÓN DE LOS RESULTADOS
    # --------------------------------------------------------

    # Mostramos los encabezados de la tabla principal.
    print("\n========== TABLA DE RESULTADOS ==========")

    print(
        f"{'N':<8}"
        f"{'Lista (us)':<16}"
        f"{'Dict (us)':<16}"
        f"{'Lista/Dict':<15}"
        f"{'Crec. Lista':<15}"
        f"{'Crec. Dict':<15}"
    )

    # Guardamos los promedios de la fila anterior.
    anterior_lista = None
    anterior_dict = None

    # Recorremos todos los resultados obtenidos.
    for resultado in resultados:

        # Calculamos el crecimiento de la lista respecto al tamaño anterior.
        crecimiento_lista = (
            resultado["lista"] / anterior_lista
            if anterior_lista is not None
            else None
        )

        # Calculamos el crecimiento del diccionario respecto al tamaño anterior.
        crecimiento_dict = (
            resultado["dict"] / anterior_dict
            if anterior_dict is not None
            else None
        )

        # Mostramos los resultados promedio.
        print(
            f"{resultado['n']:<8}"
            f"{resultado['lista']:<16.4f}"
            f"{resultado['dict']:<16.4f}"
            f"{resultado['diferencia']:<15.2f}"
            f"{(f'{crecimiento_lista:.2f}x' if crecimiento_lista is not None else '-'): <15}"
            f"{(f'{crecimiento_dict:.2f}x' if crecimiento_dict is not None else '-'): <15}"
        )

        # Actualizamos los promedios anteriores.
        anterior_lista = resultado["lista"]
        anterior_dict = resultado["dict"]

    # --------------------------------------------------------
    # 8. PRESENTACIÓN DE LAS MEDICIONES INDIVIDUALES
    # --------------------------------------------------------

    # Mostramos los tres tiempos obtenidos para cada tamaño.
    print("\n========== MEDICIONES INDIVIDUALES ==========")

    # Recorremos los resultados para mostrar cada repetición.
    for resultado in resultados:

        # Mostramos el tamaño del inventario.
        print(f"\nInventario de {resultado['n']} materias primas:")

        # Mostramos los tres tiempos de la lista.
        print("Lista:")

        for i, tiempo in enumerate(resultado["tiempos_lista"], start=1):
            print(f"  Repetición {i}: {tiempo:.4f} us")

        # Mostramos los tres tiempos del diccionario.
        print("Diccionario:")

        for i, tiempo in enumerate(resultado["tiempos_dict"], start=1):
            print(f"  Repetición {i}: {tiempo:.4f} us")


# ------------------------------------------------------------
# 9. PUNTO DE ENTRADA DEL PROGRAMA
# ------------------------------------------------------------

# Esta condición permite ejecutar el experimento directamente.
if __name__ == "__main__":

    # Iniciamos la ejecución del experimento.
    ejecutar_experimento()
