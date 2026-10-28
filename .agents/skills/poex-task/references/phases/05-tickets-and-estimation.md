# Fase 5. Dividir y estimar

**Entrada:** especificación `DONE`, o diseño `DONE` y elección de Francisco de pasar directamente a `plan`.

**Encargo:** `$mattpocock-skills:to-tickets` en la misma conversación de diseño y, si se realizó, especificación. El prompt indica esta continuidad y la ruta absoluta del tracker local. Enlaza la especificación verificada cuando exista; si se omitió, utiliza lo acordado en la conversación de diseño.

## Resultado y verificación

1. Proponer tickets que entreguen una porción de comportamiento completa a través de las capas necesarias y puedan comprobarse por separado. Cada ticket debe caber en un contexto nuevo.
2. Declarar criterios, repositorios implicados, contratos, pruebas y bloqueadores reales. El trabajo entre repositorios sigue siendo una unidad de comportamiento.
3. Validar con Francisco la cobertura de la especificación o del alcance acordado en diseño, la granularidad y el grafo. El prefactoring y expandir–migrar–contraer se justifican por el riesgo concreto; no son pasos obligatorios.
4. Acordar cómo se integrarán los tickets. Por defecto, cada ticket recorre `implement → validate → deliver` antes de liberar sus dependientes. Una rama de integración requiere una decisión expresa sobre qué evidencia permite liberar cada dependencia.
5. Mostrar los archivos exactos antes de escribir `.scratch/<slug>/issues/<NN>-<slug>.md`. Tras la aprobación y la continuación ejecutora, verificar un archivo por ticket y las relaciones entre ellos. No pasar por triage los tickets ya especificados.
6. Estimar después de acordar el desglose cuando sea necesario para un compromiso: rango, confianza, supuestos, riesgos y exclusiones. Separar esfuerzo de espera, revisión y despliegue. Francisco confirma los compromisos; el agente no inventa duraciones. Si no hace falta estimar, esta actividad no condiciona el cierre de la fase.
7. Crear `## Tickets` en TASK.md con la tabla definida en [trazabilidad](../traceability.md). Es la única fuente del progreso de los tickets; los archivos conservan contenido y dependencias. Las etiquetas del plugin no demuestran implementación ni integración. Las dudas pendientes no impiden terminar planificación; cada ticket identifica las cuestiones de las que depende su ejecución.

## Actualización de TASK.md

- Estado, fechas y encargo de `plan`.
- Tabla `ID | Tarea | Estado | Inicio | Fin`: título enlazado al archivo, estado inicial `PENDING` y fechas vacías hasta la ejecución.
- Preguntas nuevas y retirada de las resueltas. Registrar la condición de integración acordada y, cuando exista, estimación confirmada con fecha y supuestos relevantes.
- Si se omite `plan`, no crear la sección de tickets.

**DONE:** desglose aprobado por Francisco, cobertura y archivos comprobados, dependencias identificadas, integración acordada y tabla de seguimiento creada. Una estimación solo es necesaria cuando exista un compromiso que la requiera.

**Siguiente:** seleccionar con Francisco un ticket disponible y preparar `implement` en una sesión nueva.
