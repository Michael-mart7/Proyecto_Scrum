"""
prestamos.py
Registro de prestamos y devoluciones (HU04 y HU05)
Responsable: Juan Polanco
"""

from datetime import date

from archivos import cargar_lista, guardar_lista, generar_id, ruta_de

RUTA_PRESTAMOS = ruta_de("prestamos.json")
RUTA_EQUIPOS = ruta_de("equipos.json")

ESTADO_ACTIVO = "Activo"
ESTADO_DEVUELTO = "Devuelto"

# Estados del equipo. Deben coincidir con los que usa equipos.py.
EQUIPO_DISPONIBLE = "Disponible"
EQUIPO_PRESTADO = "Prestado"


def cargar_prestamos():
    return cargar_lista(RUTA_PRESTAMOS)


def guardar_prestamos(prestamos):
    guardar_lista(RUTA_PRESTAMOS, prestamos)


def buscar_por_id(prestamos, id_prestamo):
    """Devuelve el prestamo con ese id, o None si no existe."""
    for prestamo in prestamos:
        if prestamo["id"] == id_prestamo:
            return prestamo
    return None


def buscar_equipo(equipos, codigo):
    """Busca un equipo por su codigo dentro de la lista que recibe."""
    for equipo in equipos:
        if equipo["codigo"] == codigo:
            return equipo
    return None


def registrar_prestamo(prestamos, equipos, equipo, estudiante):
    """
    Registra el prestamo de un equipo a un estudiante.
    El equipo y el estudiante ya vienen elegidos desde el menu.
    Devuelve (ok, mensaje, prestamo).
    """
    if equipo is None or estudiante is None:
        return False, "Hay que elegir un equipo y un estudiante.", None

    if equipo["estado"] != EQUIPO_DISPONIBLE:
        return False, f"El equipo {equipo['codigo']} no esta disponible.", None

    prestamo = {
        "id": generar_id(prestamos),
        "codigo_equipo": equipo["codigo"],
        "documento_estudiante": estudiante["documento"],
        "nombre_estudiante": estudiante["nombre"],
        "fecha_prestamo": date.today().isoformat(),
        "fecha_devolucion": None,
        "estado": ESTADO_ACTIVO,
    }

    prestamos.append(prestamo)
    equipo["estado"] = EQUIPO_PRESTADO

    # Se guardan los dos archivos juntos para que no quede un prestamo
    # registrado sin que el equipo diga que esta prestado.
    guardar_prestamos(prestamos)
    guardar_lista(RUTA_EQUIPOS, equipos)

    mensaje = f"Prestamo #{prestamo['id']} registrado a nombre de {estudiante['nombre']}."
    return True, mensaje, prestamo


def registrar_devolucion(prestamos, equipos, id_prestamo):
    """
    Cierra un prestamo y deja el equipo otra vez disponible.
    Devuelve (ok, mensaje).
    """
    prestamo = buscar_por_id(prestamos, id_prestamo)

    if prestamo is None:
        return False, f"No existe el prestamo numero {id_prestamo}."

    if prestamo["estado"] == ESTADO_DEVUELTO:
        return False, f"El prestamo #{id_prestamo} ya fue devuelto."

    prestamo["estado"] = ESTADO_DEVUELTO
    prestamo["fecha_devolucion"] = date.today().isoformat()

    equipo = buscar_equipo(equipos, prestamo["codigo_equipo"])
    if equipo is not None:
        equipo["estado"] = EQUIPO_DISPONIBLE

    guardar_prestamos(prestamos)
    guardar_lista(RUTA_EQUIPOS, equipos)

    return True, f"El equipo {prestamo['codigo_equipo']} vuelve a estar disponible."


# HU06 (prestamos activos) y HU07 (historial) las hace Marlon, van aqui debajo.
