---
name: poex-task
description: "Inicia o reanuda el flujo de POEX Coach para realizar una tarea de desarrollo cuando Francisco proporciona una tarea o existe un TASK.md activo con workflow: implementation."
---

# Flujo de tareas de POEX Coach

Coordina una tarea de desarrollo desde su comprensión y correcta definición en Jira hasta su cierre. `AGENTS.md` conserva la autoridad sobre control humano, autorizaciones, estados, fuentes, seguridad, interacción y continuidad.

Jira permanece en modo de solo lectura. Cuando deba cambiar, prepara la modificación exacta para que Francisco la aplique manualmente y verifica después el resultado.

## Interfaz

Acepta una referencia de tarea o un expediente identificado por su clave. Devuelve el estado actual y conduce una sola acción o decisión verificable por turno.

No cargues todas las fases. Lee únicamente la referencia de la fase actual y las referencias condicionales que correspondan.

## Inicio

1. Desde la raíz de POEX Coach, localiza `.scratch/*/TASK.md`.
2. Si Francisco proporciona una clave o referencia:
   - reanuda el expediente correspondiente cuando exista;
   - si no existe, comprueba que la tarea oficial existe, puede leerse y no está cerrada ni cancelada;
   - si la comprobación es satisfactoria, prepara `TASK.md` con el inicio de la tarea y la fase `understand`;
   - crea el expediente automáticamente, verifica el resultado y comienza el trabajo.
3. Si Francisco no proporciona una referencia:
   - reanuda el único expediente no cerrado, si solo existe uno;
   - si existen varios, muestra clave, `state`, fase y siguiente acción, y solicita únicamente la clave que quiere continuar;
   - si no existe ninguno, solicita la referencia de la tarea.
4. Para un expediente existente, lee del YAML su identidad, estado, fase y paso o tarea actual; comprueba la última fila de esa fase en `## Progreso` y usa la referencia de la fase para determinar la siguiente acción.
5. Solo gestiona expedientes con `workflow: implementation`. Los demás workflows requieren su propia skill.
6. Comprueba únicamente las fuentes cuya vigencia pueda cambiar la acción registrada. Si una fuente necesaria no está disponible, registra la carencia sin inferir su contenido y solicita únicamente el acceso o dato necesario.
7. Presenta de forma compacta la tarea seleccionada, su prioridad oficial, el estado registrado, la evaluación actual, la fase, el paso y la siguiente acción.

Puede haber varias tareas con `state: IN_PROGRESS`. Solo el expediente seleccionado por Francisco está activo en la conversación actual. Al seleccionarlo, compara su prioridad oficial y su urgencia observable con los demás expedientes abiertos. Si desplaza un compromiso más urgente, expón el conflicto y solicita confirmación antes de continuar.

## Enrutamiento

| Fase | Clave | Referencia |
|---|---|---|
| 1 | `understand` | [Comprensión y definición de la tarea](references/phases/01-task-understanding.md) |
| 2 | `research` | [Investigación detallada y modelo del sistema actual](references/phases/02-current-system.md) |
| 3 | `decide` | [Preguntas, alineación y decisiones](references/phases/03-decisions.md) |
| 4 | `specify` | [Especificación](references/phases/04-specification.md) |
| 5 | `plan` | [Plan, tickets, validación y estimación](references/phases/05-tickets-and-estimation.md) |
| 6 | `prepare` | [Validación de repositorios y handoff](references/phases/06-repository-preparation.md) |
| 7 | `implement` | [Implementación incremental](references/phases/07-implementation.md) |
| 8 | `validate` | [Validación integral y autorrevisión](references/phases/08-validation.md) |
| 9 | `deliver` | [Pull request, comunicación y feedback](references/phases/09-pull-request.md) |
| 10 | `close` | [Cierre y aprendizaje](references/phases/10-closure.md) |

Lee [nivel de garantía](references/assurance.md) al clasificar la tarea al final de la fase 2 y cuando aparezca un riesgo nuevo, cambie la urgencia o se proponga reducir el nivel.

Lee [desviaciones](references/deviations.md) únicamente cuando aparezca o ya exista al iniciar información que cuestione un resultado previo, un cambio de alcance, un fallo, un bloqueo, una interrupción o una dependencia externa.

Lee [skills y artefactos](references/skills.md) antes de invocar una skill del flujo o decidir dónde debe vivir un artefacto.

Lee [trazabilidad temporal y progreso](references/traceability.md) al crear, finalizar o reabrir una tarea o fase.

## Ejecución de la fase

1. Comprueba que la entrada definida por la fase existe y sigue vigente.
2. Ejecuta únicamente el paso actual y respeta la tarea seleccionada y las autorizaciones de `AGENTS.md`.
3. Conserva la procedencia de cada hecho y evidencia material.
4. Distingue hechos, observaciones, hipótesis, decisiones y recomendaciones cuando puedan confundirse.
5. Evalúa la puerta contra todos sus criterios de salida.
6. Asigna el estado definido en `AGENTS.md` y explica el criterio pendiente cuando no esté superado.

Si la evaluación actual difiere de la última fila de `current_phase` en `## Progreso`, muestra ambos estados y su evidencia. Actualiza automáticamente esa fila y el `state` del YAML conforme a la evidencia y verifica el resultado.

La existencia de un documento, commit, prueba o informe no supera por sí sola una fase.

## Persistencia

Crea y actualiza `.scratch/<slug>/TASK.md` automáticamente, sin solicitar una aprobación separada, para registrar el estado comprobado del flujo.

1. Deriva el contenido de fuentes y decisiones ya confirmadas.
2. Escribe únicamente la actualización necesaria.
3. Verifica el resultado.
4. Informa después de forma compacta sobre lo registrado.

Esta autorización no permite introducir decisiones, alcance, requisitos, compromisos o conclusiones que Francisco no haya confirmado cuando requieran su juicio.

Para crear un expediente usa [la plantilla de TASK.md](assets/TASK.template.md). No crees otros artefactos automáticamente.

Cuando exista una clave de Jira, usa su forma estable en minúsculas como `slug`, por ejemplo `poe-8958`.

El YAML es la instantánea legible por máquinas definida en la referencia de trazabilidad. El cuerpo contiene únicamente el resumen, el progreso por fases y, cuando existan, las preguntas pendientes.

`state` admite `PENDING`, `IN_PROGRESS`, `WAITING`, `BLOCKED`, `PAUSED` y `DONE`. Este estado local no modifica por sí mismo el estado oficial de Jira.

Mantén `## Resumen` breve y en lenguaje sencillo. Debe expresar el objetivo de la tarea sin reproducir criterios, alcance detallado ni investigación técnica.

Cuando exista una pregunta que no pueda resolverse y deba formularse a otra persona, crea `## Preguntas pendientes` después de `## Progreso`. Conserva únicamente la pregunta y su propietario esperado. Elimina la entrada cuando se resuelva y elimina la sección cuando quede vacía.

Conserva en `TASK.md` las marcas temporales y el progreso definidos en la referencia de trazabilidad. Combina el cierre de una fase con el inicio de la siguiente en una sola actualización.

`.scratch/` es memoria duradera y no se limpia automáticamente.

Continúa a la fase siguiente solo cuando la última fila de la fase actual tenga estado `DONE`. Cualquier otro estado conserva `current_phase`.

## Cierre del turno o de la sesión

Termina cada turno con una sola siguiente acción concreta. Cuando Francisco vaya a detenerse o cambiar de agente, aplica la continuidad definida en `AGENTS.md` y conserva el estado real sin superar criterios pendientes.
