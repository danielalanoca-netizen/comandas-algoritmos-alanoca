from random import Random  # Genera datos aleatorios usando una semilla que permite repetirlos.
from time import perf_counter  # Mide el tiempo de ejecución con precisión.


def fuerza_bruta(productos, presupuesto):  # Busca la mejor combinación revisando las opciones.
    """Prueba las opciones de comprar o dejar cada producto."""

    def buscar(indice, restante):  # Revisa productos desde el índice indicado con el presupuesto restante.
        if indice == len(productos):  # Comprueba si ya se revisaron todos los productos.
            return 0  # Si no quedan productos, no se suma más prioridad.

        costo, prioridad = productos[indice]  # Obtiene el costo y la prioridad del producto actual.

        # Opción 1: dejar el producto.
        mejor = buscar(indice + 1, restante)  # Busca el mejor resultado sin comprarlo.

        # Opción 2: comprarlo si alcanza el presupuesto.
        if costo <= restante:  # Comprueba que el costo no supere el dinero disponible.
            comprando = prioridad + buscar(indice + 1, restante - costo)  # Suma su prioridad y revisa los demás.
            mejor = max(mejor, comprando)  # Se queda con la mejor opción entre comprar y dejarlo.

        return mejor  # Devuelve la mejor prioridad encontrada para estas opciones.

    return buscar(0, presupuesto)  # Inicia la búsqueda desde el primer producto y con todo el presupuesto.


def programacion_dinamica(productos, presupuesto):  # Resuelve el problema guardando resultados en una tabla.
    # Cada fila representa los productos revisados.
    # Cada columna representa un presupuesto posible.
    tabla = [[0] * (presupuesto + 1) for _ in range(len(productos) + 1)]  # Crea la tabla y llena sus celdas con cero.

    for i, (costo, prioridad) in enumerate(productos, start=1):  # Recorre los productos, numerándolos desde 1.
        for dinero in range(presupuesto + 1):  # Revisa cada presupuesto desde 0 hasta el máximo.
            # Opción de dejar el producto.
            tabla[i][dinero] = tabla[i - 1][dinero]  # Copia el mejor resultado sin incluir el producto actual.

            # Opción de comprarlo, si alcanza el presupuesto.
            if costo <= dinero:  # Comprueba si el presupuesto actual alcanza para comprarlo.
                comprando = prioridad + tabla[i - 1][dinero - costo]  # Suma su prioridad al mejor resultado anterior.
                tabla[i][dinero] = max(tabla[i][dinero], comprando)  # Guarda la mejor opción entre comprar y dejarlo.

    return tabla[len(productos)][presupuesto]  # Devuelve la prioridad máxima con todos los productos y el presupuesto completo.


def medir_promedio(funcion, repeticiones=3):  # Mide varias veces una función y calcula su promedio.
    funcion()  # Calentamiento; se ejecuta antes de medir y no se incluye en el promedio.

    tiempos = []  # Guarda los tiempos de cada repetición.
    for _ in range(repeticiones):  # Repite la medición la cantidad de veces indicada.
        inicio = perf_counter()  # Guarda el tiempo justo antes de ejecutar la función.
        funcion()  # Ejecuta la función que se está midiendo.
        fin = perf_counter()  # Guarda el tiempo justo después de ejecutarla.
        tiempos.append((fin - inicio) * 1000)  # Convierte la duración a milisegundos y la guarda.

    return sum(tiempos) / len(tiempos)  # Calcula y devuelve el tiempo promedio.


def main():  # Función principal: ejecuta las pruebas y muestra la tabla.
    tamanos = [8, 12, 16, 20]  # Define los cuatro tamaños de prueba.

    # Imprime los encabezados de las columnas.
    print("Productos | Presupuesto | Prioridad máxima | Fuerza bruta (ms) | Dinámica (ms)")

    for n in tamanos:  # Repite la prueba para cada cantidad de productos.
        azar = Random(n)  # Usa n como semilla para que los datos de cada tamaño sean repetibles.
        productos = [  # Crea la lista de productos para esta prueba.
            (azar.randint(1, 10), azar.randint(5, 30))  # Cada producto tiene un costo y una prioridad aleatorios.
            for _ in range(n)  # Genera n productos.
        ]

        presupuesto = n * 5  # Define el presupuesto según la cantidad de productos.

        resultado_bruto = fuerza_bruta(productos, presupuesto)  # Calcula la prioridad máxima con fuerza bruta.
        resultado_dinamico = programacion_dinamica(productos, presupuesto)  # Calcula la prioridad máxima con dinámica.

        if resultado_bruto != resultado_dinamico:  # Comprueba si las dos estrategias dieron resultados distintos.
            print(f"Error: los resultados no coinciden para n={n}.")  # Muestra un mensaje si no coinciden.
            return  # Termina el programa si las respuestas son diferentes.

        tiempo_bruto = medir_promedio(  # Empieza a medir el tiempo de fuerza bruta.
            lambda: fuerza_bruta(productos, presupuesto)  # Repite fuerza bruta con los datos de esta prueba.
        )
        tiempo_dinamico = medir_promedio(  # Empieza a medir el tiempo de programación dinámica.
            lambda: programacion_dinamica(productos, presupuesto)  # Repite dinámica con los mismos datos.
        )

        # Imprime el tamaño, el presupuesto, la prioridad y los tiempos promedio.
        print(
            f"{n:9} | {presupuesto:11} | {resultado_bruto:16} | "
            f"{tiempo_bruto:17.4f} | {tiempo_dinamico:13.4f}"
        )


if __name__ == "__main__":  # Comprueba que este archivo se esté ejecutando directamente.
    main()  # Llama a la función principal.