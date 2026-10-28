# Fase 8. Entregar y seguir

**Entrada:** validación `DONE` y commits revisados identificados. Continuar normalmente en la conversación de implementación.

## Preparar y publicar

1. Consultar el estado remoto, reglas, plantilla, checks y dependencias. Acordar bases, relaciones y orden de integración o despliegue entre repositorios.
2. Preparar un encargo con `$mattpocock-skills:pr` para redactar título y cuerpo: comportamiento, evidencia antes/después, reversibilidad y alcance del impacto. Incorporar Jira, dependencias, riesgos y QA aplicables según la plantilla del repositorio.
3. Presentar acciones exactas de push, creación/edición de PR y comunicación. Publicar solo con sus autorizaciones específicas; verificar después URL, base y SHA. Redactar una PR no autoriza publicarla.
4. Mantener Jira en solo lectura; preparar actualizaciones exactas para Francisco.

## Seguimiento

1. Consultar CI, revisiones, comentarios y conflictos al retomar el seguimiento; no presuponer vigilancia automática. Durante una espera externa, registrar `WAITING` con responsable y condición de reanudación.
2. Investigar los fallos y contrastar el feedback antes de proponer respuestas o correcciones. Las modificaciones vuelven a `implement` y `validate`; los cambios de alcance vuelven a su fase. Revalidar el contenido final.
3. Antes del merge, comprobar aprobaciones, CI, feedback, base y compatibilidad. No aprobar el propio PR ni ejecutar el merge sin autorización y proceso aplicable.
4. Verificar integración de todos los repositorios de la unidad y registrar PR, SHA y validación posterior necesaria.
5. Marcar el ticket `DONE` solo cuando sus criterios y condiciones de integración acordadas estén satisfechos. Actualizar estado y fin en la tabla `## Tickets`. Consultar las dependencias en los archivos de tickets para identificar la siguiente unidad disponible. Verificar cualquier artefacto que se modifique con autorización.
6. Si quedan tickets, volver a `implement` con uno disponible y una sesión nueva. Preservar el historial de las fases repetidas y el ticket al que correspondían. Si todos están integrados, comprobar el resultado conjunto y sus dependencias de despliegue.

## Actualización de TASK.md

- Estado, fechas y unidad de `deliver`; encargo y sesión.
- Enlaces a PR por repositorio, bases y versiones, comprobaciones e integración verificada. No copiar comentarios ni logs disponibles en GitHub.
- Esperas con responsable y condición de reanudación; preguntas nuevas y retirada de las resueltas.
- Ticket `DONE` y fecha de fin solo cuando cumple criterios e integración acordada. Sin tickets, conservar el seguimiento por fase.
- Distinguir preparado, publicado, aprobado, integrado y desplegado. Un despliegue pendiente se registra para contrastarlo con los requisitos del cierre.

**DONE:** cambio integrado conforme a lo acordado, comprobaciones requeridas y feedback material resueltos, con evidencia y seguimientos registrados; para la última unidad, resultado conjunto contrastado. Publicar una PR no completa la fase.

**Siguiente:** `implement` para otro ticket disponible, o `close` si no queda trabajo de implementación.
