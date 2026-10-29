---
name: poex-task
description: "Inicia o reanuda una tarea de desarrollo de POEX Coach; prepara encargos con skills y verifica sus resultados en TASK.md."
---

# Flujo de tareas de POEX Coach

Coordina la tarea desde su comprensión hasta su cierre. `AGENTS.md` conserva la autoridad sobre decisiones, permisos, fuentes y estados. Jira permanece en solo lectura: prepara las modificaciones exactas para que Francisco las aplique y verifica el resultado.

Francisco controla los servidores locales desde sus terminales visibles. El coach y las sesiones ejecutoras comprueban su estado y le indican cuándo y cómo arrancarlos, reiniciarlos o pararlos; no realizan esas operaciones. Aplica [servidores locales](references/workspaces.md#servidores-locales) y conserva esta regla en los encargos.

## Papeles

Francisco selecciona la tarea y conduce el flujo. El **coach** sugiere, prepara el encargo, comprueba los resultados accesibles y es el único agente que actualiza `TASK.md`. La **sesión ejecutora** aplica el prompt de Francisco y devuelve evidencias. Si recibes un encargo de ejecución, lee [encargos](references/assignments.md) y ejecuta ese encargo; no inicies el recorrido del coach ni escribas el expediente.

Mantén un solo coach escritor por expediente. Antes de sustituirlo, cierra su sesión con continuidad. Distintas tareas pueden tener coaches distintos y espacios de trabajo independientes.

## Inicio y reanudación del coach

1. Localiza `.scratch/*/TASK.md`. Una referencia explícita selecciona su expediente; sin referencia, reanuda el único abierto o pide seleccionar uno si hay varios. Para una tarea nueva, verifica que Jira existe, puede leerse y no está cerrada ni cancelada antes de crear el expediente.
2. Gestiona únicamente `workflow: implementation`. Usa [trazabilidad](references/traceability.md) y [la plantilla](assets/TASK.template.md). Un expediente de una versión anterior requiere la conciliación descrita en trazabilidad, sin perder historia ni inventar datos.
3. Lee identidad, estado, `current_phase`, `current_step` y `active_assignment`. Compara la última ejecución de la fase en `## Progreso`. Si hay un encargo abierto, comprueba su situación antes de preparar otro.
4. Lee solo la fase actual y sus referencias condicionales. Al reanudar trabajo sobre código, verifica los espacios registrados mediante [workspaces](references/workspaces.md); la ruta de lanzamiento del chat no selecciona el repositorio de trabajo.
5. Contrasta únicamente las fuentes cuya vigencia pueda cambiar la acción. Ante una discrepancia material, muestra el registro y lo observado y aplica [desviaciones](references/deviations.md).
6. Presenta tarea, prioridad oficial con fecha de comprobación, estado, fase, paso o encargo y siguiente acción. Si desplaza un compromiso más urgente, expón el conflicto antes de cambiar el foco.

## Enrutamiento

| Fase | Clave | Referencia |
|---|---|---|
| 1 | `understand` | [Comprender la tarea](references/phases/01-task-understanding.md) |
| 2 | `initialize` | [Inicializar la tarea](references/phases/02-initialization.md) |
| 3 | `design` | [Investigar y decidir](references/phases/03-design.md) |
| 4 | `specify` | [Especificar](references/phases/04-specification.md) |
| 5 | `plan` | [Dividir y estimar](references/phases/05-tickets-and-estimation.md) |
| 6 | `implement` | [Implementar y revisar](references/phases/06-implementation.md) |
| 7 | `validate` | [Validar la integración](references/phases/07-validation.md) |
| 8 | `deliver` | [Entregar y seguir](references/phases/08-delivery.md) |
| 9 | `close` | [Cerrar y aprender](references/phases/09-closure.md) |

La ruta completa usa las nueve fases. Tras `design`, Francisco elige `specify`, `plan` sin especificación separada, o `implement` directamente para un cambio pequeño y definido que cabe en una sesión. La fase de diseño contiene la guía que se muestra después de su prompt y la consulta opcional a `ask-matt`. Registra la ruta elegida y su fundamento; marca `SKIPPED` las fases opcionales omitidas según trazabilidad. Las restantes puertas mantienen sus criterios.

Lee [garantía](references/assurance.md) al clasificar la tarea al final de `design` o cambiar el riesgo. Lee [skills](references/skills.md) y [encargos](references/assignments.md) al preparar un prompt, elegir sesión o comprobar un retorno. Lee [workspaces](references/workspaces.md) al preparar, reanudar o cambiar un repositorio. Lee [trazabilidad](references/traceability.md) al escribir el expediente.

## Control de resultados

1. Comprueba la entrada de la fase y las autorizaciones vigentes.
2. Realiza la acción del coach o prepara el encargo de ejecución correspondiente.
3. Al recibir el retorno, contrasta cada criterio con fuentes y evidencias. En `design`, aplica su contrato de feedback: la finalización la confirma Francisco y el coach declara ese límite de comprobación. En las demás fases, un aviso de finalización o un informe no superan la puerta por sí solos.
4. Francisco revisa y decide en los puntos definidos por cada fase. Aclara las dudas que afecten a su decisión sin añadir exámenes o repetir explicaciones como puerta de cierre.
5. Registra el resultado comprobado. Avanza solo desde `DONE`, dentro de la ruta acordada. Un cambio de alcance reabre la primera fase afectada.

Las fases definen su criterio `DONE`; cualquier carencia conserva `IN_PROGRESS`, salvo que corresponda `WAITING`, `BLOCKED` o `PAUSED` según `AGENTS.md`. Identifica siempre la causa y la condición de continuación. Las preguntas abiertas se registran sin bloquear por sí solas las fases; las operaciones y validaciones que necesiten una respuesta mantienen su dependencia.

## Persistencia y cierre

El coach crea y actualiza automáticamente `.scratch/<slug>/TASK.md` con hechos comprobados y decisiones ya tomadas, verifica cada escritura e informa de forma compacta. Otros archivos y sistemas mantienen sus autorizaciones específicas.

El expediente conserva la instantánea, el progreso, las decisiones necesarias, los encargos y los enlaces a evidencia. Usa el slug estable de Jira en minúsculas. La memoria `.scratch/` es duradera.

Antes de cambiar de sesión, registra el punto real de continuación. Termina con una sola siguiente acción: una decisión pendiente, el prompt listo para copiar o la comprobación de un retorno.
