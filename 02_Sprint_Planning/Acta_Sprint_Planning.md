# Acta de Sprint Planning

**Fecha:** lunes 14 de septiembre de 2026
**Asistentes:** Juan Polanco, Marlon Sanabria, Michael Martinez
**Duracion:** 1 hora (maximo)

## Sprint Goal

> Entregar un MVP por consola que permita registrar equipos y estudiantes, prestar y devolver
> equipos, y que toda la informacion quede guardada en archivos JSON.

## Historias seleccionadas

| Historia | Descripcion breve | Story Points | Compromiso |
|----------|--------------------|---------------|------------|
| HU01 | Registrar equipos | 3 | Firme |
| HU02 | Listar equipos | 2 | Firme |
| HU03 | Registrar estudiantes | 3 | Firme |
| HU04 | Registrar prestamo | 5 | Firme |
| HU05 | Registrar devolucion | 3 | Firme |
| HU06 | Prestamos activos | 5 | Si alcanza el tiempo |
| HU07 | Historial de prestamos | 5 | Si alcanza el tiempo |
| HU08 | Eliminar equipos | 3 | Si alcanza el tiempo |

**Total compromiso firme (HU01-HU05):** 16 puntos
**Total adicional (HU06-HU08):** 13 puntos

## Criterios de aceptacion

Antes de estimar, Juan leyo los criterios de aceptacion de cada historia y los revisamos entre
los tres para que todos entendieramos lo mismo por "terminado". Estan escritos debajo de cada
historia en el [Product Backlog](../01_Product_Backlog/Product_Backlog.md), y son los que se
usan en la Sprint Review para aceptar o no cada historia.

## Estimaciones y justificaciones

Estimamos en Story Points y no en horas: cada numero tiene en cuenta cuanto trabajo lleva la
historia, que tan compleja es y que tanto depende de otras.

| Historia | Puntos | Por que |
|----------|--------|---------|
| HU01 | 3 | Hay que pedir cuatro datos, validar que no queden vacios y que el codigo no se repita, y guardar en JSON |
| HU02 | 2 | Es la mas sencilla: recorrer la lista, mostrarla y contar los disponibles |
| HU03 | 3 | Parecida a HU01, pero con mas validaciones: documento solo numeros y formato del correo |
| HU04 | 5 | La mas grande del compromiso firme. Toca tres modulos a la vez y tiene que guardar el prestamo y el cambio de estado del equipo juntos |
| HU05 | 3 | Reutiliza casi todo lo de HU04, solo cambia el estado de vuelta y guarda la fecha |
| HU06 | 5 | Tiene poco codigo, pero no se puede empezar hasta que HU04 este lista |
| HU07 | 5 | Igual que HU06: depende de que ya existan prestamos guardados |
| HU08 | 3 | Borrar es facil, pero hay que confirmar antes y no dejar eliminar un equipo prestado |

**Donde hubo discusion:** en HU06 y HU07. Al principio parecian de 2 o 3 puntos porque solo
filtran y muestran una lista. Al final quedaron en 5 porque dependen de HU04: si el prestamo se
atrasa, estas dos quedan bloqueadas, y esa incertidumbre tambien cuenta en la estimacion. Por lo
mismo quedaron como alcance adicional y no como compromiso firme.

## Sprint Backlog (tareas tecnicas)

| Tarea | Descripcion | Responsable | Dia |
|-------|-------------|-------------|-----|
| T01 | Estructura de carpetas y README | Marlon | Lunes 14 |
| T02 | archivos.py | Michael | Lunes 14 |
| T03 | equipos.py (registrar) | Michael | Lunes 14 |
| T04 | main.py (menu) | Juan | Lunes 14 |
| T05 | equipos.py (listar) | Michael | Martes 15 |
| T06 | estudiantes.py | Marlon | Martes 15 |
| T07-T08 | prestamos.py (registrar) | Juan | Miercoles 16 |
| T09 | prestamos.py (devolucion) | Juan | Jueves 17 |
| T10 | elegir_de_lista | Marlon | Miercoles 16 |
| T11 | prestamos activos | Marlon | Jueves 17 |
| T12 | historial de prestamos | Marlon | Viernes 18 |
| T13 | eliminar equipos | Michael | Jueves 17 |
| T14 | datos de ejemplo | Michael | Viernes 18 |

## Acuerdos del Sprint

- **Hora de la Daily:** 8:00 a.m., todos los dias.
- **Movimiento del tablero:** cada uno mueve su propia tarjeta (To Do -> In Progress -> Review/Test).
  Solo Juan mueve a Done, despues de validar.
- **Definicion de Terminado:** el codigo funciona, esta commiteado y pusheado, paso la validacion
  del PO y la tarjeta esta en Done.

## Riesgos identificados

- HU04 bloquea a HU05, HU06 y HU07: si se atrasa, todo el flujo de prestamos se atrasa.
- Cada uno programa su parte por separado y los modulos se importan entre ellos. Si no nos ponemos
  de acuerdo en donde va cada archivo, el programa no va a arrancar al juntarlo todo.
- Algunas tareas dependen de funciones que hace otra persona (por ejemplo, prestamos.py necesita
  archivos.py). Si alguien cambia el nombre o los parametros de una funcion, se rompe lo del otro.
- Es un Sprint de una semana y los tres tenemos otras clases. Si alguien se enferma o se atrasa
  un dia, no hay mucho margen para recuperarlo.
- Si solo probamos al final, un error pequeno en un modulo puede tumbar todo el programa y no
  sabriamos de donde viene.
