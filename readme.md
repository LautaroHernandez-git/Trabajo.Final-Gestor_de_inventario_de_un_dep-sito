# Sistema de Gestión de Stock para Depósito

# Descripción general

El proyecto consiste en una aplicación de consola que permite administrar el stock de productos de un depósito.

El sistema registra:
- productos,
- entradas de mercadería,
- salidas de mercadería,
- movimientos realizados,
- productos que necesitan reposición.

Toda la información se guarda utilizando archivos binarios, sin usar bases de datos.

---

# Objetivo del sistema

El objetivo principal es mantener actualizado el inventario del depósito de manera simple y eficiente.

La aplicación permite:
- consultar productos rápidamente,
- actualizar stock automáticamente,
- controlar faltantes,
- mantener un historial de movimientos,
- ordenar y visualizar inventario.

---

# Extensión adicional elegida

## Historial persistente de movimientos

Además del manejo básico del stock, el sistema guarda todas las entradas y salidas en un archivo binario adicional.

Esto permite:
- consultar movimientos de un producto,
- visualizar historial,
- registrar actividad del depósito,
- mejorar el control del sistema.

---

# Arquitectura del programa

## Estructura de archivos

```text
deposito/

├── main.py
├── productos.py
├── movimientos.py
├── archivos.py
├── ordenamientos.py
├── utilidades.py
│
├── productos.dat
└── movimientos.dat
```

---

# Explicación de cada módulo

---

## main.py

Es el archivo principal del programa.

### Funciones
- mostrar el menú,
- pedir datos al usuario,
- coordinar operaciones,
- conectar todos los módulos.

### Menú principal

```text
1. Agregar producto
2. Registrar entrada
3. Registrar salida
4. Buscar producto
5. Ver inventario
6. Ver productos a reponer
7. Ver historial de movimientos
0. Salir
```

---

## productos.py

Contiene toda la lógica relacionada con productos.

### Funciones principales
- agregar productos,
- buscar productos,
- actualizar stock,
- listar inventario,
- detectar productos a reponer.

### También se encarga de
- validar datos,
- controlar stock,
- utilizar el índice en memoria.

---

## movimientos.py

Maneja el historial de movimientos.

### Funciones
- registrar entradas,
- registrar salidas,
- consultar historial,
- mostrar movimientos de un producto.

### Información registrada

```text
- código del producto
- tipo de movimiento
- cantidad
- fecha
```

---

## archivos.py

Administra la persistencia de datos.

### Funciones
- guardar productos,
- leer productos,
- actualizar productos,
- guardar movimientos.

### Tecnologías utilizadas
- archivos binarios,
- módulo `struct`,
- registros de longitud fija.

---

## ordenamientos.py

Implementa algoritmos de ordenamiento propios.

### Permite ordenar
- por descripción,
- por cantidad en stock.

### Algoritmos posibles
- QuickSort,
- MergeSort.

---

## utilidades.py

Contiene funciones auxiliares.

### Ejemplos
- validaciones,
- impresión de datos,
- formateo,
- carga del índice.

---

# Funcionamiento general de la aplicación

---

# Inicio del programa

Cuando el sistema inicia:

1. se abre el archivo de productos,
2. se cargan los productos existentes,
3. se genera un índice en memoria,
4. se muestra el menú principal.

---

# Índice en memoria

El sistema utiliza un diccionario para localizar productos rápidamente.

## Estructura

```python
{
    codigo_producto: posicion_en_archivo
}
```

Esto permite búsquedas en tiempo:

```text
O(1)
```

---

# Alta de productos

Cuando se agrega un producto:

1. el usuario ingresa los datos,
2. se validan valores,
3. se guarda el producto en el archivo binario,
4. se actualiza el índice en memoria.

---

# Registro de entradas

Cuando ingresa mercadería:

1. se busca el producto,
2. se aumenta el stock,
3. se actualiza el archivo,
4. se registra el movimiento.

---

# Registro de salidas

Cuando sale mercadería:

1. se valida el stock disponible,
2. se descuenta la cantidad,
3. se actualiza el producto,
4. se guarda el movimiento.

---

# Política ante falta de stock

