# Acta de Sprint Review

**Fecha:** viernes 18 de septiembre de 2026
**Asistentes:** Juan Polanco (Product Owner), Marlon Sanabria (Scrum Master), Michael Martinez (Developer)
**Sprint:** Sprint 1 — 14 al 18 de septiembre de 2026

## Para qué fue la reunión

Mostrar lo que quedó funcionando y decidir, historia por historia, si cumple los criterios de
aceptación que escribimos en el Product Backlog. Las que no cumplen no se marcan como
terminadas y se quedan en el Backlog.

## Qué demostramos

Corrimos el programa desde la consola (`python main.py` dentro de `09_Codigo`) e hicimos el
recorrido completo:

1. Registramos un equipo nuevo e intentamos registrar uno con un código repetido, para mostrar
   que el sistema lo rechaza.
2. Registramos un estudiante y probamos con un documento con letras y un correo mal escrito.
3. Prestamos un equipo a un estudiante.
4. Consultamos el inventario y se vio el equipo como *Prestado*, con el conteo de disponibles
   más bajo. En la consulta de equipos prestados apareció el préstamo.
5. Intentamos eliminar ese equipo y el sistema no lo dejó por estar prestado.
6. Registramos la devolución.
7. Volvimos a consultar: el equipo ya aparecía como *Disponible*, dejó de salir en los
   prestados y en el historial quedó como *Devuelto* con su fecha.

También abrimos los archivos JSON para mostrar que los datos quedan guardados en disco y no
solo en memoria.

## Decisión sobre cada historia

| Historia | Decisión | Comentario |
|---|---|---|
| HU01 Registrar equipos | Aceptada | Cumple los cinco criterios |
| HU02 Consultar equipos | Aceptada | Muestra el conteo de disponibles sobre el total |
| HU03 Registrar estudiantes | Aceptada con observación | Valida y guarda bien, pero falta el programa académico |
| HU04 Registrar préstamo | Aceptada | El equipo cambia solo a *Prestado* y los dos archivos quedan iguales |
| HU05 Registrar devolución | Aceptada | El equipo vuelve a *Disponible* |
| HU06 Equipos prestados | Aceptada | Muestra solo los activos y el devuelto deja de aparecer |
| HU07 Historial | Aceptada | Muestra activos y devueltos con su fecha, y se conserva al reabrir |
| HU08 Eliminar equipos | Aceptada | No deja borrar un equipo prestado |

**Puntos aceptados:** 29 de 29. Todo el compromiso firme y todo el alcance adicional.

## Observaciones del Product Owner

- **HU03 se acepta con una observación.** Las validaciones funcionan y el estudiante queda
  guardado aunque se cierre el programa. Lo que falta es el **programa académico**, que pide el
  enunciado: ahora solo se piden nombre, documento y correo. Queda anotado para el siguiente
  Sprint.
- **HU06 y HU07 fueron las últimas en quedar listas**, porque dependían de que el préstamo
  funcionara. Aun así se alcanzaron dentro del Sprint y cumplen sus criterios.
- El objetivo del Sprint se cumplió: se puede registrar, prestar, consultar y devolver, y todo
  queda guardado en JSON.
