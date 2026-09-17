# Acta de Sprint Retrospective

**Fecha:** jueves 17 de septiembre de 2026, justo después de la Sprint Review
**Asistentes:** Juan Polanco, Marlon Sanabria, Michael Martinez
**Facilita:** Marlon Sanabria (Scrum Master)
**Sprint:** Sprint 1 — 14 al 17 de septiembre de 2026

## De qué se trató esta reunión

Ya en la Review hablamos del producto: si funciona, si cumple los criterios. Aquí cambiamos el
enfoque a nosotros como equipo. La pregunta no fue "¿funciona el programa?" sino "¿cómo nos fue
organizándonos para construirlo, y qué haríamos distinto la próxima vez?"

## Lo que nos salió bien

Lo primero que salió a relucir fue algo que ninguno esperaba que importara tanto: haber escrito
los criterios de aceptación desde el Planning. Cuando alguien decía "ya terminé", no había que
discutir de palabra si de verdad cumplía o no — se abría la consola y se comprobaba. Eso solo ya
nos ahorró varias discusiones que en otro proyecto se habrían alargado.

También coincidimos en que dividir el código en módulos con una sola responsabilidad cada uno
(`archivos.py`, `equipos.py`, `estudiantes.py`, `prestamos.py`) fue lo que de verdad nos permitió
programar los tres al mismo tiempo sin pisarnos. Y hay algo de lo que estamos contentos en
particular: al principio pensábamos que HU06 y HU07 se iban a quedar por fuera del Sprint, porque
dependían de que HU04 ya estuviera lista. Al final se alcanzaron a terminar y pasaron sus
criterios de aceptación, así que el Sprint se cerró completo.

## Lo que no salió tan bien, y por qué

Lo primero que reconocimos fue el desorden inicial en Git. Cada uno empezó subiendo sus archivos
a un sitio distinto — unos quedaron en la raíz del repositorio y otros dentro de una carpeta — y
como los módulos de Python se importan entre ellos, bastaba con que uno quedara mal ubicado para
que el programa completo no arrancara. Al hablarlo, vimos que la causa de fondo fue no dejar la
estructura de carpetas resuelta *antes* de que cada uno empezara a programar por su cuenta.

Después hablamos de la dependencia entre historias. El préstamo necesitaba que equipos y
estudiantes ya existieran, y las consultas de Marlon necesitaban que el préstamo ya funcionara.
Cuando alguien se atrasaba un poco, el siguiente quedaba bloqueado esperando. En el Planning
sabíamos que HU04 era importante, pero no lo teníamos tan claro como el riesgo central del Sprint
que en realidad terminó siendo.

También salió el tema de los errores pequeños con efectos grandes: una sola letra mal escrita en
el nombre de una variable dejó sin funcionar la lectura de archivos, y con eso se cayó todo el
programa. Ahí la causa fue clara — no estábamos probando cada módulo apenas se terminaba, sino
esperando a juntarlo todo al final del día, así que el error se quedó escondido más tiempo del
que debía.

Y el último punto no lo vimos nosotros solos, sino que salió de una ronda de pruebas adicional ya
con el programa "terminado": el sistema se caía con un error sin controlar si la entrada de datos
se cortaba a mitad de una pregunta, y la confirmación para eliminar un equipo solo aceptaba la
letra `s` exacta, sin aceptar algo tan natural como `si` o `sí`. Nuestro plan de pruebas cubría
bien los ocho criterios de aceptación, pero no habíamos pensado en cómo se comporta el programa
cuando alguien lo usa de forma un poco descuidada, que es como lo usa la gente de verdad.

## Qué vamos a cambiar

De esa conversación salieron cuatro cosas concretas que queremos hacer distinto:

Vamos a dejar la estructura de carpetas resuelta y el primer commit hecho **antes** de repartir
las tareas de código, no en paralelo con el resto. También vamos a identificar desde el Planning
cuál historia es la "bisagra" del Sprint — como HU04 esta vez — y programarla a mitad de semana
en vez de dejarla para cuando ya no hay margen. Cada módulo se va a probar apenas se termine, no
al final del día cuando ya está todo junto. Y al plan de pruebas le vamos a agregar, además de
los criterios de aceptación de cada historia, casos que simulen a alguien usando el programa de
forma descuidada: entradas que se cortan a la mitad, respuestas escritas de forma natural en vez
de con la letra exacta que el código espera.

## Las tres acciones que nos comprometemos a hacer

1. **Crear la estructura de carpetas y hacer el primer commit el mismo día del Sprint Planning**,
   antes de repartir las tareas de código. Marlon verifica que los tres puedan clonar el
   repositorio y correr el programa sin errores antes de que termine ese día.
2. **Marcar explícitamente en el Sprint Backlog cuál tarea es la bisagra del Sprint** — la que
   bloquea a más historias si se atrasa — y programarla con al menos dos días de margen antes del
   cierre, nunca el último día.
3. **Agregar una sección de "casos de uso descuidado" al plan de pruebas**, con al menos tres
   casos por Sprint que prueben cómo responde el programa a algo que el usuario hizo mal a
   propósito o sin querer.

## Para cerrar

El Sprint Goal se cumplió completo: se puede registrar, prestar, consultar, ver lo prestado,
revisar el historial, devolver y eliminar equipos, con todo guardado en JSON. Si algo nos queda
claro de esta semana es que lo más valioso no fue el código en sí, sino aprender que escribir los
criterios de aceptación por adelantado evita discusiones después, y que un programa que ya parece
"terminado" todavía puede tener huecos que solo aparecen cuando alguien lo prueba pensando como
un usuario real y no como quien lo escribió.
