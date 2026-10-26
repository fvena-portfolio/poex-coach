# Skills, contextos y artefactos

El mapa se ha validado contra las skills de Matt Pocock 1.3.1. Identifícalas siempre como `$mattpocock-skills:<nombre>`. Si cambia la versión instalada, se deben revisar sus instrucciones, identificadores y ubicaciones de salida antes de utilizarlas.

Las skills de terceros no se modifican para adaptarlas a POEX Coach. El flujo se adapta a su comportamiento.

## Mapa principal

| Fases | Skill | Contexto | Resultado |
|---|---|---|---|
| 1–2 | Sin skill obligatoria | POEX Coach | Prioridad y contexto oficial |
| 3–5 | `$mattpocock-skills:grill-with-docs` | Raíz de POEX Coach | Comprensión, preguntas y decisiones |
| 3–5 | `$mattpocock-skills:domain-modeling` | Raíz de POEX Coach | `GLOSSARY.md` y `docs/adr/` cuando proceda |
| 3–5 | `$mattpocock-skills:to-questionnaire` | `.scratch/<slug>/` | `to-questionnaire-<tema>.md` |
| 4–7 | `$mattpocock-skills:research` | POEX Coach | `.scratch/<slug>/research/<tema>.md` |
| 4–7 | `$poex-pr-guide`, modo `Task-planning readiness` | POEX Coach y repositorios de trabajo | Preparación, contratos, cobertura, riesgos y validación contrastados |
| 6 | `$mattpocock-skills:to-spec` | POEX Coach, tracker local | `.scratch/<slug>/spec.md` |
| 7 | `$mattpocock-skills:to-tickets` | POEX Coach, tracker local | `.scratch/<slug>/issues/<NN>-<slug>.md` |
| 8 | `$mattpocock-skills:handoff` | Contexto de origen | Archivo temporal del sistema |
| 9 | `$mattpocock-skills:tdd` | Repositorio de trabajo | Código y pruebas |
| 10–11 | `$poex-pr-guide`, modos `Full PR review` o `Follow-up revision` | Repositorio o PR | Segunda pasada independiente después de la autorrevisión de Francisco |
| 11 | `$mattpocock-skills:pr` | Repositorio de trabajo | Cuerpo y publicación autorizada del PR |
| 12 | `$mattpocock-skills:retro` | POEX Coach y repositorios | Aprendizajes y candidatos de mejora |

La skill `$mattpocock-skills:implement` no forma parte del recorrido estable. Su versión 1.3.1 ejecuta `$mattpocock-skills:code-review` y crea un commit al terminar, acciones que corresponden a la fase 10 y requieren autorizaciones independientes.

Usa el identificador completo `$mattpocock-skills:<nombre>` tanto al invocar una skill del paquete como al pedir a Francisco que la invoque. La única excepción de este mapa es `$loop-me`, que está instalada fuera del paquete `mattpocock-skills`.

Cuando una skill tenga `disable-model-invocation: true`, pide a Francisco que invoque su identificador exacto en el turno siguiente y espera su respuesta. El coordinador no puede activarla por sí mismo.

## Ubicación de documentos

Son generales y permanecen en la raíz de POEX Coach:

- `GLOSSARY.md`;
- `docs/adr/`;
- `docs/agents/`.

`GLOSSARY.md` y `docs/adr/` se crean o actualizan de forma perezosa. No se duplican por tarea.

Son específicos de una tarea:

```text
.scratch/<slug>/
├── TASK.md
├── spec.md
├── issues/
├── research/
└── to-questionnaire-<tema>.md
```

`.scratch/` es memoria duradera. No se limpia automáticamente.

El código, las pruebas, los prototipos y los commits permanecen en los repositorios de trabajo. `TASK.md` enlaza sus resultados sin copiarlos completos.

Los archivos producidos por `$mattpocock-skills:handoff` y `$mattpocock-skills:improve-codebase-architecture` son temporales. Facilitan cambios de contexto, pero no sustituyen al expediente, la especificación o los tickets.

## Skills condicionales

- `$mattpocock-skills:diagnosing-bugs`: defectos difíciles, regresiones o causas desconocidas.
- `$mattpocock-skills:prototype`: responder una pregunta concreta mediante código desechable y una rama `prototype/<nombre>` autorizada.
- `$mattpocock-skills:wayfinder`: esfuerzos excepcionalmente grandes o poco claros.
- `$mattpocock-skills:improve-codebase-architecture`: explorar límites y alternativas arquitectónicas.
- `$mattpocock-skills:wizard`: crear una herramienta repetible después de observar su necesidad.
- `$mattpocock-skills:triage`: clasificar entradas nuevas, no tickets creados por `$mattpocock-skills:to-tickets`.
- `$mattpocock-skills:implement-spec`: ejecución paralela aprobada expresamente; no es el recorrido predeterminado.
- `$mattpocock-skills:teach`: comprobar o consolidar comprensión.
- `$loop-me`: queda fuera del flujo estable mientras sea experimental.

Antes de ejecutar una skill, el coordinador identifica su objetivo, directorio, archivos afectados, efectos externos, autorización necesaria y evidencia esperada.

Una skill no concede permisos adicionales ni supera una fase por sí sola.
