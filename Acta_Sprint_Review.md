# Acta de Sprint Review

**Fecha:** viernes 18 de septiembre de 2026
**Asistentes:** Juan Polanco (Product Owner), Marlon Sanabria (Scrum Master), Michael Martinez (Developer)
**Sprint:** Sprint 1 — 14 al 18 de septiembre de 2026

## Para qué fue la reunión

Mostrar lo que quedó funcionando y decidir, historia por historia, si cumple los criterios de
aceptación que escribimos en el Product Backlog. Las que no cumplen no se marcan como
terminadas y se quedan en el Backlog.

## Qué demostramos

Corrimos el programa desde la consola e hicimos el recorrido completo:

1. Registramos un equipo nuevo e intentamos registrar uno con un código repetido, para mostrar
   que el sistema lo rechaza.
2. Registramos un estudiante y probamos con un documento con letras y un correo mal escrito.
3. Prestamos un equipo a un estudiante.
4. Consultamos el inventario y se vio el equipo como *Prestado*, con el conteo de disponibles
   más bajo.
5. Registramos la devolución.
6. Volvimos a consultar y el equipo ya aparecía otra vez como *Disponible*.

También abrimos los archivos JSON para mostrar que los datos quedan guardados en disco y no
solo en memoria.

## Decisión sobre cada historia

| Historia | Decisión | Comentario |
|---|---|---|
| HU01 Registrar equipos | Aceptada | Cumple los cinco criterios |
| HU02 Consultar equipos | Aceptada | Muestra el conteo de disponibles sobre el total |
| HU03 Registrar estudiantes | Aceptada con observación | Las validaciones funcionan, ver observaciones |
| HU04 Registrar préstamo | Aceptada | El equipo cambia solo a *Prestado* y los dos archivos quedan iguales |
| HU05 Registrar devolución | Aceptada | El equipo vuelve a *Disponible* |
| HU06 Equipos prestados | Por confirmar | Depende de que esté la consulta en `prestamos.py` |
| HU07 Historial | Por confirmar | Igual que HU06 |
| HU08 Eliminar equipos | Aceptada | No deja borrar un equipo prestado |

## Observaciones del Product Owner

- **HU03 tiene dos cosas por corregir.** El registro de estudiantes no alcanza a guardar en el
  archivo por un error en la ruta, así que el estudiante se pierde al cerrar el programa.
  Además, el enunciado pide también el **programa académico** y ahora mismo solo se piden
  nombre, documento y correo. Por eso la acepto con observación y no de una.
- **HU06 y HU07 eran alcance adicional**, no compromiso firme. Que queden pendientes no afecta
  el objetivo del Sprint, porque el flujo mínimo de prestar y devolver sí quedó funcionando.
- El objetivo del Sprint se cumplió: se puede registrar, prestar, consultar y devolver, y todo
  queda guardado en JSON.

## Guion del video

Duración: entre 5 y 10 minutos. Antes de grabar hay que dejar los datos de ejemplo cargados para
que la demostración empiece limpia.

**Presentación (Juan)**

> «Buenas. Somos Juan Polanco, Marlon Sanabria y Michael Martinez. Esta es la Sprint Review de
> nuestro proyecto, el Sistema de Préstamo de Equipos Tecnológicos, hecho en Python durante un
> Sprint de una semana. Yo soy el Product Owner, así que al final voy diciendo qué historias
> acepto y cuáles no.»

**Demostración**

> «Empiezo con la opción 2 para ver el inventario. Estos son los equipos que hay y todos están
> disponibles.»
>
> «Con la opción 1 registro uno nuevo. Le pongo código, tipo, marca y modelo, y queda registrado
> como Disponible.»
>
> «Ahora repito el mismo código a propósito… y el sistema no me deja, porque uno de los criterios
> de aceptación era justamente que no se repitieran.»
>
> «Con la opción 3 registro un estudiante. Si le pongo letras al documento, lo rechaza. Y si el
> correo está mal escrito, también.»
>
> «Opción 4, el préstamo. Fíjense que solo me deja elegir equipos disponibles. Elijo uno y
> elijo al estudiante.»
>
> «Miren el archivo `prestamos.json`: ahí está el préstamo. Y en `equipos.json` el equipo ya
> aparece como Prestado. Los dos se guardan a la vez para que nunca digan cosas distintas.»
>
> «Opción 2 otra vez: el equipo sale como Prestado y el conteo bajó.»
>
> «Opción 5, la devolución. Elijo el préstamo y lo cierro.»
>
> «Y ahora la comprobación: opción 2, el equipo volvió a estar Disponible. Con eso el ciclo
> queda cerrado.»

**Cierre (Juan, como PO)**

> «Con lo que vimos, acepto HU01, HU02, HU04, HU05 y HU08. HU03 la acepto con una observación:
> hay que arreglar el guardado y agregar el programa académico. HU06 y HU07 quedan pendientes,
> pero eran alcance adicional y no el compromiso del Sprint. El objetivo se cumplió: se puede
> prestar, consultar y devolver, y los datos quedan guardados. Gracias.»
