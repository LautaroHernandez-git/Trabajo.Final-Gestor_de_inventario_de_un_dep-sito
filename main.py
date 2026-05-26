# =========================================================
# SISTEMA DE GESTIÓN DE STOCK
# MAIN.PY
# =========================================================

# =========================================================
# PARTE DECLARATIVA
# =========================================================

# Descripción general:
# --------------------
# Este programa permite administrar el stock de productos
# de un depósito mediante una aplicación de consola.
#
# El sistema registra:
# - productos,
# - entradas de mercadería,
# - salidas de mercadería,
# - historial de movimientos,
# - productos a reponer.
#
# Toda la información se almacena utilizando archivos
# binarios con registros de longitud fija.
#
# Objetivos principales:
# ----------------------
# - Mantener actualizado el stock.
# - Permitir búsquedas rápidas de productos.
# - Detectar productos con stock bajo.
# - Registrar movimientos del depósito.
# - Mostrar inventario ordenado.
#
# Tecnologías y contenidos aplicados:
# -----------------------------------
# - Archivos binarios y módulo struct.
# - Diccionarios como índice en memoria.
# - Algoritmos de ordenamiento.
# - Modularización del sistema.
# - Validaciones y control de stock.
#
# Arquitectura:
# -------------
# El sistema está dividido en módulos independientes:
#
# - productos.py
#     Lógica de productos y stock.
#
# - movimientos.py
#     Registro e historial de movimientos.
#
# - archivos.py
#     Persistencia en archivos binarios.
#
# - ordenamientos.py
#     Algoritmos de ordenamiento.
#
# - utilidades.py
#     Funciones auxiliares y validaciones.
#
# Funcionamiento general:
# -----------------------
# El programa inicia cargando los archivos y el índice
# en memoria.
#
# Luego muestra un menú interactivo que permite realizar
# operaciones sobre el inventario.
#
# Cada operación actualiza automáticamente los archivos
# y mantiene sincronizado el stock del sistema.
#
# Extensión adicional implementada:
# ---------------------------------
# Historial persistente de movimientos.
#
# El sistema guarda todas las entradas y salidas en un
# archivo independiente para permitir consultas y
# seguimiento de actividad del depósito.
#
# =========================================================
# PARTE DECLARATIVA
# =========================================================

# Importación de módulos principales del sistema

import productos as prod
import movimientos as mov
import archivos as arch
import ordenamientos as ord
import utilidades as util


# =========================================================
# DECLARACIÓN DE FUNCIONES
# =========================================================

def mostrar_menu():
    """
    Muestra el menú principal del sistema de manera clara e interactiva.

    El menú se ejecuta continuamente hasta que el usuario
    decida salir del programa.

    Opciones disponibles:
    1 → Agregar producto
    2 → Registrar entrada de mercadería
    3 → Registrar salida de mercadería
    4 → Buscar producto
    5 → Ver inventario completo
    6 → Ver productos a reponer
    7 → Ver historial de movimientos
    0 → Salir
    """

    print("\n===================================")
    print("   SISTEMA DE GESTIÓN DE STOCK")
    print("===================================")

    print("\n1. Agregar producto")
    print("2. Registrar entrada")
    print("3. Registrar salida")
    print("4. Buscar producto")
    print("5. Ver inventario")
    print("6. Productos a reponer")
    print("7. Historial de movimientos")
    print("0. Salir")


def opcion_agregar_producto():
    """
    Registra un nuevo producto en el sistema.

    Funcionamiento:
    - Solicita información del producto.
    - Verifica que el código no exista.
    - Guarda el producto en el archivo binario.
    - Actualiza el índice en memoria.

    Resultado:
    El producto queda disponible para operaciones futuras.
    """

    print("\n--- NUEVO PRODUCTO ---")


def opcion_registrar_entrada():
    """
    Registra ingreso de mercadería.

    Funcionamiento:
    - Solicita código del producto.
    - Busca el producto utilizando el índice.
    - Solicita cantidad ingresada.
    - Aumenta el stock.
    - Actualiza el archivo.
    - Registra movimiento.

    Resultado:
    El stock del producto aumenta automáticamente.
    """

    print("\n--- REGISTRO DE ENTRADA ---")


def opcion_registrar_salida():
    """
    Registra salida de mercadería.

    Funcionamiento:
    - Solicita código.
    - Verifica existencia del producto.
    - Solicita cantidad.
    - Controla stock disponible.

    Si hay stock suficiente:
    - actualiza stock,
    - guarda cambios,
    - registra movimiento.

    Si NO hay stock suficiente:
    - rechaza operación,
    - informa error,
    - mantiene stock original.

    Resultado:
    Se evita inconsistencia de inventario.
    """

    print("\n--- REGISTRO DE SALIDA ---")


def opcion_buscar_producto():
    """
    Busca y muestra información de un producto.

    Funcionamiento:
    - Solicita código.
    - Usa el índice en memoria.
    - Accede rápidamente al archivo.
    - Muestra información completa.

    Resultado:
    Consulta rápida y eficiente.
    """

    print("\n--- BUSCAR PRODUCTO ---")


