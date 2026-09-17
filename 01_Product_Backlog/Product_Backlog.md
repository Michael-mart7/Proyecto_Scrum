# Product Backlog

**Producto:** Sistema de Préstamo de Equipos Tecnológicos
**Product Owner:** Juan Polanco
**Sprint 1:** 14 al 18 de septiembre de 2026

## De qué se trata

La institución presta equipos a los estudiantes, pero lo hace todo a mano. Cuando alguien
pregunta qué portátil está prestado, a quién y desde cuándo, no hay forma rápida de saberlo.

Lo que vamos a entregar no es el sistema completo. Es un MVP por consola que sirve para validar
el proceso básico: registrar los equipos y los estudiantes, prestar, devolver y poder consultar
en qué estado está cada cosa. Si eso funciona, después se puede pensar en algo más grande.

## Historias de usuario

Las ocho salen del enunciado. Los criterios de aceptación los escribimos nosotros, y son los que
uso para decidir si una historia está terminada o no.

---

### HU01 — Registrar equipos
**Prioridad:** Alta · **Puntos:** 3

> Como administrador, quiero registrar equipos tecnológicos para mantener actualizado el inventario.

Para darla por terminada:
- Pide código, tipo, marca y modelo.
- No deja guardar ningún campo vacío.
- Si el código ya existe, avisa y no crea un duplicado.
- El equipo queda como *Disponible*.
- Sigue ahí después de cerrar y volver a abrir el programa.

---

### HU02 — Consultar equipos
**Prioridad:** Alta · **Puntos:** 2

> Como administrador, quiero consultar los equipos registrados para conocer su disponibilidad.

Para darla por terminada:
- Muestra código, tipo, marca, modelo y estado de cada equipo.
- Al final dice cuántos hay disponibles sobre el total.
- Si no hay equipos, lo dice en vez de mostrar una lista vacía.
- El estado que muestra es el real: si algo está prestado, se ve.

---

### HU03 — Registrar estudiantes
**Prioridad:** Alta · **Puntos:** 3

> Como administrador, quiero registrar estudiantes para asociarlos a los préstamos.

Para darla por terminada:
- Pide nombre, documento y correo.
- El documento solo acepta números y no se puede repetir.
- El correo tiene que tener un arroba, algo antes, algo después y un punto en el dominio.
- No deja campos vacíos.
- El estudiante queda guardado y sigue ahí en la siguiente ejecución.

---

### HU04 — Registrar préstamo
**Prioridad:** Alta · **Puntos:** 5

> Como administrador, quiero registrar el préstamo de un equipo a un estudiante.

Para darla por terminada:
- Solo deja elegir equipos que estén disponibles.
- El estudiante se elige de los que ya están registrados.
- Si no hay equipos libres o no hay estudiantes, avisa y no continúa.
- Guarda número de préstamo, equipo, estudiante y fecha.
- El equipo pasa solo a *Prestado*.
- El préstamo y el equipo quedan guardados juntos, sin que uno diga una cosa y el otro otra.

Es la historia que más puntos tiene porque toca tres módulos a la vez.

---

### HU05 — Registrar devolución
**Prioridad:** Alta · **Puntos:** 3

> Como administrador, quiero registrar la devolución de un equipo para actualizar su disponibilidad.

Para darla por terminada:
- Solo muestra los préstamos que siguen activos.
- Si no hay ninguno, lo dice.
- El préstamo pasa a *Devuelto* y guarda la fecha.
- El equipo vuelve a *Disponible* y se puede volver a prestar.
- Un préstamo ya devuelto no se puede devolver otra vez.

---

### HU06 — Consultar equipos prestados
**Prioridad:** Media · **Puntos:** 5

> Como administrador, quiero consultar los equipos actualmente prestados.

Para darla por terminada:
- Muestra solo los préstamos activos.
- De cada uno se ve el equipo, el estudiante y la fecha.
- Si no hay ninguno, lo dice.
- Cuando algo se devuelve, deja de aparecer aquí.

---

### HU07 — Historial de préstamos
**Prioridad:** Media · **Puntos:** 5

> Como administrador, quiero consultar el historial de préstamos realizados.

Para darla por terminada:
- Muestra todos los préstamos, activos y devueltos.
- Se ve el estado de cada uno y la fecha de devolución si ya se devolvió.
- El historial no se pierde al cerrar el programa.
- Aparecen en el orden en que se hicieron.

---

### HU08 — Eliminar equipos
**Prioridad:** Baja · **Puntos:** 3

> Como administrador, quiero eliminar un equipo del inventario cuando ya no esté disponible.

Para darla por terminada:
- Pide confirmación antes de borrar.
- Si el equipo está prestado, no lo deja y dice que primero hay que registrar la devolución.
- Si está disponible, lo borra del inventario.
- Deja de aparecer en el listado.

---

## Resumen

| Historia | Prioridad | Puntos | Compromiso | Estado al cierre |
|---|---|---|---|---|
| HU01 Registrar equipos | Alta | 3 | Firme | Terminada |
| HU02 Consultar equipos | Alta | 2 | Firme | Terminada |
| HU03 Registrar estudiantes | Alta | 3 | Firme | Terminada con observación |
| HU04 Registrar préstamo | Alta | 5 | Firme | Terminada |
| HU05 Registrar devolución | Alta | 3 | Firme | Terminada |
| HU06 Equipos prestados | Media | 5 | Si alcanza el tiempo | Terminada |
| HU07 Historial | Media | 5 | Si alcanza el tiempo | Terminada |
| HU08 Eliminar equipos | Baja | 3 | Si alcanza el tiempo | Terminada |

**Total:** 29 puntos. 16 del compromiso firme y 13 del alcance adicional.

Los Story Points son una estimación de esfuerzo y de riesgo, no de horas. HU06 y HU07 tienen 5
puntos aunque su código sea corto porque dependen de que HU04 esté lista, y esa incertidumbre
también cuenta.

Las cinco primeras son el flujo mínimo que hay que poder demostrar: registrar un equipo,
registrar un estudiante, prestar, consultar y devolver.

La columna *Compromiso* dice cómo se planificó cada historia al empezar el Sprint, y *Estado al
cierre* cómo quedó después de la Sprint Review. Al final se terminaron las ocho, incluidas las
tres que eran alcance adicional.

## Pendiente para el siguiente Sprint

Esto es lo que quedó por hacer. Lo dejo aquí para que no se pierda y se priorice en la próxima
Sprint Planning.

### HU09 — Programa académico del estudiante
**Prioridad:** Alta · **Puntos:** 2

> Como administrador, quiero registrar el programa académico de cada estudiante para saber a qué
> programa pertenece quien se lleva un equipo.

Sale de la observación que dejé en HU03 durante la Review: el enunciado pide documento, nombre,
correo y programa académico, y hoy solo se piden los tres primeros.

Para darla por terminada:
- Al registrar un estudiante también se pide el programa académico.
- No deja el programa vacío.
- Queda guardado en `estudiantes.json` junto con los demás datos.
- Los estudiantes que ya estaban registrados siguen cargando sin error.

Le pongo prioridad alta porque es algo que el enunciado pide desde el principio, y pocos puntos
porque es agregar un campo a algo que ya funciona. El último criterio es el que tiene más riesgo:
hay que cuidar que los estudiantes que ya estaban guardados sin ese dato no hagan fallar el
sistema.
