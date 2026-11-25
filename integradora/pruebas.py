
# Daniel Antony Alanoca Alfaro

# Importamos la clase y los paquetes de nuestro planificador.
from planificador import Paquete, PlanificadorMejorado


# Creamos los seis casos de prueba del profesor.
casos = [
    (
        "El voraz se equivoca",
        [
            Paquete("P1", 10, 60),
            Paquete("P2", 20, 100),
            Paquete("P3", 30, 120)
        ],
        50, 220, {"P2", "P3"}
    ),
    (
        "Cuatro paquetes",
        [
            Paquete("P1", 2, 3),
            Paquete("P2", 3, 4),
            Paquete("P3", 4, 5),
            Paquete("P4", 5, 6)
        ],
        8, 10, {"P2", "P4"}
    ),
    (
        "Capacidad cero",
        [
            Paquete("P1", 5, 10),
            Paquete("P2", 7, 12)
        ],
        0, 0, set()
    ),
    (
        "Sin paquetes",
        [],
        30, 0, set()
    ),
    (
        "Nada cabe",
        [
            Paquete("P1", 40, 90),
            Paquete("P2", 50, 100)
        ],
        30, 0, set()
    ),
    (
        "Entran todos",
        [
            Paquete("P1", 5, 10),
            Paquete("P2", 7, 12),
            Paquete("P3", 3, 4)
        ],
        100, 26, {"P1", "P2", "P3"}
    )
]


# Contamos las pruebas correctas.
correctas = 0
total = 0


# Ejecutamos los seis casos.
for nombre, paquetes, capacidad, esperada, codigos in casos:

    # Creamos una instancia nueva del planificador.
    planificador = PlanificadorMejorado()

    # Ejecutamos la selección de paquetes.
    ganancia, elegidos = planificador.elegir(paquetes, capacidad)

    # Comprobamos la ganancia y los paquetes seleccionados.
    resultado = (
        ganancia == esperada
        and set(elegidos) == codigos
    )

    # Actualizamos el contador.
    total += 1

    if resultado:
        correctas += 1
        print(f"CORRECTO: {nombre}")
    else:
        print(f"ERROR: {nombre}")
        print("Ganancia obtenida:", ganancia)
        print("Paquetes obtenidos:", elegidos)


# Comprobamos las dos consultas adicionales
planificador = PlanificadorMejorado()

# Ejecutamos el primer caso para cargar los paquetes seleccionados.
planificador.elegir(casos[0][1], casos[0][2])

# Consultamos si P2 está seleccionado.
total += 1

if planificador.esta_en_el_viaje("P2"):
    correctas += 1
    print("CORRECTO: EstaEnElViaje(P2)")
else:
    print("ERROR: EstaEnElViaje(P2)")


# Consultamos si P1 está seleccionado.
total += 1

if not planificador.esta_en_el_viaje("P1"):
    correctas += 1
    print("CORRECTO: EstaEnElViaje(P1)")
else:
    print("ERROR: EstaEnElViaje(P1)")


# Mostramos el resultado final.
print("\nRESULTADO FINAL")
print(f"{correctas} de {total} pruebas correctas")
