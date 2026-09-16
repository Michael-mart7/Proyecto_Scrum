#Gestión del inventario de equipos tecnológicos (HU01, HU02, HU08)

import archivos

RUTA_ARCHIVO = archivos.ruta_de("equipos.json")

ESTADO_DISPONIBLE = "Disponible"
ESTADO_PRESTADO = "Prestado"

#Tipos sugeridos al registrar. El usuario puede escribir otro.
TIPOS_SUGERIDOS = ["Portátil", "Tablet", "Videobeam", "Cámara", "Otro"]


def cargar_equipos():
    return archivos.cargar_lista(RUTA_ARCHIVO)


def guardar_equipos(equipos):
    archivos.guardar_lista(RUTA_ARCHIVO, equipos)

def buscar_por_codigo(equipos, codigo):
    #Los códigos se comparan sin distinguir mayúsculas para que "eq-001" y
    #"EQ-001" no se registren como dos equipos distintos.
    for equipo in equipos:
        if equipo["codigo"].upper() == codigo.strip().upper():
            return equipo
    return None


def listar_por_estado(equipos, estado):
    return [equipo for equipo in equipos if equipo["estado"] == estado]


def esta_disponible(equipo):
    return equipo["estado"] == ESTADO_DISPONIBLE


def cambiar_estado(equipo, estado):
    equipo["estado"] = estado

def validar_datos_equipo(equipos, codigo, tipo, marca, modelo):
    if not codigo.strip():
        return False, "El código del equipo no puede quedar vacío."
    if not tipo.strip():
        return False, "El tipo del equipo no puede quedar vacío."
    if not marca.strip():
        return False, "La marca del equipo no puede quedar vacía."
    if not modelo.strip():
        return False, "El modelo del equipo no puede quedar vacío."

    if buscar_por_codigo(equipos, codigo) is not None:
        return False, f"Ya existe un equipo registrado con el código '{codigo.strip().upper()}'."

    return True, ""


def registrar_equipo(equipos, codigo, tipo, marca, modelo):
    ok, mensaje = validar_datos_equipo(equipos, codigo, tipo, marca, modelo)
    if not ok:
        return False, mensaje, None

    equipo = {
        "codigo": codigo.strip().upper(),
        "tipo": tipo.strip(),
        "marca": marca.strip(),
        "modelo": modelo.strip(),
        "estado": ESTADO_DISPONIBLE
    }
    equipos.append(equipo)

    guardar_equipos(equipos)
    return True, f"Equipo '{equipo['codigo']}' registrado correctamente.", equipo


def eliminar_equipo(equipos, codigo):
    #No se valida aquí si el equipo está prestado según la lista de préstamos:
    #basta con su propio estado, que prestamos.py mantiene actualizado.
    equipo = buscar_por_codigo(equipos, codigo)
    if equipo is None:
        return False, f"No existe ningún equipo con el código '{codigo.strip().upper()}'."

    if not esta_disponible(equipo):
        return False, (
            f"No se puede eliminar el equipo '{equipo['codigo']}' porque está prestado. "
            "Registre primero la devolución."
        )

    equipos.remove(equipo)
    guardar_equipos(equipos)
    return True, f"Equipo '{equipo['codigo']}' eliminado del inventario."