# Inventario de COFFEEOLOGY

## 1. Datos del inventario

Para representar el inventario en el modelo propuesto se consideran los siguientes datos:

| Dato | Descripción |
|---|---|
| Código | Identificador único asignado a cada materia prima. |
| Nombre | Nombre de la materia prima. |
| Cantidad disponible | Cantidad existente de la materia prima. |
| Unidad de medida | Unidad utilizada para representar la cantidad, por ejemplo kg, unidades o bolsas. |
| Stock mínimo | Cantidad mínima establecida para identificar cuándo se necesita reposición. |
| Estado | Situación de la materia prima, por ejemplo disponible o pendiente de reposición. |

El catálogo de COFFEEOLOGY puede contener aproximadamente 450 materias primas, de las cuales alrededor de 350 se utilizan habitualmente durante un mes. No todas se consumen o reponen mensualmente.

Actualmente, el control de existencias depende de las revisiones de los empleados y de la comunicación entre turnos. Los campos anteriores corresponden al modelo de inventario propuesto y no significan que actualmente exista un sistema digital que los almacene.

## 2. Operaciones del inventario

Para analizar el proceso mediante estructuras de datos se consideran las siguientes operaciones:

| Operación | Descripción |
|---|---|
| Buscar por clave | Encontrar una materia prima utilizando su código único. |
| Insertar | Registrar una nueva materia prima en el inventario. |
| Borrar | Eliminar una materia prima que ya no forma parte del inventario. |
| Consultar el menor | Encontrar la materia prima que tiene la menor cantidad disponible. |
| Consultar el sucesor | Encontrar la siguiente materia prima según el orden establecido por su cantidad disponible. |
| Consultar un rango | Obtener las materias primas cuya cantidad disponible se encuentra entre dos valores determinados. |
| Recorrer en orden | Revisar todas las materias primas ordenadas según su cantidad disponible. |
| Actualizar cantidad | Modificar la cantidad disponible de una materia prima. |
| Identificar faltantes | Comparar la cantidad disponible con el stock mínimo para identificar materias primas que necesitan reposición. |
| Generar lista de compras | Reunir las materias primas identificadas para preparar la solicitud de adquisición. |

Las consultas de menor, sucesor, rango y recorrido ordenado se consideran operaciones del modelo propuesto para facilitar el análisis de las existencias.

## 3. Frecuencia de las operaciones

Las siguientes frecuencias son estimaciones cualitativas basadas en el proceso actual de COFFEEOLOGY y en las necesidades del modelo de inventario propuesto. No representan mediciones exactas de un sistema digital existente.

| Operación | Frecuencia estimada | Justificación |
|---|---|---|
| Buscar por clave | Varias veces al día | Permitiría localizar una materia prima específica durante las revisiones de existencias. |
| Actualizar cantidad | Varias veces al día | Las cantidades disponibles cambian conforme se utilizan o reciben materias primas. |
| Recorrer en orden | Varias veces al día | Permitiría revisar las materias primas según su cantidad disponible. |
| Identificar faltantes | Varias veces al día | Durante las revisiones de los turnos se identifican productos que necesitan reposición. |
| Consultar el menor | Ocasionalmente | Permitiría identificar la materia prima con menor cantidad disponible. |
| Consultar el sucesor | Ocasionalmente | Permitiría continuar la revisión desde una materia prima hacia la siguiente según la cantidad disponible. |
| Consultar un rango | Ocasionalmente | Permitiría consultar materias primas cuyas cantidades se encuentren dentro de un intervalo. |
| Insertar | Pocas veces | Se realiza cuando se incorpora una nueva materia prima al catálogo. |
| Borrar | Pocas veces | Se realiza cuando una materia prima deja de formar parte del inventario. |
| Generar lista de compras | Una vez al día | El encargado del turno de la noche consolida los productos necesarios aproximadamente a las 21:30. |

## 4. Operaciones más importantes para el análisis

De acuerdo con el funcionamiento de COFFEEOLOGY y las necesidades del modelo propuesto, las operaciones que merecen mayor atención son:

1. **Buscar por clave:** permite localizar una materia prima específica durante las revisiones del inventario.
2. **Actualizar cantidad:** permite mantener actualizada la cantidad disponible de cada materia prima.
3. **Recorrer en orden:** facilita revisar las materias primas según su cantidad disponible.
4. **Identificar faltantes:** permite reconocer las materias primas que necesitan reposición.
5. **Consultar el menor:** facilita localizar las materias primas con menos existencias.
6. **Generar lista de compras:** permite consolidar los productos que deben adquirirse al finalizar el día.
