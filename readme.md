# README GENERAL

## 1. Descripción del proyecto

Este proyecto tiene como objetivo analizar y estudiar posibles mejoras en los procesos de gestión de inventario de Coffeeology mediante la aplicación de estructuras de datos y algoritmos.

El trabajo se desarrolla utilizando Python y se enfoca en comprender el funcionamiento del proceso actual, identificar sus dificultades y evaluar alternativas algorítmicas mediante pruebas y mediciones de rendimiento.

## 2. Evolución del problema

Inicialmente, el proyecto estaba orientado a optimizar la búsqueda y verificación de productos al momento de registrar las comandas de los clientes.

Sin embargo, durante el análisis del funcionamiento de Coffeeology se identificó que el control y la revisión del inventario representan un proceso que requiere más tiempo y atención del personal.

Por este motivo, se decidió actualizar el enfoque del proyecto hacia la gestión del inventario, priorizando el análisis de las operaciones que realiza el personal para identificar materias primas faltantes y preparar las solicitudes de compra.

## 3. Descripción del proceso actual

Coffeeology maneja un inventario de materias primas que puede alcanzar aproximadamente 450 registros, con un uso habitual de alrededor de 350 materias primas durante un mes.

Actualmente, el control del inventario se realiza mediante revisiones manuales y la experiencia del personal.

El proceso funciona de la siguiente manera:

1. Durante el turno de la mañana se identifican las materias primas faltantes o que necesitan reposición.
2. La información se comunica al encargado del turno de la tarde.
3. Durante el turno de la tarde se pueden identificar otras necesidades y se informa al encargado del turno de la noche.
4. El encargado del turno de la noche consolida la información y revisa las necesidades del inventario.
5. Aproximadamente a las 21:30 se prepara una lista de compra.
6. La lista se envía mediante WhatsApp al personal encargado de realizar las compras.
7. Al día siguiente, los turnos reciben las materias primas adquiridas.

La revisión del inventario se realiza diariamente antes del cierre. Este proceso puede requerir entre 30 minutos y una hora de trabajo del encargado.

## 4. Problema identificado

La revisión manual de una cantidad considerable de materias primas puede consumir tiempo y dificultar la identificación de productos faltantes.

Además, la información debe recopilarse entre distintos turnos, lo que hace necesario consolidar los datos antes de preparar la lista de compra.

Por ello, se considera importante analizar estructuras de datos y algoritmos que permitan mejorar la búsqueda, actualización y consulta de la información del inventario.

## 5. Objetivo general

Analizar y evaluar estructuras de datos y algoritmos que permitan mejorar la eficiencia de las operaciones relacionadas con la gestión del inventario de Coffeeology, mediante implementaciones en Python y mediciones de rendimiento.

## 6. Desarrollo por hitos

### H1 — Análisis inicial del problema

Análisis del contexto de Coffeeology, identificación del proceso que se desea estudiar y descripción de las dificultades encontradas.

### H2 — Estructuras de datos

Análisis de las operaciones del inventario y evaluación de estructuras de datos para almacenar, buscar y administrar las materias primas.

Se estudia el rendimiento de las alternativas mediante pruebas experimentales y comparación de tiempos de ejecución.

### H3 — Estrategias de optimización

Análisis de estrategias algorítmicas mediante problemas de optimización relacionados con el contexto de Coffeeology.

Se realizan comparaciones entre fuerza bruta y programación dinámica, además de estudiar la representación de procesos mediante grafos.

**Nota:** Los problemas de optimización utilizados en los experimentos académicos pueden emplear datos simulados. Estos resultados no representan necesariamente operaciones implementadas actualmente en Coffeeology.

## 7. Tecnologías utilizadas

- **Lenguaje de programación:** Python.
- **Editor de código:** Visual Studio Code.
- **Control de versiones:** Git y GitHub.
- **Análisis:** estructuras de datos, algoritmos y mediciones de rendimiento.

## 8. Organización del proyecto

La documentación y los ejercicios se organizan por hitos y prácticas de la asignatura.

- `hitos/h2/`: documentación y experimentos del segundo hito.
- `hitos/h3/`: documentación y experimentos del tercer hito.
