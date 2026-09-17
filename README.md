# Sistema de Préstamo de Equipos Tecnológicos

Proyecto del curso **Scrum y Metodologías Ágiles** de Campuslands, con el trainer Duvan Sanabria.

Es un MVP por consola hecho en Python. Sirve para llevar el préstamo de equipos (portátiles,
tablets, videobeams…) a estudiantes: registrar equipos y estudiantes, prestar, devolver y saber
en qué estado está cada equipo. Los datos se guardan en archivos JSON, así que no se pierden al
cerrar el programa.

Lo hicimos en un Sprint de una semana, del 14 al 18 de septiembre de 2026.

## Equipo

| Integrante | Rol |
|---|---|
| Juan Polanco | Product Owner y Developer |
| Marlon Sanabria | Scrum Master y Developer |
| Michael Martinez | Developer |

## Cómo ejecutarlo

Solo se necesita Python 3. No hay que instalar nada más.

```bash
cd 09_Codigo
python main.py
```

El programa trae datos de ejemplo en `09_Codigo/datos/` para poder probarlo de una vez.

## Qué se puede hacer

```
1. Registrar equipo
2. Listar equipos
3. Registrar estudiante
4. Registrar prestamo
5. Registrar devolucion
6. Consultar equipos prestados
7. Historial de prestamos
8. Eliminar equipo
0. Salir
```

## Cómo está organizado

```
Proyecto_Scrum/
├── Product_Backlog.md        historias de usuario, prioridad y puntos
├── Acta_Sprint_Planning.md
├── Acta_Sprint_Review.md
├── Informe_Final.md          resumen del Sprint y enlaces a los videos
├── 07_Pruebas/
│   └── Plan_de_Pruebas.md
└── 09_Codigo/
    ├── main.py               menú principal
    ├── archivos.py           lectura y escritura de los JSON
    ├── equipos.py            inventario de equipos
    ├── estudiantes.py        registro de estudiantes
    ├── prestamos.py          préstamos y devoluciones
    ├── menu_elegir_de_lista.py
    └── datos/                equipos.json, estudiantes.json, prestamos.json
```

Los enlaces al tablero y a los videos de los eventos están al final del
[Informe Final](Informe_Final.md).
