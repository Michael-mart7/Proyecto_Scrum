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