Si una salida supera el stock disponible:

```text
cantidad_salida > stock_actual
```

el sistema:
- rechaza la operación,
- muestra un mensaje de error,
- no modifica el stock.

Esto evita inconsistencias.

---

# Productos a reponer

El sistema detecta automáticamente productos con stock bajo.

## Condición

```text
stock_actual < stock_minimo
```

## Caso límite

Si:

```text
stock_actual == stock_minimo
```

el producto NO aparece como “a reponer”.

---

# Historial de movimientos

Cada entrada o salida queda registrada en:

```text
movimientos.dat
```

Esto permite:
- consultar movimientos,
- revisar actividad,
- controlar cambios de stock.

---

# Ordenamiento del inventario

El inventario puede mostrarse:
- ordenado alfabéticamente,
- ordenado por stock.

Para esto se implementa un algoritmo de ordenamiento propio.

---

# Manejo de archivos binarios

---

# Archivo de productos

```text
productos.dat
```

Cada registro contiene:

```text
[codigo][descripcion][stock][stock_minimo][precio]
```

Todos los registros tienen tamaño fijo.

---

# Archivo de movimientos

```text
movimientos.dat
```

Cada registro contiene:

```text
[codigo_producto][tipo][cantidad][fecha]
```

---

# Cómo se abordan los contenidos de la materia

---

# 1. Archivos binarios y struct

Se utilizan archivos binarios para guardar productos y movimientos.

El módulo `struct` permite:
- empaquetar datos,
- escribir registros de tamaño fijo,
- leer información eficientemente.

---

# 2. Diccionarios

Se usa un diccionario como índice en memoria.

Esto permite:
- búsquedas rápidas,
- acceso directo,
- mejor rendimiento.

---

# 3. Algoritmos de ordenamiento

El sistema implementa un algoritmo propio para ordenar:
- por descripción,
- por stock.

---

# 4. Búsqueda

La búsqueda de productos se realiza utilizando el índice en memoria.

Complejidad:

```text
O(1)
```

---

# 5. Recorridos con acumuladores

Se utilizan recorridos para:
- listar inventario,
- detectar productos a reponer,
- consultar historial,
- generar reportes.

---

# 6. Modularización

El sistema se divide en módulos independientes.

Esto mejora:
- organización,
- mantenimiento,
- reutilización,
- claridad del código.

---

# Flujo general del sistema

```text
Usuario
   ↓
Menú principal
   ↓
Funciones del sistema
   ↓
Archivos binarios
```

## Casos de análisis de referencia

### Caso normal: entrada de mercadería

**Situación**
Registrar una entrada de stock para un producto existente.

**Ejemplo**
- Stock actual: 50
- Entrada: 20

**Resultado esperado**
Stock final: 70
Se registra el movimiento en `movimientos.dat`.

---

### Caso límite: stock exactamente en el mínimo

**Ejemplo**
- Stock actual: 15
- Stock mínimo: 10
- Salida: 5

**Resultado esperado**
Stock final: 10
El producto **NO** aparece como “a reponer”.

---

### Caso límite: stock por debajo del mínimo

**Ejemplo**
- Stock actual: 15
- Stock mínimo: 10
- Salida: 7

**Resultado esperado**
Stock final: 8

El producto aparece en el listado de reposición.

---

### Caso extremo: salida mayor al stock disponible

**Ejemplo**
- Stock actual: 12
- Salida solicitada: 20

**Resultado esperado**
El sistema debe:

- rechazar la operación
- informar error
- no modificar stock
- no registrar movimiento

---

### Caso de búsqueda eficiente

**Situación**
Consulta de un producto por código.

**Resultado esperado**
Resolución mediante acceso al índice en memoria con complejidad:
**O(1)**

---

# Conclusión

La arquitectura propuesta permite desarrollar un sistema modular, organizado y eficiente para gestionar el stock de un depósito.

La aplicación cumple con todos los requisitos obligatorios del proyecto y agrega una extensión útil mediante el historial persistente de movimientos.

El uso de archivos binarios, índices en memoria y algoritmos de ordenamiento permite aplicar los principales contenidos vistos en la materia.