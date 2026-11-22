# Daniel Antony Alanoca Alfaro
"""Mide la solución ingenua y la mejorada con cargas que se duplican."""  # Describe el propósito general del archivo.
from heapq import heappop, heappush  # Importa las operaciones para sacar e insertar elementos en un min-heap.
import random  # Importa herramientas para generar datos aleatorios repetibles.
from statistics import mean  # Importa la función que calcula el promedio.
from time import perf_counter  # Importa un reloj de alta precisión para medir duraciones.
class ReceptorIngenuo:  # Define la versión lenta del receptor, que almacena pedidos en una lista.
    """Versión con lista simple para comparar el costo de las operaciones."""  # Documenta qué representa esta clase.
    def __init__(self):  # Inicializa un receptor ingenuo nuevo.
        self.lista = []  # Crea una lista vacía donde se guardarán los pedidos pendientes.
        self.siguiente_llegada = 0  # Guarda el número de llegada que se asignará al próximo pedido.
    def registrar(self, pedido, plazo):  # Define cómo registrar un pedido en el receptor ingenuo.
        self.lista.append((plazo, self.siguiente_llegada, pedido))  # Agrega el plazo, el orden de llegada y el nombre a la lista.
        self.siguiente_llegada += 1  # Aumenta el contador para que el próximo pedido tenga otro número de llegada.
    def esta_pendiente(self, pedido):  # Define cómo buscar un pedido pendiente por su nombre.
        for plazo, llegada, nombre in self.lista:  # Revisa los pedidos de la lista uno por uno.
            if nombre == pedido:  # Comprueba si el nombre del pedido actual coincide con el buscado.
                return True  # Devuelve verdadero apenas encuentra el pedido.
        return False  # Devuelve falso si recorrió toda la lista y no lo encontró.
    def preparar_siguiente(self):  # Define cómo seleccionar y retirar el pedido más urgente.
        if not self.lista:  # Comprueba si la lista está vacía.
            return None  # Devuelve None porque no hay pedidos para preparar.
        mejor = 0  # Supone inicialmente que el primer pedido de la lista es el más urgente.
        for i in range(1, len(self.lista)):  # Revisa el resto de las posiciones para hallar el pedido más urgente.
            actual = self.lista[i]  # Obtiene el pedido que se está revisando en esta iteración.
            elegido = self.lista[mejor]  # Obtiene el pedido que hasta ahora se considera el más urgente.
            if actual[0] < elegido[0] or (  # Comprueba si el plazo actual es menor, o si hay empate de plazo.
                actual[0] == elegido[0] and actual[1] < elegido[1]  # En caso de empate, prefiere el número de llegada menor.
            ):  # Termina la condición que compara plazo y orden de llegada.
                mejor = i  # Guarda la posición del nuevo pedido más urgente.
        return self.lista.pop(mejor)[2]  # Quita el pedido elegido de la lista y devuelve su nombre.
class ReceptorMejorado:  # Define la versión rápida del receptor.
    """Min-heap para prioridad y set para consultas de pertenencia."""  # Documenta las estructuras que utiliza esta clase.
    def __init__(self):  # Inicializa un receptor mejorado nuevo.
        self.heap = []  # Crea la lista que heapq organizará como un min-heap.
        self.pendientes = set()  # Crea un conjunto para consultar rápidamente los nombres pendientes.
        self.siguiente_llegada = 0  # Guarda el número de llegada que se asignará al próximo pedido.
    def registrar(self, pedido, plazo):  # Define cómo registrar un pedido en el receptor mejorado.
        llegada = self.siguiente_llegada  # Guarda el orden de llegada de este pedido.
        self.siguiente_llegada += 1  # Aumenta el contador para el próximo pedido.
        heappush(self.heap, (plazo, llegada, pedido))  # Inserta el pedido en el heap ordenado por plazo y llegada.
        self.pendientes.add(pedido)  # Añade el nombre al set para poder consultarlo rápidamente.
    def esta_pendiente(self, pedido):  # Define cómo consultar si un pedido está pendiente.
        return pedido in self.pendientes  # Busca el nombre en el set y devuelve verdadero o falso.
    def preparar_siguiente(self):  # Define cómo retirar el pedido más urgente del min-heap.
        if not self.heap:  # Comprueba si el heap está vacío.
            return None  # Devuelve None porque no hay pedidos para preparar.
        plazo, llegada, pedido = heappop(self.heap)  # Extrae del heap el pedido con menor plazo y llegada más temprana.
        self.pendientes.remove(pedido)  # Elimina el nombre del set porque el pedido ya no está pendiente.
        return pedido  # Devuelve el nombre del pedido que se va a preparar.
def crear_carga(cantidad, semilla):  # Define una función que genera pedidos y consultas para una prueba.
    """Crea los mismos pedidos y consultas para ambas soluciones."""  # Documenta que ambas soluciones recibirán la misma carga.
    generador = random.Random(semilla)  # Crea un generador aleatorio con semilla fija para repetir los mismos datos.
    pedidos = [  # Comienza a construir la lista de pedidos de prueba.
        ("Pedido-" + str(i), generador.randint(1, 1000))  # Genera un nombre único y un plazo aleatorio entre 1 y 1000.
        for i in range(cantidad)  # Repite la creación de pedidos la cantidad de veces solicitada.
    ]  # Termina de construir la lista de pedidos.
    cantidad_consultas = cantidad // 3  # Define que habrá una consulta por cada tres pedidos.
    consultas = [  # Comienza a construir la lista de nombres que se consultarán.
        "Pedido-" + str(generador.randrange(cantidad))  # Elige aleatoriamente el nombre de un pedido existente.
        for _ in range(cantidad_consultas)  # Repite la selección hasta completar el número de consultas.
    ]  # Termina de construir la lista de consultas.
    return pedidos, consultas  # Devuelve los pedidos y las consultas creados.
