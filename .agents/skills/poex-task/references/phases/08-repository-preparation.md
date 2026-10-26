# Fase 8. Preparación de repositorios y handoff

**Objetivo:** preparar con seguridad los repositorios y transferir un ticket disponible a un contexto nuevo.

**Entrada:** fase 7 superada, ticket de la frontera seleccionado y autorización para preparar repositorios.

**Acciones:**

1. Confirmar comportamiento, criterios, bloqueadores, repositorios, contratos y evidencia del ticket.
2. Leer `AGENTS.md`, `README.md`, reglas SCM y comandos de validación de cada repositorio.
3. Inspeccionar rama, `HEAD`, upstream, ramas base, working tree, índice, archivos sin seguimiento, commits locales, operaciones incompletas y worktrees.
4. Comparar con la fase 4 y consultar GitHub en modo de solo lectura cuando sea necesario.
5. Clasificar cualquier cambio local. No usar `stash`, `reset`, `clean`, cambio de rama, rebase, merge o modificación del índice sin decisión expresa.
6. Considerar un worktree autorizado cuando varias tareas no puedan aislarse con seguridad.
7. No modificar `poex-infra`.

Las reglas específicas del repositorio prevalecen. Como fallback:

| Trabajo | Origen habitual | Rama |
|---|---|---|
| Funcionalidad | `develop` | `feature/POE-<n>-<titulo-jira-kebab>` |
| Corrección | `develop` | `bugfix/POE-<n>-<titulo-jira-kebab>` |
| Release | `develop` | `release/x.y.z` |
| Hotfix de producción | `main` | `hotfix/x.y.z` |

La base habitual del PR será `develop`, la rama de hotfix o la rama de release según el flujo. El sufijo usa el título oficial de Jira en kebab-case.

Fallback de commits:

```text
<type>(<scope>): <descripción> (POE-<n>)
```

Tipos:

```text
feat, fix, docs, style, refactor, perf, test, build, ci, chore, revert
```

Los commits son atómicos y reversibles. Las reglas y `commitlint` del repositorio prevalecen.

8. Mostrar por repositorio estado inicial, preservación, origen, destino, actualización necesaria, comandos, validaciones y recuperación.
9. Obtener autorización antes de mutar.
10. Con autorización, preservar el trabajo, actualizar referencias, situarse en la base, avanzar de forma segura y crear o reutilizar la rama.
11. Detenerse ante divergencias o conflictos. No usar `reset --hard`, `clean` ni force push.
12. Ejecutar la línea base proporcional: dependencias, generación, lint, tipos, pruebas, build o health check.
13. Separar fallos preexistentes de fallos introducidos.
14. Pedir a Francisco que invoque `$mattpocock-skills:handoff` hacia el repositorio de implementación.
15. El handoff temporal referencia ticket, especificación, criterios, decisiones, repositorios, rama, `HEAD`, línea base, validaciones, riesgos y evidencia esperada.
16. Mostrar el handoff exacto antes de escribirlo.
17. Proponer la actualización exacta de `TASK.md`.

**Resultado:** repositorios preparados, línea base conocida y handoff autosuficiente.

**Evidencia:** estado Git anterior y posterior, autorización, commits base, línea base, handoff y expediente aprobado.

**Puerta de salida:**

- `SUPERADO`: el ticket está disponible, el trabajo previo está protegido y la implementación puede comenzar.
- `REVISAR`: falta preservar, validar, preparar o completar el handoff.
- `BLOQUEADO`: un conflicto, divergencia, cambio desconocido o fallo impide avanzar.

**Siguiente paso:** fase 9 en un contexto nuevo del repositorio.

