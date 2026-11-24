# README GENERAL

## 1. Descripción del proyecto

Este proyecto busca analizar cómo se realiza el control del inventario de Coffeeology y estudiar formas de mejorar este proceso mediante el uso de estructuras de datos y algoritmos.

El trabajo se desarrolla utilizando Python. Se busca entender el problema, probar diferentes soluciones y comparar sus tiempos de ejecución.

## 2. Cómo surgió el problema

Al principio, el proyecto se enfocaba en mejorar la búsqueda de productos al momento de registrar las comandas de los clientes.

Sin embargo, al conocer mejor el funcionamiento de Coffeeology, se identificó que la revisión del inventario también representa una dificultad, ya que requiere bastante tiempo y atención del personal.

Por esta razón, se decidió enfocar el proyecto en el control de inventario y en la identificación de materias primas que necesitan reposición.

## 3. Cómo se realiza actualmente el inventario

Coffeeology puede manejar aproximadamente 450 materias primas, de las cuales alrededor de 350 se utilizan normalmente durante un mes.

Actualmente, el inventario se revisa manualmente y el personal utiliza su experiencia para identificar qué productos hacen falta.

El proceso funciona de la siguiente manera:

1. El turno de la mañana revisa las materias primas y comunica cuáles hacen falta.
2. El encargado de la tarde recibe la información.
3. Durante la tarde se pueden identificar otras necesidades y se comunican al encargado de la noche.
4. El encargado de la noche reúne toda la información y revisa las necesidades.
5. Aproximadamente a las 21:30 prepara la lista de compras.
6. La lista se envía por WhatsApp al personal encargado de realizar las compras.
7. Al día siguiente se reciben las materias primas compradas.

Esta revisión se realiza todos los días antes del cierre y puede tomar entre 30 minutos y una hora.

## 4. Problema identificado

La revisión manual de tantas materias primas puede tomar bastante tiempo y dificultar la identificación de los productos que necesitan reposición.

Además, la información se comunica entre diferentes turnos, por lo que el encargado de la noche debe reunir todos los datos antes de preparar la lista de compras.

Por eso, se busca estudiar formas de organizar y consultar mejor la información del inventario.

## 5. Objetivo del proyecto

Analizar diferentes estructuras de datos y algoritmos que puedan ayudar a mejorar las tareas relacionadas con el inventario de Coffeeology.

Para ello, se desarrollan programas en Python y se realizan pruebas para comparar sus resultados y tiempos de ejecución.

## 6. Desarrollo por hitos

### H1 — Análisis del problema

Se estudió el funcionamiento de Coffeeology, se identificó el problema y se describió cómo se realiza actualmente el control del inventario.

### H2 — Estructuras de datos

Se estudiaron diferentes formas de almacenar y buscar materias primas.

Se realizaron pruebas para comparar el rendimiento de las estructuras de datos y conocer cuál resulta más conveniente para las operaciones del inventario.

### H3 — Estrategias y grafos

Se compararon dos formas de resolver un problema de selección de productos con un presupuesto limitado:

- Fuerza bruta.
- Programación dinámica.

También se representó el proceso de inventario de Coffeeology mediante un grafo dirigido.

Para este ejercicio se trabajó con:

- Lista de adyacencia.
- Matriz de adyacencia.
- Algoritmo BFS (búsqueda en anchura).

Con esto se pudo representar la comunicación entre los turnos, el encargado de compras y la recepción de las materias primas.

**Nota:** Algunos ejercicios utilizan datos simulados para realizar las pruebas. Por lo tanto, sus resultados son académicos y no representan necesariamente datos reales ni sistemas utilizados actualmente por Coffeeology.

## 7. Herramientas utilizadas

- **Lenguaje de programación:** Python.
- **Editor de código:** Visual Studio Code.
- **Control de versiones:** Git y GitHub.

Cada carpeta contiene los documentos y programas correspondientes al trabajo realizado en cada hito.

## 8. Conclusión

Durante el desarrollo del proyecto se estudiaron diferentes formas de resolver problemas relacionados con el inventario de Coffeeology.

Se trabajó con estructuras de datos, algoritmos de búsqueda, programación dinámica y grafos.

Las pruebas permitieron comparar diferentes soluciones y comprender cómo influye la elección de un algoritmo o estructura de datos en el tiempo de ejecución.

El proyecto permite aplicar los conocimientos de la materia a un problema basado en el funcionamiento de un negocio real.
