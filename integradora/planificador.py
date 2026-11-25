
# Daniel Antony Alanoca Alfaro

# Importamos dataclass para crear objetos que representen los paquetes.
from dataclasses import dataclass


# Representamos cada paquete con su código, peso y ganancia.
@dataclass
class Paquete:
    codigo: str
    kg: int
    ganancia: int


# Creamos nuestro planificador mejorado.
class PlanificadorMejorado:

    def __init__(self):
        # Este conjunto guardará los códigos de los paquetes seleccionados.
        self.elegidos = set()

    def elegir(self, paquetes, capacidad_kg):

        # Reiniciamos los paquetes seleccionados en cada ejecución.
        self.elegidos = set()

        # Comprobamos que la capacidad no sea negativa.
        if capacidad_kg < 0:
            raise ValueError("La capacidad no puede ser negativa.")

        # Obtenemos la cantidad de paquetes.
        n = len(paquetes)

        # Creamos una tabla con la mejor ganancia para cada capacidad.
        # Inicialmente, todas las ganancias son cero.
        dp = [0] * (capacidad_kg + 1)

        # Creamos una matriz para recordar qué paquetes fueron seleccionados.
        # Cada fila representa un paquete.
        # Cada columna representa una capacidad.
        decisiones = [
            bytearray(capacidad_kg + 1)
            for _ in range(n)
        ]

        # Recorremos todos los paquetes.
        for i in range(n):

            # Obtenemos el peso y la ganancia del paquete actual.
            peso = paquetes[i].kg
            ganancia = paquetes[i].ganancia

            # Comprobamos que el peso sea válido.
            if peso <= 0:
                raise ValueError("El peso debe ser mayor que cero.")

            # Recorremos las capacidades de mayor a menor.
            # Esto evita utilizar el mismo paquete más de una vez.
            for capacidad in range(capacidad_kg, peso - 1, -1):

                # Calculamos la ganancia si llevamos este paquete.
                nueva_ganancia = dp[capacidad - peso] + ganancia

                # Comparamos con la mejor ganancia que ya teníamos.
                if nueva_ganancia > dp[capacidad]:

                    # Guardamos la nueva ganancia si es mejor.
                    dp[capacidad] = nueva_ganancia

                    # Registramos que este paquete fue seleccionado
                    # para alcanzar esta capacidad.
                    decisiones[i][capacidad] = 1

        # La última posición contiene la ganancia máxima.
        mejor_ganancia = dp[capacidad_kg]

        # Recuperamos los paquetes que forman la mejor solución.
        capacidad_actual = capacidad_kg

        # Revisamos las decisiones desde el último paquete hacia atrás.
        for i in range(n - 1, -1, -1):

            # Comprobamos si el paquete actual fue seleccionado.
            if decisiones[i][capacidad_actual] == 1:

                # Guardamos el código del paquete seleccionado.
                self.elegidos.add(paquetes[i].codigo)

                # Reducimos la capacidad disponible.
                capacidad_actual -= paquetes[i].kg

        # Devolvemos la ganancia máxima y los códigos seleccionados.
        return mejor_ganancia, list(self.elegidos)

    def esta_en_el_viaje(self, codigo):

        # Consultamos si el código pertenece al conjunto.
        # La búsqueda promedio tiene complejidad O(1).
        return codigo in self.elegidos
