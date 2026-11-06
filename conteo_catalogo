# Catálogo Coffeeology — conteo según menú compartido

## Resultado de la contabilización

- **Registros comerciales de productos (presentaciones/variantes): 128**
- **Registros de extras y complementos: 7**
- **Total de registros seleccionables en el CSV: 135**
- **Nombres distintos de productos principales: 96**

El conteo considera cada presentación o variante seleccionable como un registro independiente. Los extras también se incluyen como registros independientes con `tipo=Extra`.

## Conteo por sección
- Bakery: 5 registros\n- Bebidas frías con café: 10 registros\n- Bebidas frías sin café: 13 registros\n- Brunch (hasta 13:00): 4 registros\n- Cakes: 9 registros\n- Chocolate: 12 registros\n- Con leche: 11 registros\n- Croissants especiales: 5 registros\n- Desayunos (hasta 13:00): 4 registros\n- Elemental lattes: 8 registros\n- Espresso: 9 registros\n- Extras: 5 registros\n- Extras/complementos: 1 registros\n- Gaseosas/aguas: 2 registros\n- Infusiones: 2 registros\n- Lattes de la casa: 6 registros\n- Menú fit - bebidas calientes: 6 registros\n- Menú fit - bebidas frías: 2 registros\n- Menú fit - extras: 1 registros\n- Menú fit - snacks: 4 registros\n- Recetas internacionales: 8 registros\n- Salados: 3 registros\n- Sandwiches (desde 14:00): 5 registros\n
## Reglas aplicadas

1. Tamaños C, G y X se cuentan por separado.
2. Shot y Doppio se cuentan por separado.
3. Frío y caliente se cuentan por separado cuando el menú los ofrece.
4. Con agua y con leche se cuentan por separado.
5. Entera y media se cuentan por separado.
6. Las dos variantes de Iced tea (tradicional y frutal) se cuentan por separado porque el menú las describe como opciones.
7. `Pizza en pan de laja` aparece en Brunch y Sandwiches; se cuenta una sola vez para evitar duplicación.
8. Extras (incluidos scoop de proteína y papas fritas) se conservan, pero se identifican como `Extra`.
9. Cuando el precio no es legible o no aparece, se deja vacío; no se inventa.
10. Los códigos COF001... son identificadores creados para esta muestra, no códigos oficiales de Coffeeology.

## Advertencias para validar con el negocio

- En Elemental Lattes, el menú muestra precios para Aurum latte (frío 30 Bs / caliente 28 Bs), pero no se distinguen precios individuales para Carbon, Cuprum, Iodum, Phosphorus, Radium y Cristal latte. Se dejaron vacíos.
- Radium latte, Aurum latte y Phosphorus latte también aparecen en Menú Fit con presentaciones/precios distintos. Se conservaron las entradas de Menú Fit y Elemental Lattes por sus contextos y presentaciones distintas; confirmar si el negocio las maneja como la misma ficha de producto o como versiones diferentes.
- Las abreviaturas C, G, X, J y D se conservaron tal como aparecen en el menú, sin asumir equivalencias que no están definidas.
- Este conteo es el número de opciones comerciales visibles en el menú compartido, no necesariamente el número de SKU activos en el sistema POS ni la cantidad física de inventario.

## Archivo de datos

`catalogo_coffeeology.csv` contiene el listado completo, con código de muestra, producto, categoría, presentación/variante, precio, tipo y observaciones.
