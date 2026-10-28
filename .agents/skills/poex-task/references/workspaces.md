# Espacios de trabajo por tarea

## Preparación

Un workspace asigna una tarea, un repositorio y un uso a un directorio verificable. La ruta principal del repositorio sirve para localizar Git; el trabajo se realiza en la ruta asignada.

1. Inspecciona instrucciones SCM, referencias y `git worktree list --porcelain` antes de proponer cambios. Consulta los expedientes abiertos para detectar asignaciones duplicadas.
2. Para los repositorios afectados, acuerda la rama base con Francisco. Contrasta su vigencia cuando sea material; una referencia remota local no demuestra por sí sola vigencia en GitHub. Registra el SHA base acordado. Actualizar referencias mediante fetch también requiere la autorización aplicable.
3. Propón un worktree por tarea y repositorio. Convención: `/home/franciscovenagualda/Repositories/worktrees/<slug>-<repo-corto>`, por ejemplo `poe-8958-backend`. El nombre final debe ser único también entre revisiones y tickets paralelos.
4. Muestra ruta, rama, base, comandos y efectos exactos antes de crear o reutilizar el workspace. Conserva los cambios y ramas de otros directorios. La aprobación del diseño del flujo no autoriza estas operaciones Git.
5. Reutiliza una rama existente solo tras verificar su contenido y recibir autorización. Si ya está utilizada por otro worktree, conserva esa protección; acuerda la ubicación correcta o una alternativa, sin `--force` ni reseteos.
6. Para una revisión, usa un workspace distinto en detached HEAD fijado al SHA revisado. Si aparece trabajo de corrección, requiere otro encargo y una rama autorizada. Una actualización de la PR exige verificar de nuevo el SHA.
7. Tras preparar cada workspace, verifica y registra su identidad. Si falla uno, conserva los ya creados y registra el resultado parcial; no los elimines como recuperación automática.
8. Identifica comandos y recursos del entorno. En Backend, respeta el repositorio Maven por worktree exigido por su `AGENTS.md`. Puertos, bases de datos, contenedores y resultados deben aislarse cuando puedan interferir. Registra identificadores y rutas, nunca secretos. Si no es posible aislar la ejecución, serializa las operaciones que comparten el recurso.

La fase `initialize` prepara la identidad y conoce cómo validar; `understand` permite consultas puntuales en solo lectura para comprender la tarea. La línea base de comprobaciones pertinentes se ejecuta antes de modificar código, en el workspace de implementación. Registra SHA, estado local, entorno, comandos y resultados; separa fallos previos y carencias de entorno. No atribuyas una prueba al último SHA si se ejecutó sobre otro contenido.

## Registro en TASK.md

`workspaces` es una lista. Cada entrada contiene:

| Campo | Significado |
|---|---|
| `id` | Identificador estable y único dentro de la tarea. |
| `repository` | Identidad del repositorio, sin credenciales. |
| `common_dir` | Ruta absoluta real del directorio Git compartido, obtenida con Git. |
| `path` | Ruta absoluta real del worktree. |
| `purpose` | `implementation` o `review`. |
| `branch` | Rama esperada, o `null` para una revisión detached. |
| `pinned_head` | SHA fijado para una revisión, o `null` para implementación. |
| `base_ref`, `base_sha` | Base acordada y SHA inicial. Un avance remoto no cambia silenciosamente esta base. |
| `last_head` | Último SHA observado y verificado. |
| `verified_at` | Fecha real de la comprobación. |

En `## Resultados y evidencia` conserva cambios locales conocidos, línea base y configuración de ejecución por `id`. Los archivos pendientes pertenecen a la tarea; no se exige un árbol limpio para reanudar.

## Reanudar y comprobar

1. Lee la asignación; nunca elijas un directorio por coincidencia aproximada de nombre ni por el cwd del chat.
2. Ejecuta [verify-workspace.py](../scripts/verify-workspace.py) con `path`, `common_dir`, rama o `pinned_head` y `last_head` del registro. El script comprueba identidad y devuelve observaciones de solo lectura; no concede permisos ni asegura que no haya otro escritor.
3. Compara `HEAD`, cambios staged/unstaged/untracked, upstream, base y operaciones pendientes con el último registro y el encargo. Una diferencia de `HEAD` requiere explicar el avance; no demuestra por sí sola un error ni autoriza actualizar el registro sin revisar.
4. Verifica que no haya otro encargo escritor sobre la misma ruta real. El ejecutor anterior debe haber terminado antes de cederla. Los agentes paralelos necesitan workspaces y ramas distintos; los revisores que necesiten una copia estable usan su propio workspace.
5. Si falla la identidad, el directorio falta o hay trabajo desconocido, detén las modificaciones dependientes y presenta la discrepancia. Reparar, mover, recrear, cambiar rama o limpiar requiere la decisión y autorización correspondientes.
6. Usa `git -C <ruta>` y el directorio explícito de cada herramienta. Repite la comprobación antes de un lote de modificaciones, tras cambiar de contexto y antes de operaciones Git. Lee las instrucciones del workspace, incluidas las del subdirectorio afectado.

La exclusividad es un contrato entre las sesiones participantes, no un bloqueo del sistema operativo. `git worktree lock` no impide ediciones concurrentes. Este flujo no garantiza aislamiento frente a programas o agentes que no sigan el contrato: ante actividad externa detectada, detén la escritura y concilia el estado.

## Ciclo de vida

Añade repositorios nuevos solo cuando su alcance esté acordado; reabre diseño o planificación si cambian los contratos o criterios. Los permisos del sandbox de una sesión nueva deben cubrir los directorios de ejecución; una asignación en TASK.md no los amplía.

Cerrar la tarea no borra worktrees. Antes de proponer su retirada, verifica trabajo pendiente, commits sin preservar y uso por otras sesiones. Elimina o mueve únicamente con autorización específica y verifica después. Conserva las referencias históricas de la tarea.
