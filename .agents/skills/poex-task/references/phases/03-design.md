# Fase 3. Investigar y decidir

**Entrada:** `understand` e `initialize` en `DONE`; workspaces verificados y preguntas pendientes disponibles.

**Encargo principal:** `$mattpocock-skills:grill-with-docs`, en una sesión de planificación abierta en POEX Coach. El prompt enlaza Jira, TASK.md y los workspaces e impone una pregunta o decisión por turno.

Cuando la tarea afecte a varios repositorios, el prompt debe indicar que se realizará un único diseño de la funcionalidad completa. Enumerará los repositorios afectados y sus workspaces verificados. Pedirá analizar las responsabilidades de cada uno, los contratos que los conectan, la compatibilidad, las dependencias y las comprobaciones del comportamiento conjunto. La especificación y el desglose posteriores conservarán este alcance común.

## Resultado que debe producir

- Modelo del comportamiento actual respaldado por código y pruebas vigentes: entradas, responsabilidades, datos, permisos, errores y contratos entre repositorios que cambian la decisión.
- Distinción entre hechos, hipótesis y decisiones de producto o técnicas. El agente investiga los hechos; Francisco decide con opciones, consecuencias y recomendación razonada.
- Cuestiones previas revisadas, distinguiendo respuestas, decisiones confirmadas y preguntas que siguen abiertas. Evitar repetir lo ya resuelto. Identificar destinatario y siguiente acción cuando se conozcan; Francisco autoriza cualquier comunicación.
- Comportamiento esperado, alcance, contratos, compatibilidad, límites y forma de comprobarlo. Un prototipo o investigación es un desvío acotado que devuelve evidencia a este resultado.

Las escrituras de glosario o ADR siguen las autorizaciones de AGENTS.md. Las conclusiones de diseño se trabajan en la conversación ejecutora y se trasladan a la especificación o tickets cuando se elijan esas fases; no se exige `design.md` ni copiar los hallazgos al expediente. Antes de cambiar de sesión, conservar la continuidad necesaria en un destino autorizado.

## Cierre de la entrega del prompt

Después del prompt de `grill-with-docs`, muestra el siguiente bloque al usuario. Es una guía para cuando termine la sesión; entregar el prompt no demuestra que la fase haya comenzado ni terminado. `ask-matt` es opcional y lo activa Francisco en la sesión ejecutora.

---

Cuando termines `grill-with-docs`, elige cómo continuar:

| Ruta | Cuándo elegirla | Qué indicar al coach |
|---|---|---|
| **`to-spec → to-tickets → implement`** | El trabajo ocupará varias sesiones y necesita una especificación común. Primero documenta lo acordado; después divídelo en tickets. | `specify` |
| **`to-tickets → implement`** | Lo acordado está claro y puedes dividirlo directamente en tareas verificables, con sus dependencias. | `plan` |
| **`implement`** | El cambio es pequeño, está bien definido y cabe en una sola sesión. Aprovecha el contexto actual para implementarlo. | `implement` |

**Si necesitas una recomendación**, envía este prompt en la misma conversación donde has usado `grill-with-docs`:

> Usa `$mattpocock-skills:ask-matt`. Según lo trabajado en esta conversación, ¿recomiendas continuar con `to-spec`, `to-tickets` o `implement`? Explica brevemente por qué. No ejecutes el siguiente paso.

Cuando decidas, vuelve al coach e indica:

> He terminado diseño. Quiero continuar con `<specify | plan | implement>`.

El coach preparará el siguiente prompt e indicará dónde utilizarlo:

- **Especificación y tickets:** en la misma conversación de diseño.
- **Implementación directa:** en esa misma conversación.
- **Implementación de un ticket:** en una conversación nueva por ticket.

**Para pedir feedback al equipo**, usa `$poex-proposal frontend` o `$poex-proposal backend` en la conversación donde hayas usado `grill-with-docs`. Sustituye el argumento por el repositorio que quieras consultar. Obtendrás un resumen breve de la tarea y la solución propuesta, listo para copiar y compartir con sus desarrolladores.

---

## Feedback y siguiente encargo

1. Francisco comunica que ha terminado la revisión de diseño y elige `specify`, `plan` o `implement`. Puede aportar la recomendación de `ask-matt`; el coach sugiere y Francisco decide.
2. Registra la finalización como confirmada por Francisco. El coach no presupone acceso a la conversación ejecutora ni presenta su contenido como revisado por él. La elección de ruta por sí sola no confirma que se haya realizado el diseño.
3. Añade a `## Preguntas pendientes` las cuestiones abiertas que Francisco comunique y retira las resueltas. Las dudas abiertas no impiden por sí solas pasar a la siguiente fase; las acciones que dependan de sus respuestas conservan esa dependencia.
4. Aplica [garantía](../assurance.md) con la evidencia disponible y confirma el nivel. Registra la ruta elegida y las omisiones según [trazabilidad](../traceability.md), sin marcar como realizadas las fases omitidas.
5. Cierra el encargo de diseño antes de preparar el siguiente. Actualiza el estado y progreso de TASK.md y entrega el prompt correspondiente, indicando expresamente la sesión. Para `specify`, `plan` o implementación directa se conserva la conversación de diseño mientras siga siendo útil y tenga capacidad.

## Actualización de TASK.md

Registrar estado, fechas, ruta elegida y nivel confirmado, con la procedencia del feedback. Añadir las preguntas abiertas comunicadas y retirar las resueltas. Marcar las fases omitidas `SKIPPED` según trazabilidad. Mantener el encargo mientras esté abierto; no duplicar la conversación ni crear un informe de diseño.

**DONE:** Francisco confirma que ha terminado la revisión de diseño; nivel y ruta confirmados; preguntas comunicadas actualizadas. La evidencia de finalización es su confirmación, no una revisión del chat ejecutor por el coach.

**Siguiente:** la fase elegida por Francisco: `specify`, `plan` o `implement`.
