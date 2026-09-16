"""
estudiantes.py
Registro de estudiantes y validaciones (HU03)
Responsable: Marlon Sanabria
"""

from archivos import cargar_lista, guardar_lista, generar_id

RUTA_ESTUDIANTES = "estudiantes.json"


def buscar_por_documento(estudiantes, documento):
    """Devuelve el estudiante con ese documento, o None si no existe."""
    for estudiante in estudiantes:
        if estudiante["documento"] == documento:
            return estudiante
    return None


def correo_valido(correo):
    """
    Un correo es valido si tiene exactamente un @, con texto antes
    y despues, y al menos un punto en la parte del dominio.
    """
    if correo.count("@") != 1:
        return False

    usuario, dominio = correo.split("@")

    if not usuario or not dominio:
        return False

    if "." not in dominio:
        return False

    return True


def registrar_estudiante(estudiantes, nombre, documento, correo):
    """
    Registra un estudiante nuevo.
    Devuelve (ok, mensaje, estudiante).
    """
    if not nombre or not documento or not correo:
        return False, "Todos los campos son obligatorios.", None

    if not documento.isdigit():
        return False, "El documento debe contener solo numeros.", None

    if not correo_valido(correo):
        return False, "El correo no tiene un formato valido.", None

    if buscar_por_documento(estudiantes, documento):
        return False, f"Ya existe un estudiante con el documento {documento}.", None

    nuevo_estudiante = {
        "id": generar_id(estudiantes),
        "nombre": nombre,
        "documento": documento,
        "correo": correo,
    }

    estudiantes.append(nuevo_estudiante)
    guardar_lista(RUTA_ESTUDIANTES, estudiantes)

    return True, "Estudiante registrado con exito.", nuevo_estudiante


if __name__ == "__main__":
    # Prueba rapida manual, no forma parte de main.py
    lista = cargar_lista(RUTA_ESTUDIANTES)
    ok, mensaje, est = registrar_estudiante(lista, "Ana Perez", "1020304050", "ana@correo.com")
    print(mensaje)
