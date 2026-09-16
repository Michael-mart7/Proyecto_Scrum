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