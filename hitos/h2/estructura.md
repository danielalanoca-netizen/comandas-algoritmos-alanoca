
# Elección de estructuras de datos - COFFEEOLOGY

## 1. Estructura de datos seleccionada

Para administrar el inventario de materias primas de COFFEEOLOGY se seleccionó el **diccionario (`dict`) de Python** como estructura de datos principal.

El diccionario almacenará cada materia prima utilizando su código como clave y sus demás datos como valor.

Ejemplo de representación:

```python
# Diccionario que representa el inventario de materias primas.
inventario = {
    "MP-0001": {
        "nombre": "Harina",
        "cantidad": 25,
        "unidad": "kg",
        "stock_minimo": 5,
        "estado": "Disponible"
    },
    "MP-0002": {
        "nombre": "Azúcar",
        "cantidad": 12,
        "unidad": "kg",
        "stock_minimo": 4,
        "estado": "Disponible"
    }
}
```

De esta manera, cada materia prima puede localizarse directamente mediante su código, sin recorrer todos los registros del inventario.

## 2. Justificación de la elección

Se eligió un diccionario porque la operación prioritaria del caso es buscar materias primas por código.

El inventario de COFFEEOLOGY puede alcanzar aproximadamente 450 materias primas. Por ello, es importante contar con una estructura que permita consultar y actualizar registros de manera eficiente.

Las principales ventajas de esta estructura son:

- Permite buscar una materia prima por código con un costo promedio O(1).
- Permite insertar y eliminar registros mediante su clave.
- Facilita actualizar la cantidad disponible de una materia prima.
- Permite recorrer todos los registros para identificar faltantes y preparar listas de compras.
- Es una estructura incorporada en Python y no requiere implementar una estructura adicional.

Las operaciones que necesitan ordenar o comparar cantidades pueden realizarse mediante recorridos del inventario. Aunque estas operaciones tienen un costo mayor, su frecuencia y el tamaño del catálogo permiten mantener una implementación sencilla.

## 3. Costos de las operaciones frecuentes

Las siguientes operaciones se realizan de manera frecuente dentro del proceso de control del inventario.

| Operación frecuente | Complejidad temporal | Justificación |
|---|---|---|
| Buscar por código | O(1) promedio | Se accede directamente al registro mediante su clave. |
| Actualizar cantidad | O(1) promedio | Se localiza el registro mediante su código y se modifica su cantidad. |
| Recorrer el inventario | O(n) | Es necesario visitar todos los registros. |
| Identificar faltantes | O(n) | Se revisa cada materia prima y se compara su cantidad con el stock mínimo. |
| Generar lista de compras | O(n) | Se recorren los registros para identificar las materias primas que necesitan reposición. |

Estas operaciones justifican la elección del diccionario porque permite realizar las consultas y actualizaciones individuales de forma eficiente, mientras que los recorridos completos se mantienen en O(n).

## 4. Costos de las operaciones ocasionales

Existen otras operaciones que también necesita el inventario, pero que se realizan con menor frecuencia.

| Operación ocasional | Complejidad temporal | Justificación |
|---|---|---|
| Insertar materia prima | O(1) promedio | Se agrega un registro utilizando su código como clave. |
| Eliminar materia prima | O(1) promedio | Se elimina el registro mediante su código. |
| Consultar la cantidad mínima | O(n) | Se recorren todos los registros para encontrar la menor cantidad. |
| Consultar el sucesor | O(n) | Se revisan los registros para encontrar la siguiente cantidad mayor. |
| Consultar un rango | O(n) | Se recorren los registros para seleccionar las cantidades dentro del rango. |
| Recorrer en orden por cantidad | O(n log n) | Se ordenan los registros por cantidad antes de recorrerlos. |

Las operaciones de mínimo, sucesor y rango pueden resolverse mediante recorridos sin necesidad de incorporar una estructura adicional.

## 5. Comparación con la solución ingenua

Para justificar la elección se compara el diccionario con una lista, considerando la búsqueda de materias primas por código.

| Criterio | Lista (`list`) | Diccionario (`dict`) |
|---|---|---|
| Búsqueda por código | O(n) | O(1) promedio |
| Inserción | O(1) al final, en promedio | O(1) promedio |
| Eliminación por código | O(n) | O(1) promedio |
| Actualización por código | O(n) para localizar el registro | O(1) promedio |
| Acceso mediante clave | No disponible directamente | Disponible |

En una lista, para encontrar una materia prima puede ser necesario revisar hasta los 450 registros del inventario.

En un diccionario, el código funciona como clave y permite localizar el registro con un costo promedio constante, sin depender proporcionalmente de la cantidad de materias primas.

Por esta razón, el diccionario resulta más conveniente para las búsquedas frecuentes del inventario.

## 6. Relación con el experimento

Para comprobar la diferencia entre ambas estructuras se realizó un experimento utilizando la operación de búsqueda por código.

Se compararon los siguientes tamaños:

- 50 materias primas.
- 100 materias primas.
- 200 materias primas.
- 400 materias primas.

En cada prueba se realizaron 1000 consultas, utilizando los mismos códigos para ambas estructuras.

Los resultados mostraron que el diccionario mantuvo tiempos relativamente estables, mientras que la lista aumentó su tiempo conforme creció el inventario.

Esta observación coincide con las complejidades esperadas:

- Lista: O(n), porque necesita recorrer los registros hasta encontrar el código.
- Diccionario: O(1) promedio, porque utiliza el código como clave.

Los resultados y el procedimiento completo se encuentran en `medicion.md` y `medicion.py`.

## 7. Conclusión

Se seleccionó el diccionario como estructura principal para el inventario de COFFEEOLOGY porque permite realizar búsquedas y actualizaciones por código con un costo promedio O(1). Las operaciones que necesitan recorrer u ordenar los registros tienen costos mayores, pero pueden resolverse sin incorporar estructuras adicionales. La comparación experimental también mostró una ventaja del diccionario frente a la lista para la búsqueda por código. Por lo tanto, esta estructura ofrece un equilibrio adecuado entre rendimiento y simplicidad para el tamaño del inventario.