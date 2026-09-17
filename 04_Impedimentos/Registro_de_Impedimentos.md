# Registro de impedimentos

**Sprint:** Sprint 1 — 14 al 18 de septiembre de 2026
**Lleva el registro:** Marlon Sanabria (Scrum Master)

Aquí anotamos todo lo que nos frenó durante el Sprint. Algunos salieron en la Daily y otros en
medio del día, cuando alguien se quedaba bloqueado. En cada caso quedó quién se encargaba de
resolverlo y qué hicimos.

| # | Fecha | Impedimento | Responsable | Acción tomada | Estado |
|---|---|---|---|---|---|
| 1 | Lunes 14 | Juan no sabía dónde ubicar `main.py` porque todavía no existía la estructura de carpetas, y si cada uno ponía sus archivos donde quisiera íbamos a chocar | Marlon | Se acordó que nadie subía código hasta que Marlon dejara lista la estructura (T01) | Resuelto |
| 2 | Martes 15 | Unos archivos quedaron en la raíz del repositorio y otros dentro de `09_Codigo`. Como los módulos se importan entre ellos, el programa no arrancaba | Michael | Se acordó que todo el código va en `09_Codigo` y se movieron los archivos que estaban afuera | Resuelto |
| 3 | Martes 15 | Una letra de más en el nombre de una variable de `archivos.py` impedía leer los JSON, y con eso se caía todo el programa | Michael | Se corrigió el nombre y se acordó probar cada módulo apenas se termina, sin esperar a juntarlo todo | Resuelto |
| 4 | Jueves 17 | Marlon no podía empezar las consultas de HU06 y HU07 porque dependían de que el registro de préstamos (HU04) estuviera listo | Juan | Juan terminó HU04 primero y avisó apenas quedó lista, para que Marlon pudiera arrancar con las consultas | Resuelto |
| 5 | Viernes 18 | Al reorganizar los datos de ejemplo, los estudiantes quedaron sin su `id`, y registrar un estudiante nuevo hacía caer el programa | Michael | Se les agregó el `id` a los estudiantes y se volvió a probar el registro | Resuelto |
| 6 | Viernes 18 | Varias capturas de las pruebas se subieron con el mismo nombre de archivo y unas reemplazaron a otras, así que algunos casos se quedaron sin su evidencia | Marlon y Michael | Se recuperaron las capturas desde el historial de Git, y desde entonces las nuevas se nombran por caso (por ejemplo `CP-23.png`) | Resuelto |

## Qué nos dejaron

Casi todos los impedimentos vinieron de lo mismo: trabajar por separado sin haber acordado antes
cómo íbamos a juntar las partes. Por eso en la Retrospectiva quedaron tres acciones que salen
directamente de este registro:

- Dejar la estructura de carpetas lista **antes** de repartir el código (impedimentos 1 y 2).
- Identificar desde el Planning la tarea de la que dependen las demás y hacerla primero
  (impedimento 4).
- Probar cada parte apenas se termina, y volver a probar cuando cambian los datos
  (impedimentos 3 y 5).
