# Encargos, sesiones y retorno

## Preparar el encargo

1. Verifica la entrada de la fase y lee la skill instalada, incluida su política de invocación. Conserva el identificador completo `$mattpocock-skills:<nombre>`.
2. Delimita una unidad verificable: objetivo, entradas, resultados, permisos y punto de parada. Las decisiones materiales no resueltas impiden encargar acciones que dependan de ellas.
3. Verifica los [workspaces](workspaces.md) implicados y la vigencia de las entradas. Registra rutas absolutas, ramas y SHA; para documentos locales, una huella SHA-256 permite detectar cambios sin copiar su contenido.
4. Prepara un prompt usando [la plantilla](../assets/assignment.template.md). Sustituye todos sus marcadores por datos comprobados. Incluye la invocación explícita de la skill, el directorio de apertura y si debe usarse una sesión nueva o una anterior identificada.
5. Registra `active_assignment` según [trazabilidad](traceability.md), inicialmente `PENDING`, y el prompt exacto en `## Encargo actual`. Una autorización anterior solo se incorpora con su alcance y procedencia; un permiso pendiente se presenta como pendiente, nunca como concedido.
6. Entrega una única acción: pegar el prompt en la sesión indicada. No abras chats ni envíes mensajes entre ellos automáticamente.

No existe un ejecutor automático de skills. Francisco activa la skill al enviar el prompt. El coach no modifica ni copia el plugin para eludir su política de invocación.

## Elegir sesión

- Conserva investigación, decisiones, especificación y tickets en la misma sesión ejecutora mientras siga siendo útil y tenga capacidad. Tras diseño, Francisco confirma su finalización y elige la ruta según [la fase de diseño](phases/03-design.md); el coach verifica los artefactos accesibles de las fases posteriores. Leer el código y los documentos actualizados sigue siendo obligatorio.
- Para implementación directa desde diseño, conserva esa misma sesión y su contexto. Indica expresamente esta continuidad en el siguiente prompt.
- Comienza cada ticket de implementación en una sesión nueva, con entradas autosuficientes. Mantén sus correcciones en esa sesión si conserva el contexto útil.
- Ejecuta la retrospectiva en la sesión que evalúa, antes de descartarla; si ya no está disponible, usa sus fuentes primarias accesibles y declara las carencias.
- Usa handoff cuando el trabajo viaje a otro directorio, agente o herramienta. Referencia los artefactos duraderos; el archivo temporal no es su sustituto.
- Si debes cambiar de contexto antes de terminar la planificación, conserva razones, decisiones y fuentes. No ordenes vaciar el contexto solo porque haya terminado una skill.

## Durante la ejecución

La sesión ejecutora lee el encargo registrado y verifica que el identificador, objetivo y entradas coinciden con el prompt. Un encargo sustituido o unas entradas materialmente distintas requieren volver al coach antes de escribir.

El ejecutor verifica directorios e instrucciones aplicables y trabaja solo sobre el alcance autorizado. Usa `TASK.md` en solo lectura. Una discrepancia de identidad, decisión material nueva, cambio de alcance o permiso insuficiente detiene la acción dependiente y produce un retorno con la pregunta concreta. Las preguntas abiertas se comunican para mantener la lista común; no bloquean por sí solas el resto del encargo. Puede terminar comprobaciones independientes dentro del encargo.

Para aprobar un archivo del coach, Francisco debe ver primero su contenido exacto. Una invocación de skill no concede permiso para escribirlo, hacer commit o publicar. Si la skill requiere una acción no autorizada, el ejecutor prepara el resultado revisable y devuelve esa acción pendiente. No declara completada la skill entera.

Cuando Francisco confirme que ha iniciado la ejecución, el coach registra el encargo `IN_PROGRESS` y la fase `WAITING`: responsable Francisco/sesión ejecutora; condición de reanudación, aviso de retorno con evidencia. Preparar un prompt no demuestra que se haya ejecutado. Durante la espera, el coach no modifica las entradas ni los workspaces comprometidos. Cambiar el encargo requiere detener o cerrar el anterior y asignar otro identificador.

## Retorno obligatorio

Para `design`, usa el feedback de Francisco definido en [la fase de diseño](phases/03-design.md); no exijas el informe técnico siguiente para sustituir una conversación a la que el coach no tiene acceso. Esta excepción no acredita escrituras ni otros efectos no comprobados.

El ejecutor entrega en el chat:

- identificador y objetivo del encargo;
- resultado por criterio, distinguiendo comprobado, pendiente e hipótesis;
- repositorio, ruta, rama y SHA inicial/final; cambios sin commit conocidos;
- archivos o artefactos producidos, con rutas y huellas o referencias verificables;
- comandos, directorio, resultado y evidencia de validación; diferencia respecto a la línea base;
- decisiones confirmadas por Francisco durante la ejecución, con sus razones y alcance;
- bloqueos, permisos pendientes y acción propuesta.

Los informes extensos se guardan únicamente en un destino autorizado. Si todo está en el chat, Francisco aporta el retorno al coach. Este no presupone acceso a otros chats; pide el informe solo si las fuentes accesibles no bastan.

## Comprobación del coach

En `design`, aplica el contrato de feedback de su fase y registra a Francisco como fuente de la confirmación. Para los demás encargos, sigue estas comprobaciones:

1. Al recibir el aviso, vuelve a `IN_PROGRESS` para verificar. Mantén el encargo abierto hasta contrastar el retorno; no liberes su workspace antes de que el ejecutor haya terminado de escribir.
2. Compara identificador, entradas y workspaces con el encargo. Un resultado de otra revisión o de otro ticket no satisface este encargo.
3. Inspecciona artefactos, diff, pruebas y fuentes oficiales según el resultado. Vincula la evidencia de ejecución al código y entorno observados. Repite comprobaciones cuando falte evidencia, haya cambiado el código o exista una duda material; no repitas suites ya acreditadas por rutina.
4. Confirma con Francisco cualquier decisión material del informe que no tenga respaldo verificable. Usa la revisión y las decisiones previstas en la fase como punto de control, sin añadir un examen de conocimientos.
5. Si falta un criterio, conserva la fase `IN_PROGRESS` y prepara una continuación acotada. Si depende de otra persona o de un permiso, usa el estado aplicable con responsable y condición. Archiva el encargo anterior con su resultado real y enlaza el nuevo; no conviertas una ejecución incompleta en `DONE`.
6. Si cumple todos sus criterios, registra el encargo `DONE`. Evalúa después la puerta de la fase: un encargo puede terminar sin completar todos sus pasos.
7. Conserva en `## Resultados y evidencia` el identificador, resultado, fuentes, decisiones y limitaciones. Archiva allí los encargos sustituidos y sus motivos. Retira `## Encargo actual` y deja `active_assignment: null` cuando no quede ejecución abierta.
8. Actualiza y verifica `TASK.md`; entrega la siguiente acción o el siguiente prompt.
