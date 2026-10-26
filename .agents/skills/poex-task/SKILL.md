---
name: poex-task
description: "Inicia o reanuda el flujo de POEX Coach para realizar una tarea de desarrollo cuando Francisco proporciona una tarea o existe un TASK.md activo con workflow: implementation."
---

# Flujo de tareas de POEX Coach

Coordina una tarea de desarrollo desde su selección hasta su cierre. `AGENTS.md` conserva la autoridad sobre control humano, autorizaciones, estados, fuentes, seguridad, interacción y continuidad.

Jira permanece en modo de solo lectura. Cuando deba cambiar, prepara la modificación exacta para que Francisco la aplique manualmente y verifica después el resultado.

## Interfaz

Acepta una referencia de tarea o el expediente activo. Devuelve el estado actual y conduce una sola acción o decisión verificable por turno.

No cargues todas las fases. Lee únicamente la referencia de la fase actual y las referencias condicionales que correspondan.

## Inicio

1. Desde la raíz de POEX Coach, localiza `.scratch/*/TASK.md`.
2. Identifica el expediente con `current_focus: true` y las tareas no cerradas.
3. Si no existe expediente y Francisco ha proporcionado una tarea, comienza en la fase 1 sin crear archivos todavía.
4. Si hay varios focos, ninguno entre varias tareas abiertas o una contradicción de prioridad, solicita una sola decisión.
5. Lee del expediente activo `workflow`, `work_state`, `rigor`, `phase`, `phase_status`, `step` y `next_action`.
6. Comprueba las fuentes y repositorios cuya vigencia pueda cambiar la acción actual. Si una fuente necesaria no está disponible, registra la carencia sin inferir su contenido y solicita únicamente el acceso o dato necesario.
7. Presenta de forma compacta prioridad oficial, estado registrado, evaluación actual, fase, paso pendiente y siguiente acción. Si la prioridad oficial no puede verificarse, indícala como pendiente de verificación; el foco activo no demuestra prioridad.

Solo gestiona expedientes con `workflow: implementation`. Los demás workflows requieren su propia skill.

Puede haber varias tareas abiertas, pero solo una con `current_focus: true`.

## Enrutamiento

| Fase | Referencia |
|---|---|
| 1 | [Selección, captura y prioridad](references/phases/01-selection.md) |
| 2 | [Reconstrucción del contexto oficial](references/phases/02-official-context.md) |
| 3 | [Comprensión demostrada del producto](references/phases/03-product-understanding.md) |
| 4 | [Investigación y modelo del sistema actual](references/phases/04-current-system.md) |
| 5 | [Preguntas, alineación y decisiones](references/phases/05-decisions.md) |
| 6 | [Especificación](references/phases/06-specification.md) |
| 7 | [Plan, tickets, validación y estimación](references/phases/07-tickets-and-estimation.md) |
| 8 | [Preparación de repositorios y handoff](references/phases/08-repository-preparation.md) |
| 9 | [Implementación incremental](references/phases/09-implementation.md) |
| 10 | [Validación integral y autorrevisión](references/phases/10-validation.md) |
| 11 | [Pull request, comunicación y feedback](references/phases/11-pull-request.md) |
| 12 | [Cierre y aprendizaje](references/phases/12-closure.md) |

Lee [rigor](references/rigor.md) durante la fase 1 y cuando aparezca un riesgo nuevo, cambie la urgencia, se proponga reducir el nivel o una comprobación pueda ser `NO APLICA`.

Lee [desviaciones](references/deviations.md) únicamente cuando aparezca o ya exista al iniciar información que cuestione un resultado previo, un cambio de alcance, un fallo, un bloqueo, un cambio de foco o una dependencia externa.

Lee [skills y artefactos](references/skills.md) antes de invocar una skill del flujo o decidir dónde debe vivir un artefacto.

## Ejecución de la fase

1. Comprueba que la entrada definida por la fase existe y sigue vigente.
2. Ejecuta únicamente el paso actual y respeta el foco y las autorizaciones de `AGENTS.md`.
3. Conserva la procedencia de cada hecho y evidencia material.
4. Distingue hechos, observaciones, hipótesis, decisiones y recomendaciones cuando puedan confundirse.
5. Evalúa la puerta contra todos sus criterios de salida.
6. Asigna el estado definido en `AGENTS.md` y explica el criterio pendiente cuando no esté superado.

Si la evaluación actual difiere de `phase_status`, muestra ambos estados y su evidencia. Trata `phase_status` como estado registrado hasta que Francisco apruebe su actualización.

La existencia de un documento, commit, prueba o informe no supera por sí sola una fase.

## Persistencia

Antes de crear o modificar `.scratch/<slug>/TASK.md`:

1. prepara el contenido o cambio exacto;
2. muestra los archivos afectados;
3. obtiene la aprobación de Francisco;
4. escribe únicamente el cambio aprobado;
5. verifica el resultado.

Para crear un expediente usa [la plantilla de TASK.md](assets/TASK.template.md). No crees otros artefactos automáticamente.

Cuando exista una clave de Jira, usa su forma estable en minúsculas como `slug`, por ejemplo `poe-8958`.

`work_state` admite `DISPONIBLE`, `EN_CURSO`, `EN_ESPERA`, `BLOQUEADA`, `APARCADA` y `CERRADA`. Cambiar el foco no modifica por sí mismo el estado oficial de Jira.

Registra de forma compacta objetivo, fuentes, alcance, decisiones, riesgos, resultados, evidencia, bloqueos, compromisos, duración confirmada, fricción, aprendizajes, fase, paso y siguiente acción. Enlaza las fuentes oficiales sin copiarlas.

`.scratch/` es memoria duradera y no se limpia automáticamente.

Continúa a la fase siguiente solo cuando la puerta esté `SUPERADO` y el estado esté registrado. Permanece en la fase cuando esté `REVISAR` o `BLOQUEADO`.

## Cierre del turno o de la sesión

Termina cada turno con una sola siguiente acción concreta. Cuando Francisco vaya a detenerse o cambiar de agente, aplica la continuidad definida en `AGENTS.md` y conserva el estado real sin superar criterios pendientes.
