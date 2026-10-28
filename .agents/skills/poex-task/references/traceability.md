# Estado, evidencia y continuidad

## Instantánea YAML

El coach es el único escritor de TASK.md. Actualiza hechos y decisiones confirmadas, verifica la escritura e informa de forma compacta. Conserva las fechas reales en ISO 8601 con zona Europe/Madrid; usa `NOT_RECORDED` cuando una fecha histórica sea desconocida.

| Campo | Contenido |
|---|---|
| `workflow_version` | `3`: comprensión e inicialización separadas, fases omitidas `SKIPPED` y progreso de tickets en una única tabla. |
| `key`, `title`, `jira_url` | Identidad oficial verificada; `workflow: implementation`. |
| `state` | Estado canónico de la fase activa y, por tanto, de la tarea. |
| `assurance_level` | Nivel confirmado o `PENDING` hasta terminar diseño. |
| `phases` | Keys de la ruta acordada, en orden. Inicialmente las nueve del enrutamiento; retirar de esta ruta las fases omitidas, conservándolas en `## Progreso`. |
| `current_phase` | Fase activa por key, no por número. |
| `current_step` | Paso de comprensión o inicialización, ticket activo o acción verificable de la fase; `null` si no se necesita. |
| `started_at`, `updated_at`, `completed_at` | Inicio real, última actualización y cierre; `completed_at: null` hasta terminar. |
| `components` | Valores exactos del campo oficial de Jira; `[]` si Jira devolvió lista vacía. |
| `workspaces` | Asignaciones según [workspaces](workspaces.md); `[]` hasta prepararlas. |
| `active_assignment` | Encargo abierto o `null`, según el contrato siguiente. |

Las etiquetas de triaje como `ready-for-agent` no son estados canónicos. Las dependencias se liberan con la condición de integración acordada en planificación; completar la fase de implementación no marca automáticamente el ticket `DONE`.

## Encargo abierto

`active_assignment` contiene:

- `id`: identificador único en el expediente, por ejemplo `POE-8958-design-001`; no reutilizarlo para otro alcance.
- `phase`, `unit`: key de fase y ticket o unidad (`null` si no aplica).
- `skill`, `skill_version`: identificador explícito y versión comprobada.
- `state`: `PENDING` al preparar; `IN_PROGRESS` al confirmar inicio y durante verificación; los demás estados canónicos según evidencia.
- `session`: indicación de sesión nueva o referencia a la anterior; nombre/enlace/identificador si se conoce, nunca inventado.
- `workspace_ids`: asignaciones incluidas en el encargo.
- `inputs`: rutas/URLs y sus SHA o huellas disponibles; incluir TASK.md como referencia, pero no fijar su huella porque el coach actualiza el estado durante la espera.
- `authorized_actions`: alcance exacto y procedencia de las autorizaciones confirmadas. Vacío significa solo lectura y propuesta en el chat. Las acciones pendientes figuran como pendientes en el prompt.
- `created_at`, `started_at`, `returned_at`: fechas reales; las dos últimas, `null` mientras el evento no se confirme.

`## Encargo actual` conserva el prompt exacto. La sesión ejecutora puede tener limitado el acceso a los workspaces o herramientas; registrar la asignación no amplía los permisos del entorno.

Al retornar, la fase vuelve de `WAITING` a `IN_PROGRESS` para verificar. El encargo solo queda `DONE` tras contrastar todos sus criterios. Archiva su resultado y evidencias antes de retirarlo. Una continuación conserva referencia al encargo anterior y usa un nuevo id. No marques como realizado un encargo detenido ni pierdas su resultado parcial.

## Cuerpo del expediente

- `## Resumen`: objetivo breve.
- `## Progreso`: tabla de ejecuciones de fases y fases omitidas.
- `## Artefactos`: enlaces a documentos producidos y comprobados, con versión o huella cuando corresponda; solo cuando existan.
- `## Tickets`: tabla única de progreso de tickets; solo cuando se hayan generado archivos.
- `## Decisiones y continuidad`: decisiones confirmadas, razones relevantes, ruta acordada, bloqueos/seguimientos y siguiente acción; solo cuando haya contenido.
- `## Resultados y evidencia`: referencias verificadas por fase, ticket, workspace o encargo, con los límites de la comprobación; solo cuando haya contenido.
- `## Preguntas pendientes`: preguntas técnicas y externas en una lista común para facilitar consultas agrupadas. Conservar texto y contexto mínimos, destinatario o fase prevista si se conocen y acción dependiente cuando exista. Retirar al resolverse; las respuestas relevantes pertenecen al artefacto de trabajo correspondiente. No inventar responsables ni respuestas.
- `## Encargo actual`: únicamente mientras exista encargo abierto.

Conserva otras secciones históricas si contienen evidencia que aún no se ha conciliado. El expediente enlaza los artefactos; no duplica especificaciones ni tickets. Comprensión conserva solo progreso y preguntas; inicialización añade el registro operativo de workspaces. No crear informes narrativos ni evaluaciones personales por defecto.

## Tickets

Crear esta sección únicamente cuando `plan` haya producido archivos aprobados y comprobados:

| ID | Tarea | Estado | Inicio | Fin |
|---|---|---|---|---|
| `<id>` | `<título enlazado a la ruta absoluta del archivo>` | `PENDING` | — | — |

