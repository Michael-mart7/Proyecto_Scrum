"""
main.py
Menu principal del Sistema de Prestamo de Equipos Tecnologicos
Responsable: Juan Polanco

Este archivo solo arma el menu y muestra resultados. La logica esta en los
modulos de cada uno: equipos.py, estudiantes.py y prestamos.py.
"""

from archivos import cargar_lista
from menu_elegir_de_lista import elegir_de_lista

import equipos as mod_equipos
import estudiantes as mod_estudiantes
import prestamos as mod_prestamos

SEPARADOR = "-" * 50


# ---------- Ayudas para pedir y mostrar datos ----------

def pedir_texto(mensaje):
    """Pide un dato y no sigue hasta que el usuario escriba algo."""
    while True:
        valor = input(mensaje).strip()
        if valor:
            return valor
        print("Este dato no puede quedar vacio.")


def texto_equipo(equipo):
    return f"{equipo['codigo']} - {equipo['tipo']} {equipo['marca']} {equipo['modelo']} ({equipo['estado']})"


def texto_estudiante(estudiante):
    return f"{estudiante['documento']} - {estudiante['nombre']}"


def texto_prestamo(prestamo):
    return f"#{prestamo['id']} - {prestamo['codigo_equipo']} - {prestamo['nombre_estudiante']} - {prestamo['fecha_prestamo']}"


def elegir(lista, describir, texto_item):
    """
    Usa elegir_de_lista (la funcion de Marlon), que imprime cada elemento tal
    cual. Por eso le pasamos textos ya armados y despues recuperamos el
    elemento original por su posicion.
    """
    if not lista:
        print(f"No hay {texto_item} para mostrar.")
        return None

    textos = [describir(elemento) for elemento in lista]
    elegido = elegir_de_lista(textos, texto_item)

    if elegido is None:
        return None
    return lista[textos.index(elegido)]


# ---------- Opciones del menu ----------

def registrar_equipo(datos):
    """HU01"""
    print("\n--- Registrar equipo ---")
    print("Tipos sugeridos:", ", ".join(mod_equipos.TIPOS_SUGERIDOS))

    codigo = pedir_texto("Codigo: ")
    tipo = pedir_texto("Tipo: ")
    marca = pedir_texto("Marca: ")
    modelo = pedir_texto("Modelo: ")

    ok, mensaje, equipo = mod_equipos.registrar_equipo(datos["equipos"], codigo, tipo, marca, modelo)
    print(mensaje)


def listar_equipos(datos):
    """HU02"""
    print("\n--- Equipos registrados ---")
    equipos = datos["equipos"]

    if not equipos:
        print("Todavia no hay equipos registrados.")
        return

    for equipo in equipos:
        print(texto_equipo(equipo))

    disponibles = mod_equipos.listar_por_estado(equipos, mod_equipos.ESTADO_DISPONIBLE)
    print(SEPARADOR)
    print(f"Disponibles: {len(disponibles)} de {len(equipos)}")


def registrar_estudiante(datos):
    """HU03"""
    print("\n--- Registrar estudiante ---")

    nombre = pedir_texto("Nombre completo: ")
    documento = pedir_texto("Documento: ")
    correo = pedir_texto("Correo: ")

    ok, mensaje, estudiante = mod_estudiantes.registrar_estudiante(
        datos["estudiantes"], nombre, documento, correo
    )
    print(mensaje)


def registrar_prestamo(datos):
    """HU04"""
    print("\n--- Registrar prestamo ---")

    disponibles = mod_equipos.listar_por_estado(datos["equipos"], mod_equipos.ESTADO_DISPONIBLE)
    if not disponibles:
        print("No hay equipos disponibles para prestar.")
        return

    equipo = elegir(disponibles, texto_equipo, "equipos disponibles")
    if equipo is None:
        return

    estudiante = elegir(datos["estudiantes"], texto_estudiante, "estudiantes")
    if estudiante is None:
        return

    ok, mensaje, prestamo = mod_prestamos.registrar_prestamo(
        datos["prestamos"], datos["equipos"], equipo, estudiante
    )
    print(mensaje)