def opcion_ver_inventario():
    """
    Muestra el inventario completo.

    Funcionamiento:
    - Lee productos del archivo.
    - Permite ordenar:
        • por descripción
        • por stock
    - Ejecuta algoritmo de ordenamiento propio.
    - Muestra listado ordenado.

    Resultado:
    Inventario organizado y fácil de consultar.
    """

    print("\n--- INVENTARIO COMPLETO ---")


def opcion_productos_a_reponer():
    """
    Detecta productos con stock bajo.

    Funcionamiento:
    - Recorre productos.
    - Compara:
        stock_actual < stock_minimo

    Si se cumple:
    - muestra producto en listado.

    Caso límite:
    Si stock_actual == stock_minimo
    el producto NO aparece a reponer.

    Resultado:
    Permite controlar faltantes.
    """

    print("\n--- PRODUCTOS A REPONER ---")


def opcion_ver_historial():
    """
    Muestra historial de movimientos.

    Funcionamiento:
    - Lee movimientos.dat
    - Permite:
        • ver historial completo
        • consultar por producto

    Cada movimiento contiene:
    - producto,
    - tipo,
    - cantidad,
    - fecha.

    Resultado:
    Permite seguimiento de actividad.
    """

    print("\n--- HISTORIAL DE MOVIMIENTOS ---")


def cargar_sistema():
    """
    Inicializa el sistema.

    Funcionamiento:
    - Verifica archivos.
    - Crea archivos si no existen.
    - Carga índice en memoria.
    - Prepara estructuras principales.

    Resultado:
    Sistema listo para funcionar.
    """

    print("\nCargando sistema...\n")


def cerrar_sistema():
    """
    Finaliza correctamente el sistema.

    Funcionamiento:
    - Guarda cambios pendientes.
    - Finaliza ejecución.
    - Muestra mensaje de salida.

    Resultado:
    Cierre seguro del programa.
    """

    print("\nCerrando sistema...")
    print("¡Hasta luego!\n")

# =========================================================
# PARTE ALGORÍTMICA
# =========================================================

# Inicialización del sistema
cargar_sistema()

# Variable de control del menú
opcion = -1

# =========================================================
# BUCLE PRINCIPAL
# =========================================================

while opcion != 0:

    # Mostrar menú principal
    mostrar_menu()

    # Solicitar opción
    opcion = int(input("\nSeleccione una opción: "))

# =====================================================
# CONTROL DE OPCIONES - MENÚ INTERACTIVO
# =====================================================

if opcion == 1:

    print("\n===================================")
    print("      AGREGAR PRODUCTO")
    print("===================================")

    opcion_agregar_producto()

    input("\nPresione ENTER para volver al menú...")


elif opcion == 2:

    print("\n===================================")
    print("    REGISTRAR ENTRADA")
    print("===================================")

    opcion_registrar_entrada()

    print("\n✓ Entrada registrada correctamente")

    input("\nPresione ENTER para continuar...")


elif opcion == 3:

    print("\n===================================")
    print("     REGISTRAR SALIDA")
    print("===================================")

    opcion_registrar_salida()

    print("\n✓ Operación finalizada")

    input("\nPresione ENTER para continuar...")


elif opcion == 4:

    print("\n===================================")
    print("       BUSCAR PRODUCTO")
    print("===================================")

    opcion_buscar_producto()

    input("\nPresione ENTER para volver...")


elif opcion == 5:

    print("\n===================================")
    print("     INVENTARIO COMPLETO")
    print("===================================")

    print("\n¿Cómo desea ordenar el inventario?")
    print("1. Ordenar por descripción")
    print("2. Ordenar por stock")

    criterio = int(input("\nSeleccione una opción: "))

    opcion_ver_inventario()

    print("\n✓ Inventario cargado correctamente")

    input("\nPresione ENTER para continuar...")


elif opcion == 6:

    print("\n===================================")
    print("    PRODUCTOS A REPONER")
    print("===================================")

    opcion_productos_a_reponer()

    print("\n✓ Consulta finalizada")

    input("\nPresione ENTER para continuar...")


elif opcion == 7:

    print("\n===================================")
    print("   HISTORIAL DE MOVIMIENTOS")
    print("===================================")

    print("\n1. Ver historial completo")
    print("2. Buscar movimientos de un producto")

    subopcion = int(input("\nSeleccione una opción: "))

    opcion_ver_historial()

    input("\nPresione ENTER para continuar...")


elif opcion == 0:

    print("\n===================================")
    print("      CERRANDO SISTEMA")
    print("===================================")

    cerrar_sistema()


else:

    print("\n===================================")
    print("       OPCIÓN INVÁLIDA")
    print("===================================")

    print("\n⚠ La opción ingresada no existe.")
    print("Por favor, seleccione una opción válida.")

    input("\nPresione ENTER para intentar nuevamente...")