def ejecutar_carga(tipo_receptor, pedidos, consultas):  # Define la función que ejecuta una carga sobre un receptor.
    """Ejecuta registros, consultas y preparaciones; devuelve resultados."""  # Documenta las operaciones realizadas.
    receptor = tipo_receptor()  # Crea un receptor de la clase recibida como argumento.
    for nombre, plazo in pedidos:  # Recorre todos los pedidos de la carga.
        receptor.registrar(nombre, plazo)  # Registra el pedido actual.
    respuestas_consultas = [  # Comienza a guardar los resultados de las consultas.
        receptor.esta_pendiente(nombre) for nombre in consultas  # Consulta cada nombre y guarda verdadero o falso.
    ]  # Termina de crear la lista de respuestas de pertenencia.
    orden_preparacion = []  # Crea una lista vacía para guardar el orden en que se preparan los pedidos.
    while True:  # Repite el proceso hasta que no queden pedidos pendientes.
        pedido = receptor.preparar_siguiente()  # Retira el siguiente pedido más urgente.
        if pedido is None:  # Comprueba si el receptor ya no tenía pedidos.
            break  # Sale del bucle porque ya se prepararon todos.
        orden_preparacion.append(pedido)  # Guarda el pedido retirado en el orden de preparación.
    return respuestas_consultas, orden_preparacion  # Devuelve los resultados para poder comparar ambas soluciones.
def medir(tipo_receptor, pedidos, consultas):  # Define una función que mide el tiempo de una ejecución completa.
    inicio = perf_counter()  # Guarda el instante justo antes de ejecutar la carga.
    resultado = ejecutar_carga(tipo_receptor, pedidos, consultas)  # Ejecuta los registros, consultas y preparaciones.
    segundos = perf_counter() - inicio  # Calcula cuánto tiempo transcurrió desde el inicio.
    return segundos, resultado  # Devuelve el tiempo y los resultados obtenidos.
def main():  # Define la función principal que organiza todas las mediciones.
    tamanos = [2000, 4000, 8000]  # Define tres cargas; cada una duplica el tamaño de la anterior.
    repeticiones = 3  # Indica que se harán tres corridas medidas para calcular el promedio.
    print("Tamaño | Ingenua (s) | Mejorada (s) | Relación")  # Imprime los títulos de las columnas de la tabla.
    print("-------|-------------|--------------|---------")  # Imprime una línea para separar el encabezado.
    for cantidad in tamanos:  # Repite el proceso de medición para cada tamaño de carga.
        pedidos, consultas = crear_carga(cantidad, semilla=2026 + cantidad)  # Genera datos repetibles para este tamaño.
        _, resultado_ingenuo = medir(ReceptorIngenuo, pedidos, consultas)  # Ejecuta una corrida de calentamiento para la versión ingenua.
        _, resultado_mejorado = medir(ReceptorMejorado, pedidos, consultas)  # Ejecuta una corrida de calentamiento para la versión mejorada.
        if resultado_ingenuo != resultado_mejorado:  # Comprueba que ambas soluciones produzcan los mismos resultados.
            raise AssertionError("Las soluciones dieron resultados distintos")  # Detiene el programa si las respuestas no coinciden.
        tiempos_ingenuo = []  # Crea una lista para guardar las tres mediciones de la solución ingenua.
        tiempos_mejorado = []  # Crea una lista para guardar las tres mediciones de la solución mejorada.
        for _ in range(repeticiones):  # Repite las mediciones la cantidad de veces indicada.
            tiempo_i, resultado_i = medir(ReceptorIngenuo, pedidos, consultas)  # Mide una ejecución de la versión ingenua.
            tiempo_m, resultado_m = medir(ReceptorMejorado, pedidos, consultas)  # Mide una ejecución de la versión mejorada.
            if resultado_i != resultado_m:  # Verifica que ambas soluciones sigan entregando los mismos resultados.
                raise AssertionError("Las soluciones dieron resultados distintos")  # Detiene el programa si encuentra una diferencia.
            tiempos_ingenuo.append(tiempo_i)  # Añade el tiempo de esta corrida ingenua a su lista.
            tiempos_mejorado.append(tiempo_m)  # Añade el tiempo de esta corrida mejorada a su lista.
        promedio_i = mean(tiempos_ingenuo)  # Calcula el promedio de las tres mediciones ingenuas.
        promedio_m = mean(tiempos_mejorado)  # Calcula el promedio de las tres mediciones mejoradas.
        relacion = promedio_i / promedio_m if promedio_m else float("inf")  # Divide los tiempos para saber cuántas veces fue más lenta la ingenua.
        print(  # Comienza a imprimir la fila de resultados de este tamaño.
            f"{cantidad:>6} | {promedio_i:>11.6f} | "  # Imprime tamaño y promedio ingenuo con seis decimales.
            f"{promedio_m:>12.6f} | {relacion:>7.2f}x"  # Imprime promedio mejorado y relación con dos decimales.
        )  # Termina de imprimir la fila de resultados.
if __name__ == "__main__":  # Comprueba que el archivo se esté ejecutando directamente.
    main()  # Llama a la función principal para iniciar las mediciones.