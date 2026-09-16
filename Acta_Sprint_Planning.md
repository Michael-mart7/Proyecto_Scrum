# Acta de Sprint Planning

**Fecha:** lunes 14 de septiembre de 2026
**Asistentes:** Juan Polanco, Marlon Sanabria, Michael Martinez
**Duracion:** 1 hora (maximo)

## Sprint Goal

> [Escribir aqui la frase acordada entre los tres. Ejemplo: "Entregar un MVP por consola
> que permita registrar equipos y estudiantes, y gestionar prestamos y devoluciones con
> datos en JSON."]

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

## Estimaciones y justificaciones

> [Anotar aqui si alguien no estuvo de acuerdo con los puntos sugeridos y por que.
> Ejemplo: "HU06 tiene poco codigo, pero depende de HU04, asi que la incertidumbre es alta."]

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
- [Agregar otros riesgos que surjan en la reunion.]