La tabla es la única fuente del progreso de los tickets: no duplicar sus estados en YAML ni en los archivos. Los archivos conservan comportamiento, criterios y dependencias. `ready-for-agent` es una etiqueta de preparación, no un estado de ejecución.

- Registrar inicio cuando Francisco confirme la ejecución real, no al crear el ticket o preparar su prompt.
- Usar los estados canónicos según la situación del ticket; una espera o bloqueo incluye responsable y condición de continuación.
- `implement: DONE` o `validate: DONE` no cierran el ticket. Registrar `DONE` y fin cuando satisfaga criterios y condición de integración acordada.
- Ante reapertura, conservar el cierre anterior y su motivo en el historial; actualizar la fila a su estado actual y dejar `Fin` vacío hasta el nuevo cierre. Mantener el inicio original. Las ejecuciones de fases distinguen cada ciclo.
- Consultar las dependencias en los archivos antes de proponer el siguiente ticket; completarlas se evalúa según la condición de integración acordada.
- Sin tickets, omitir la sección y registrar la unidad con `—` en el progreso de las fases.

## Preguntas y criterios pendientes

Una pregunta abierta no bloquea por sí sola una fase ni obliga a reabrir la anterior. Registrar qué acción necesita su respuesta y realizar el trabajo independiente. Un criterio de salida de la fase no satisfecho, una validación necesaria pendiente o una operación imprescindible sin autorización sí mantienen abierto el resultado que depende de ellos. La omisión de una fase no resuelve esas dependencias.

## Progreso y transiciones

La tabla contiene `Fase | Unidad | Estado | Inicio | Fin`. Inicializa las fases de `phases`: `understand` en `IN_PROGRESS`, el resto en `PENDING`, con unidad `—`. La unidad identifica el ticket cuando se repiten implementación, validación y entrega.

La última fila de `current_phase` representa su ejecución actual y coincide con `state`. Al volver a una fase terminada, añade otra fila con unidad y motivo de reapertura; preserva su historia. Los pasos internos se identifican solo por `current_step`.

- Al cambiar de paso, actualiza `current_step` y `updated_at`.
- Al cambiar de estado, actualiza juntos YAML y fila activa. `WAITING` requiere responsable y condición de reanudación registrados.
- Al completar una fase e iniciar otra, registra en una escritura su `DONE` y fin, el inicio de la siguiente, `current_phase`, `current_step`, `state` y `updated_at`.
- Cuando Francisco omita una fase opcional, retirarla de `phases` y mantener su fila en `## Progreso` como `SKIPPED`, con inicio y fin `—`. Registrar fecha, motivo y autor de la decisión en continuidad. `SKIPPED` solo se usa para fases omitidas, nunca como estado general de la tarea, ticket o encargo.
- Conservar cualquier ejecución anterior si cambia la ruta; añadir una fila `SKIPPED` para reflejar la nueva decisión sin reescribir fechas ni resultados anteriores. Si se reincorpora una fase, añadirla a `phases` y abrir una nueva ejecución con fechas reales.
- Registrar la finalización de `design` con Francisco como fuente de confirmación; el coach no atribuye una revisión propia al chat ejecutor que no ha consultado.
- Conservar causa, inicio y resolución de esperas o bloqueos relevantes al cambiar el estado, para que la actualización de la instantánea no borre su evolución.
- Al cerrar, registra juntos `close: DONE`, `state: DONE`, `completed_at`, `current_step: null` y `updated_at`. No debe quedar un encargo abierto.

No interpretes el tiempo entre inicio y fin como esfuerzo dedicado sin confirmación. El número de fase se deriva del enrutamiento; no almacenes un contador como `6/8`.

## Expedientes anteriores

Al detectar una versión ausente o anterior, conserva la identidad, historia, decisiones y evidencia. Reconstruye campos solo desde fuentes comprobadas; una contradicción material se consulta con Francisco.

Para versión 2, separar conceptualmente la comprensión de `understand` y su preparación de repositorios, que ahora corresponde a `initialize`; conservar la fila histórica y comprobar la preparación vigente antes de completar la nueva fase. Trasladar entradas de `tickets` del YAML a `## Tickets` conservando ids, enlaces y estados. Usar `NOT_RECORDED` para fechas desconocidas. Contrastar sus dependencias con los archivos; conservar el registro anterior hasta conciliar las diferencias, sin modificar los tickets automáticamente.

Para versiones anteriores, `research` y `decide` corresponden a `design`; `prepare` corresponde a la preparación de `initialize`. `specify`, `plan`, `implement`, `validate`, `deliver` y `close` conservan su significado con las nuevas puertas. La historia original permanece identificada.

No conviertas automáticamente una fase vieja en `DONE` bajo requisitos nuevos. Mantén los registros anteriores como historia identificada; añade una ejecución nueva de la fase que corresponda y comprueba sus criterios. Un resultado anterior válido se reutiliza por referencia, no se repite por burocracia.

Si el estado Git actual difiere del registro, conserva ambos como observaciones con sus fechas; no reescribas el pasado ni inventes workspaces. Antes de emitir un encargo escritor deben estar resueltas las discrepancias de identidad y registrados los workspaces reales. Las autorizaciones antiguas no se amplían por la migración.
