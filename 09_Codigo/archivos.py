#Lectura y escritura de los archivos JSON del proyecto

import json
import os

#Las rutas se arman a partir de la carpeta de este archivo y no de la carpeta
#desde donde se ejecuta el programa, para que los JSON siempre se encuentren.
CARPETA_DATOS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "datos")


def ruta_de(nombre_archivo):
    return os.path.join(CARPETA_DATOS, nombre_archivo)


def cargar_lista(ruta):
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            contenido = archivo.read().strip()
    except FileNotFoundError:
        #La primera vez que se ejecuta el programa el archivo todavía no existe.
        return []

    if not contenido:
        return []

    try:
        datos = json.loads(contenido)
    except json.JSONDecodeError as detalle:
        raise ValueError(f"El archivo '{ruta}' está corrupto: {detalle}")

    if not isinstance(datos, list):
        raise ValueError(f"El archivo '{ruta}' debería contener una lista de registros.")

    return datos