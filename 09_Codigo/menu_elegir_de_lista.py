"""
Fragmento para main.py
Funcion elegir_de_lista (T10) - tarea M5 de Marlon
Pegar dentro de main.py, junto a las demas funciones del menu.
"""


def elegir_de_lista(lista, texto_item):
    """
    Muestra una lista numerada y devuelve el elemento elegido.
    Devuelve None si el usuario cancela con la opcion 0.

    texto_item: texto para el mensaje cuando la lista esta vacia,
    por ejemplo "equipos", "estudiantes" o "prestamos".
    """
    if not lista:
        print(f"No hay {texto_item} registrados.")
        return None

    for indice, item in enumerate(lista, start=1):
        print(f"{indice}. {item}")
    print("0. Cancelar")

    while True:
        opcion = input("Elige una opcion: ").strip()

        if not opcion.isdigit():
            print("Opcion invalida, intenta de nuevo.")
            continue

        opcion = int(opcion)

        if opcion == 0:
            return None

        if 1 <= opcion <= len(lista):
            return lista[opcion - 1]

        print("Opcion invalida, intenta de nuevo.")
