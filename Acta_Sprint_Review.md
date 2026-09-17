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
> «Con la opción 6 veo los equipos que están prestados ahora mismo, con el estudiante y la
> fecha.»
>
> «Si intento eliminar ese equipo con la opción 8, no me deja: primero hay que registrar la
> devolución.»
>
> «Opción 5, la devolución. Elijo el préstamo y lo cierro.»
>
> «Y ahora la comprobación: opción 2, el equipo volvió a estar Disponible. En la opción 6 ya no
> aparece, y en la opción 7, el historial, queda el préstamo como Devuelto con su fecha. Con
> eso el ciclo queda cerrado.»

**Cierre (Juan, como PO)**

> «Con lo que vimos, acepto HU01, HU02, HU04, HU05, HU06, HU07 y HU08. HU03 la acepto con una
> observación: falta pedir el programa académico. En total aceptamos los 29 puntos. El objetivo
> se cumplió: se puede prestar, consultar y devolver, y los datos quedan guardados. Gracias.»
