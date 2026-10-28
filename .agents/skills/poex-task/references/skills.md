# Skills, contextos y artefactos

Mapa contrastado con Matt Pocock 1.3.1. Antes de preparar un encargo, lee la skill instalada y sus recursos necesarios. Si cambia su versión, comprueba instrucciones, invocación, salidas y efectos antes de reutilizar el prompt.

El coach prepara la invocación explícita; Francisco la envía siguiendo [encargos](assignments.md). Conserva el plugin original. Las skills auxiliares invocables por el agente pueden utilizarse dentro del encargo conforme a sus instrucciones y permisos.

| Fase | Skill principal | Resultado y contexto |
|---|---|---|
| `understand` | Flujo propio | Tarea revisada y preguntas abiertas identificadas. |
| `initialize` | Flujo propio | Workspaces autorizados, preparados y verificados. |
| `design` | `$mattpocock-skills:grill-with-docs` | Sesión de planificación en POEX Coach; hechos investigados en workspaces y decisiones acordadas. |
| `specify` | `$mattpocock-skills:to-spec` | Misma sesión; especificación local. |
| `plan` | `$mattpocock-skills:to-tickets` | Misma sesión; tickets locales con bloqueadores. |
| `implement` | `$mattpocock-skills:implement` | Sesión nueva por ticket, o la misma de diseño para implementación directa; TDD y revisión con los límites de la fase. |
| `validate` | Comprobaciones del proyecto | Evidencia conjunta y cobertura cross-stack. |
| `deliver` | `$mattpocock-skills:pr` | Cuerpo de PR; publicación y seguimiento sujetos a autorización. |
| `close` | `$mattpocock-skills:retro` cuando aporte valor | Recuperar retrospectiva existente o proponerla en la sesión evaluada; cierre comprobado. |

`implement` 1.3.1 pide ejecutar `code-review` antes de hacer commit, pero `code-review` usa `<base>...HEAD`. El encargo adapta explícitamente ese orden: código y pruebas; retorno para un commit autorizado; revisión sobre los commits existentes. Si no se autoriza el commit, devuelve el diff y deja pendiente esa revisión. No presentes la revisión de un HEAD anterior como revisión del trabajo sin commit. Las correcciones posteriores requieren nueva evidencia sobre su contenido final.

## Artefactos

El tracker de las skills es el local de POEX Coach: lee `docs/agents/issue-tracker.md` desde su ruta absoluta aunque el cwd sea otro repositorio. Jira conserva el alcance y estado oficiales. Los tickets locales son unidades de implementación, no nuevas subtareas oficiales.

- `.scratch/<slug>/TASK.md`: expediente, escrito solo por el coach.
- `.scratch/<slug>/spec.md`: especificación.
- `.scratch/<slug>/issues/<NN>-<slug>.md`: un archivo por ticket.
- `.scratch/<slug>/research/<tema>.md`: investigación cuando justifique un artefacto.
- `.scratch/<slug>/to-questionnaire-<tema>.md`: cuestionario cuando proceda.
- `GLOSSARY.md` y `docs/adr/` de POEX Coach: vocabulario y decisiones generales, creados de forma perezosa; las decisiones de dominio específicas del repositorio respetan su documentación propietaria. Evita duplicar una decisión entre repositorios: usa referencias.

La creación o modificación de esos archivos, excepto TASK.md por el coach, requiere mostrar el cambio exacto y obtener aprobación. Si falta, la salida del encargo es una propuesta en el chat y la escritura queda pendiente. La configuración de un tracker local no concede permiso para escribir.

Código, pruebas y prototipos viven en los workspaces autorizados. Los handoffs son temporales y enlazan fuentes duraderas. Los informes de revisión se conservan por referencia o mediante un resumen verificable en TASK.md; el retorno no crea automáticamente otro documento.

## Desvíos y apoyos

Usa un encargo específico cuando la necesidad exista: `prototype` para una pregunta ejecutable; `research` para investigación acotada; `to-questionnaire` para conocimiento externo; `diagnosing-bugs` para un defecto difícil. Lee su SKILL.md antes de elegirlo. Sus salidas vuelven al diseño o al criterio que las necesita.

`$poex-pr-guide` aporta contraste de planificación, revisión o seguimiento cuando hay una necesidad POEX concreta. Aplica su checkpoint humano. En validación, delimita qué contratos o requisitos aún no están cubiertos por la revisión de Matt para evitar repetirla sin aportar evidencia.

`implement-spec` es una ruta excepcional que requiere acuerdo explícito sobre agentes, worktrees, integración y permisos. No la actives al disponer simplemente de varios tickets. La ruta ordinaria mantiene un ticket ejecutándose por tarea. Las etiquetas de triaje del plugin describen disponibilidad; los estados de ejecución siguen siendo los canónicos de AGENTS.md.
