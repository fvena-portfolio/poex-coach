# Trazabilidad temporal y progreso

Lee esta referencia al crear, finalizar o reabrir una tarea o fase.

## Instantánea YAML

El YAML de `TASK.md` es la fuente de verdad para el estado actual legible por máquinas. Contiene:

| Campo | Contenido |
|---|---|
| `key` | Clave oficial de la tarea. |
| `title` | Título oficial vigente. |
| `jira_url` | URL de la tarea oficial para `workflow: implementation`. |
| `workflow` | Workflow que controla el expediente. |
| `state` | Estado local canónico de la tarea. |
| `assurance_level` | Nivel de garantía confirmado o `PENDING`. |
| `current_phase` | Clave semántica de la fase actual definida en el enrutamiento de `SKILL.md`. |
| `current_step` | Key del paso interno o de la tarea activa; `null` cuando la fase no los diferencie. |
| `started_at` | Inicio real de la tarea. |
| `updated_at` | Momento de la última actualización verificada del expediente. |
| `completed_at` | Fin real de la tarea o `null` mientras siga abierta. |
| `components` | Nombres exactos de los componentes registrados en Jira. |

Usa cadenas ISO 8601 entre comillas para las fechas. Usa `components: []` mientras Jira no haya devuelto ningún componente. No traduzcas, normalices ni infieras sus valores.

Cada workflow conserva únicamente la URL de su fuente principal. `implementation` usa `jira_url`. Un workflow de revisión usa `pr_url` en su propia plantilla. No incluyas campos de fuente vacíos que pertenezcan a otro workflow.

Cuando la fase tenga varios pasos internos, `current_step` contiene una key corta en inglés definida por esa fase. Cuando organice el trabajo mediante tareas, contiene la clave estable de la tarea activa. Cuando la fase no diferencie pasos ni tareas, usa `current_step: null`.

Conserva el título y las fechas de inicio y fin únicamente en el YAML. El cuerpo comienza en `## Progreso`.

`current_phase` usa una clave semántica. El número de fase y el progreso `<fase>/10` se derivan del enrutamiento; no se almacenan en el YAML.

Mantén la instantánea y el cuerpo coherentes en una sola actualización:

- `started_at` se establece al crear el expediente y no cambia;
- `updated_at` cambia en cada escritura verificada;
- `current_phase` cambia al iniciar o reabrir una fase;
- `current_step` cambia al iniciar otro paso o tarea dentro de la fase;
- `components` refleja la última respuesta oficial comprobada de Jira;
- `completed_at` permanece en `null` hasta que la tarea termina;
- al cerrar la tarea, `state`, `current_step`, `completed_at` y `updated_at` se actualizan juntos.

## Marcas temporales

Usa la hora real del sistema en formato ISO 8601 y con zona horaria, por ejemplo `2026-10-27T16:35:42+01:00`.

Registra:

- inicio y fin de la tarea en `started_at` y `completed_at`;
- inicio y fin de cada fase;
- reaperturas de una fase.

La tarea comienza cuando su expediente está creado y se inicia la primera fase. La fecha de creación o asignación en Jira no demuestra el inicio del trabajo.

Una fase termina cuando su puerta está evaluada y el resultado está registrado. Usa `NOT_RECORDED` cuando una transición anterior carezca de una hora comprobable; no la estimes.

## Registro

La sección `## Progreso` contiene una única tabla:

| Fase | Estado | Inicio | Fin |
|---|---|---|---|

Al crear el expediente, añade las diez keys del enrutamiento. `understand` comienza en `IN_PROGRESS`; las demás fases comienzan en `PENDING`.

Usa únicamente la key de la fase en la primera columna. El nombre y la posición se obtienen del enrutamiento de `SKILL.md`.

La última fila cuya key coincida con `current_phase` representa la ejecución actual. Su estado debe coincidir con `state` en el YAML.

Los pasos internos no se registran en esta tabla. `current_step` conserva únicamente el paso o tarea activa; la referencia de la fase determina la siguiente acción.

Conserva resultados y evidencia en sus secciones propias, no en la tabla de progreso.

No sobrescribas una fase terminada. Si debe reabrirse, añade al final una nueva fila con la misma key, estado `IN_PROGRESS`, su nueva fecha de inicio y fin vacío. Registra el motivo de la reapertura en la sección correspondiente.

El progreso `<fase>/10` se deriva de `current_phase` y del enrutamiento. No se almacena en `TASK.md`.

## Transiciones

Reduce las escrituras sin perder trazabilidad:

- al crear el expediente, registra juntos `started_at`, `updated_at`, `current_phase: understand` y la tabla inicial;
- al cambiar de paso o tarea dentro de una fase, actualiza juntos `current_step` y `updated_at`;
- cuando cambie el estado de la fase activa, actualiza juntos su última fila, `state` y `updated_at`;
- al cambiar de fase, registra juntos el fin y estado `DONE` de la fila actual, el inicio y estado `IN_PROGRESS` de la siguiente, `current_phase`, el primer `current_step` aplicable o `null`, `state` y `updated_at`;
- al cerrar, registra juntos el fin y estado `DONE` de `close`, `state: DONE`, `current_step: null`, `completed_at` y `updated_at`.

Cada actualización sigue el procedimiento automático de persistencia definido en `SKILL.md`.