def registrar_devolucion(datos):
    """HU05"""
    print("\n--- Registrar devolucion ---")

    activos = [p for p in datos["prestamos"] if p["estado"] == mod_prestamos.ESTADO_ACTIVO]
    if not activos:
        print("No hay prestamos activos.")
        return

    prestamo = elegir(activos, texto_prestamo, "prestamos activos")
    if prestamo is None:
        return

    ok, mensaje = mod_prestamos.registrar_devolucion(
        datos["prestamos"], datos["equipos"], prestamo["id"]
    )
    print(mensaje)


def consultar_prestados(datos):
    """HU06 - la funcion prestamos_activos(prestamos) la agrega Marlon en prestamos.py"""
    print("\n--- Equipos prestados ---")
    try:
        activos = mod_prestamos.prestamos_activos(datos["prestamos"])
    except AttributeError:
        print("Esta opcion todavia no esta lista.")
        return

    if not activos:
        print("No hay equipos prestados.")
        return

    for prestamo in activos:
        print(texto_prestamo(prestamo))


def historial_prestamos(datos):
    """HU07 - la funcion historial(prestamos) la agrega Marlon en prestamos.py"""
    print("\n--- Historial de prestamos ---")
    try:
        todos = mod_prestamos.historial(datos["prestamos"])
    except AttributeError:
        print("Esta opcion todavia no esta lista.")
        return

    if not todos:
        print("Todavia no hay prestamos.")
        return

    for prestamo in todos:
        fecha_devolucion = prestamo["fecha_devolucion"] or "pendiente"
        print(f"{texto_prestamo(prestamo)} - {prestamo['estado']} - devolucion: {fecha_devolucion}")


def eliminar_equipo(datos):
    """HU08"""
    print("\n--- Eliminar equipo ---")

    equipo = elegir(datos["equipos"], texto_equipo, "equipos")
    if equipo is None:
        return

    confirmacion = pedir_texto(f"Seguro que quieres eliminar {equipo['codigo']}? (s/n): ")
    if confirmacion.lower() not in ("s", "si", "sí"):
        print("Eliminacion cancelada.")
        return

    ok, mensaje = mod_equipos.eliminar_equipo(datos["equipos"], equipo["codigo"])
    print(mensaje)


OPCIONES = [
    ("Registrar equipo", registrar_equipo),
    ("Listar equipos", listar_equipos),
    ("Registrar estudiante", registrar_estudiante),
    ("Registrar prestamo", registrar_prestamo),
    ("Registrar devolucion", registrar_devolucion),
    ("Consultar equipos prestados", consultar_prestados),
    ("Historial de prestamos", historial_prestamos),
    ("Eliminar equipo", eliminar_equipo),
]


# ---------- Programa principal ----------

def mostrar_menu():
    print("\n=== Menu principal ===")
    for numero, (etiqueta, _) in enumerate(OPCIONES, start=1):
        print(f"{numero}. {etiqueta}")
    print("0. Salir")


def main():
    try:
        datos = {
            "equipos": mod_equipos.cargar_equipos(),
            "estudiantes": cargar_lista(mod_estudiantes.RUTA_ESTUDIANTES),
            "prestamos": mod_prestamos.cargar_prestamos(),
        }
    except ValueError as detalle:
        print(detalle)
        print("Revisa los archivos JSON antes de volver a ejecutar el programa.")
        return

    print("=== Sistema de Prestamo de Equipos Tecnologicos ===")

    while True:
        mostrar_menu()
        opcion = input("Elige una opcion: ").strip()

        if opcion == "0":
            break

        if not opcion.isdigit() or not 1 <= int(opcion) <= len(OPCIONES):
            print("Opcion invalida, intenta de nuevo.")
            continue

        funcion = OPCIONES[int(opcion) - 1][1]

        try:
            funcion(datos)
        except ValueError as detalle:
            # Si falla al guardar, se avisa pero el programa sigue abierto.
            print(detalle)

    print("Listo, hasta luego.")


if __name__ == "__main__":
    try:
        main()
    except EOFError:
        # Si la entrada estandar se corta a mitad de un input() (por ejemplo,
        # al redirigir datos desde un archivo o un pipe que se queda corto),
        # no debe verse un traceback: se avisa y se termina limpio.
        print("\nEntrada finalizada inesperadamente. Programa terminado.")
    except KeyboardInterrupt:
        # Ctrl+C tampoco debe mostrar un traceback.
        print("\nPrograma interrumpido por el usuario.")
