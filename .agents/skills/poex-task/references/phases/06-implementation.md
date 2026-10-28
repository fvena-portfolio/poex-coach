# Fase 6. Implementar y revisar

**Entrada:** ticket disponible y plan `DONE`; en ruta compacta, unidad y criterios acordados en `design`. Workspaces y alcance de escritura autorizados.

## Preparación del coach

1. Revalidar [workspaces](../workspaces.md), instrucciones SCM, base, cambios previos y dependencias del ticket. Una discrepancia operativa se resuelve aquí con las reglas de `initialize`; un cambio de alcance vuelve a diseño o planificación.
2. Identificar los puntos de prueba acordados y ejecutar o encargar la línea base pertinente antes de modificar código. Distinguir fallos preexistentes y de entorno. Un fallo necesario para validar el resultado requiere resolución o una alternativa acordada, no un descarte implícito.
3. Preparar el encargo con `$mattpocock-skills:implement`: sesión nueva por ticket; para implementación directa sin tickets, continuar en la misma conversación de diseño mientras siga siendo útil y tenga capacidad. El prompt indica la sesión y delimita el ticket o unidad acordada, workspaces, pruebas, permisos, decisiones que requieran a Francisco y retorno.

## Ejecución y retornos

La skill conduce TDD: un comportamiento, prueba roja por la razón esperada y mínima implementación verde. Las pruebas observan interfaces públicas acordadas. Si TDD no es viable, devolver la limitación y una alternativa para decisión de Francisco.

Conservar evidencia proporcional de los incrementos y del comportamiento cross-stack. Francisco decide cambios de alcance, puntos de prueba y hallazgos materiales. El coach prepara los prompts y comprueba los retornos accesibles; no registrar cada edición ni convertir cada incremento en una comprobación de conocimientos.

Adaptación explícita de `implement` 1.3.1:

1. Primer encargo: código y comprobaciones, dentro de los permisos otorgados. Devolver el diff y la evidencia antes de stage/commit o de una revisión que solo compare commits.
2. El coach comprueba el retorno y propone los commits exactos: alcance, diff candidato, mensaje y base. Tras autorización, un encargo de continuación realiza stage, comprueba el diff staged contra lo aprobado y crea el commit. Si difiere, detiene el commit.
3. Con commits existentes y diff no vacío, continuar con `$mattpocock-skills:code-review`, indicando la base fija y los requisitos acordados en la especificación, el ticket o, para implementación directa, la conversación de diseño. Verificar ambos ejes, Standards y Spec, y las instrucciones de los repositorios. El prompt limita la revisión a solo lectura; sus subagentes heredan esos límites.
4. Francisco decide los hallazgos materiales con evidencia. Correcciones autorizadas vuelven al ciclo de implementación; su commit y revisión deben cubrir el contenido final. No atribuir al working tree una revisión de un HEAD anterior.

El coach verifica criterios, comandos, SHA e informe de revisión sobre el contenido final. Puede aceptar evidencia válida sin repetir suites por rutina.

## Actualización de TASK.md

- Estado, inicio y fin de la fase, con la unidad correspondiente; encargo y sesión.
- Al confirmar el inicio real de ejecución de un ticket, actualizar su fila a `IN_PROGRESS` y registrar `Inicio`. Crear el archivo o entregar el prompt no inicia el ticket.
- Referencias a commits, comprobaciones y revisión final, con resultados breves. Mantener código, diffs y logs extensos en sus fuentes.
- Preguntas pendientes y siguiente corrección, comprobación o decisión. Una duda detiene solo las acciones que requieren su respuesta.
- Mantener el ticket abierto al completar implementación; su fin depende de los criterios y la integración acordada.

**DONE:** cambio implementado, commits autorizados y revisados, comprobaciones pertinentes acreditadas y revisión del contenido final completada, sin correcciones materiales pendientes. Una operación necesaria sin autorización permanece pendiente. `DONE` aquí no significa que el ticket esté integrado.

**Siguiente:** `validate` para esa unidad, conservando la sesión útil.
