# Fase 1. Comprensión y definición de la tarea

**Objetivo:** proteger el trabajo existente, partir de repositorios actualizados, situar a Francisco sobre la tarea, resaltar los puntos clave para que valore qué entiende y qué necesita aclarar, identificar posibles mejoras en la definición de Jira y preparar las ramas de trabajo antes de investigar el sistema en profundidad o diseñar una solución.

**Entrada:** referencia explícita a una tarea oficial existente, legible y no cerrada ni cancelada; acceso autorizado de solo lectura a Jira y a los repositorios.

## Transición entre pasos

Al terminar un paso, presenta su resultado y la siguiente acción. Francisco puede plantear dudas antes de continuar. Su decisión de continuar no sustituye el criterio de finalización: registra `DONE` únicamente cuando el resultado del paso existe y está comprobado.

Al iniciar un paso, actualiza `current_step` con su key y actualiza `updated_at`. No registres el paso en `## Progreso`.

Francisco puede plantear una duda en cuanto aparezca. Responderla no requiere crear un paso nuevo. Si puede resolverse mediante las fuentes autorizadas ya disponibles o una consulta puntual, el agente la responde de inmediato. En caso contrario, la registra automáticamente y la conduce al paso 5 o a la fase correspondiente.

No volver a formular una duda ya respondida o registrada.

Si Francisco detiene el trabajo, `current_step` conserva el paso que debe reanudarse. Usa `PAUSED` únicamente cuando Francisco suspenda conscientemente la tarea.

## Paso 1. Salvaguarda y actualización inicial de repositorios

**Key:** `repositories`

1. Leer `AGENTS.md` y las reglas SCM aplicables de backend, frontend, QA y web.
2. Pedir a Francisco que prepare manualmente esos cuatro repositorios:
   - proteger cualquier trabajo pendiente;
   - cambiar a `develop`, salvo que la tarea requiera una base alternativa;
   - actualizar la rama mediante el mecanismo seguro definido por el repositorio;
   - confirmar cuando haya terminado.
3. Tratar `poex-infra` únicamente como referencia de solo lectura. No cambiar su rama, actualizarlo ni modificarlo.
4. Mientras Francisco prepara los repositorios, puede leerse Jira y prepararse el contexto del paso 2. No presentar ese contexto ni iniciar formalmente el paso 2 hasta completar este paso.
5. Después de la confirmación, verificar en cada repositorio mutable:
   - rama y `HEAD`;
   - upstream y divergencia;
   - working tree, índice y archivos sin seguimiento;
   - commits locales;
   - operaciones Git incompletas.
6. Si aparece un problema:
   - mostrar el repositorio, el estado exacto y el riesgo;
   - pedir a Francisco que lo resuelva;
   - mantener el paso en `WAITING` hasta que confirme la resolución;
   - volver a verificar antes de continuar.
7. Aceptar una base alternativa, como `hotfix/x.y.z`, únicamente mediante una decisión explícita de Francisco y después de comprobar que está limpia y actualizada.
8. Una decisión de continuar con una base alternativa no autoriza a mezclar cambios locales o trabajo de otra tarea.
9. Completar el paso cuando los cuatro repositorios mutables estén en `develop` o en la base alternativa confirmada, estén actualizados y no contengan trabajo pendiente ni operaciones ambiguas.

## Paso 2. Contexto inicial

**Key:** `context`

1. Leer la tarea, sus comentarios y sus relaciones directas. Solicitar explícitamente el campo estándar `components`. Si la respuesta omite el campo, volver a consultarlo antes de evaluar el paso.
2. Buscar en Jira tareas potencialmente relacionadas aunque no estén enlazadas, mediante consultas acotadas por título, conceptos y componentes. Incluir únicamente los resultados que puedan cambiar la comprensión de la tarea y explicar la relación.
3. Limitar la consulta inicial de GitHub a:
   - PR, commits o ramas enlazados desde Jira;
   - coincidencias de la clave exacta de Jira en PR, commits o ramas;
   - trabajo anterior sobre exactamente el mismo cambio.
4. Reservar las búsquedas amplias de código, arquitectura o implementaciones similares para la orientación técnica y la fase 2.
5. Si GitHub no está disponible o no devuelve resultados, registrarlo únicamente cuando pueda limitar la comprensión. No tratarlo como bloqueo por defecto.
6. Presentar un contexto breve usando estas etiquetas y una línea separada para cada dato:
   - **Tarea:** clave y título;
   - **Tipo:** tipo oficial;
   - **Estado:** estado oficial;
   - **Prioridad:** prioridad oficial;
   - **Solicitante:** nombre y fecha;
   - **Asignado:** responsable actual;
   - **Problema:** formulación breve respaldada por el contenido oficial;
   - **Objetivo:** resultado expresado en el contenido oficial;
   - **Componentes:** nombres exactos registrados en Jira;
   - **Tareas relacionadas:** relaciones directas y resultados materiales de la búsqueda acotada;
   - **Decisiones documentadas:** decisiones expresas conservadas en los comentarios;
   - **Bloqueos:** bloqueos registrados en las fuentes.
7. No incluir en el contexto las subtareas vacías creadas únicamente para representar frontend, backend, QA o infraestructura.
8. Copiar los componentes exactamente como los devuelve el campo `components`:
   - no traducir, normalizar, completar ni inferir componentes en este paso;
   - si Jira devuelve una lista vacía, dejar el valor de **Componentes** en blanco;
   - la omisión del campo en la respuesta no demuestra que la lista esté vacía;
   - reservar la detección y corrección de componentes ausentes para el paso 7.
9. Actualizar `components` en el YAML con la lista exacta devuelta por Jira. Usar `[]` cuando Jira devuelva una lista vacía.
10. Separar los hechos obtenidos de Jira de las limitaciones de consulta y los bloqueos. No incluir inferencias técnicas en el contexto inicial.
11. Completar el paso cuando los datos requeridos estén obtenidos de sus fuentes, el campo `components` se haya consultado explícitamente, el YAML refleje su valor oficial y cualquier carencia de consulta esté identificada.

## Paso 3. Traducción fiel

**Key:** `translation`

1. Traducir al español:
   - descripción;
   - criterios de aceptación;
   - requisitos técnicos incluidos en la tarea;
   - comentarios asociados, respetando su orden cronológico.
2. No traducir ni reproducir los checklists.
3. Conservar la estructura, el orden, la numeración, las negaciones, los nombres propios, los valores literales y los términos técnicos.
4. Mantener entre paréntesis el término original cuando una traducción pueda perder precisión.
5. No resumir, reinterpretar, corregir ni completar el contenido.
6. No convertir ambigüedades en requisitos ni resolver contradicciones silenciosamente.
7. Señalar separadamente cualquier fragmento que no pueda traducirse con seguridad.
8. Completar el paso cuando cada fragmento requerido esté traducido fielmente o identificado como una carencia o incertidumbre concreta.

## Paso 4. Orientación técnica inicial

**Key:** `orientation`

1. Tomar como límites provisionales los componentes identificados y los requisitos técnicos expresamente incluidos en la tarea.
2. Consultar únicamente el código y la documentación necesarios para identificar:
   - los repositorios y módulos directamente relacionados;
   - el punto de entrada principal;
   - el comportamiento actual visible;
   - los términos técnicos necesarios para interpretar la tarea.
3. Presentar una orientación breve con:
   - comportamiento actual;
   - ubicación general de ese comportamiento;
   - cambio solicitado respecto al estado actual;
   - términos técnicos aclarados;
   - dependencias o incógnitas evidentes.
4. Describir únicamente recorridos confirmados. Cuando ayude a la comprensión, utilizar un flujo breve desde la entrada hasta el resultado.
5. Distinguir hechos comprobados, observaciones e hipótesis. Referenciar la rama, el SHA y las ubicaciones del código utilizadas.
6. Detener la exploración cuando exista contexto suficiente para interpretar la tarea.
7. Reservar para la fase 2:
   - el análisis exhaustivo de capas y responsabilidades;
   - la comparación detallada de contratos;
   - autorización, persistencia, transacciones y procesos asíncronos;
   - el análisis completo de pruebas;
   - la reproducción del comportamiento;
   - riesgos, alternativas y decisiones de diseño.
8. Registrar como pendiente cualquier incógnita que no sea imprescindible para comprender la tarea. No completar su contenido mediante suposiciones.
9. Completar el paso cuando Francisco pueda distinguir, a alto nivel, el comportamiento actual del cambio solicitado y entienda los requisitos técnicos incluidos en Jira.

## Paso 5. Resolución y registro de dudas

**Key:** `questions`

1. Recuperar las dudas surgidas durante el contexto, la traducción y la orientación técnica, y preguntar a Francisco si existe alguna más.
2. Cuando sea útil, sugerir un máximo de tres posibles dudas deducidas del contenido.
3. Tratar una sola duda cada vez.
4. Clasificar cada duda:
   - resoluble mediante fuentes autorizadas;
   - investigable durante la fase 2;
   - dependiente de una decisión o aclaración externa;
   - no relevante para el resultado de la tarea.
5. Para una duda resoluble, realizar únicamente la consulta necesaria, responder con información trazable y distinguir los hechos de la explicación.
6. Explicar los conceptos financieros desde sus fundamentos. Para backend o QA, utilizar primero un símil general y, cuando sea posible, un equivalente en JavaScript.
7. Cuando no pueda resolverse y deba formularse a otra persona, registrarla en `## Preguntas pendientes` de `TASK.md` con la pregunta exacta y el propietario esperado.
8. Si la duda requiere al product owner, registrar como propietario a la persona identificada en la tarea. No enviar la pregunta sin autorización.
9. Las dudas pendientes no cambian por sí solas el estado de la tarea durante las fases 1 y 2. Registrarlas y continuar el recorrido para permitir que aparezcan nuevas dudas antes de recopilarlas en la fase 3.
10. Después de cada respuesta, preguntar si queda alguna duda.
11. Completar el paso cuando cada duda esté respondida o, si requiere una respuesta externa, registrada con su pregunta exacta y propietario esperado. No es necesario resolver las preguntas destinadas a la fase 3.
12. Las dudas ya tratadas se incorporan a la síntesis solo cuando formen parte de los puntos clave.

## Paso 6. Síntesis de puntos clave

**Key:** `summary`

1. Preparar el menor conjunto de puntos necesario para interpretar correctamente la tarea.
2. Incluir, cuando corresponda:
   - problema y actores afectados;
   - motivo y objetivo del cambio;
   - comportamiento esperado y diferencia respecto al comportamiento actual;
   - reglas de producto, límites y condiciones materiales;
   - decisiones ya documentadas;
   - preguntas abiertas registradas;
   - hallazgos de la orientación técnica que cambien o aclaren la interpretación de la tarea.
3. Agrupar los criterios y detalles relacionados. No reproducir todos los criterios de aceptación ni crear un punto por cada campo, validación o elemento de interfaz.
4. Distinguir claramente:
   - contenido oficial de Jira;
   - hechos técnicos comprobados;
   - preguntas todavía abiertas.
5. Presentar los puntos como una lista breve y explicativa. No convertirla en un cuestionario ni pedir a Francisco que repita información que acaba de leer.
6. Después de presentar la lista, hacer una única pregunta: «¿Tienes claros estos puntos o quieres que explique alguno?».
7. Si Francisco los tiene claros, registrar su confirmación y continuar.
8. Si quiere profundizar, explicar un solo punto cada vez y volver a preguntar si necesita aclarar otro.
9. Cuando un punto no pueda resolverse mediante fuentes autorizadas, registrarlo como duda para recopilarlo en la fase 3. No cambiar por ello el estado de la tarea.
10. Completar el paso cuando Francisco confirme que los puntos están claros o haya identificado qué aspectos quiere profundizar y estos estén explicados o registrados.
11. Conservar en `TASK.md` únicamente las preguntas que permanezcan pendientes de respuesta externa. No conservar la confirmación, una transcripción, puntuación ni resultado de examen.

## Paso 7. Recomendaciones para la definición de Jira

**Key:** `jira`

1. Revisar la definición vigente de la tarea utilizando la traducción, la orientación técnica, las dudas tratadas y la síntesis de puntos clave.
2. Preparar una lista breve de recomendaciones que puedan mejorar su definición o preparación. Considerar únicamente cuando corresponda:
   - componentes, subtareas y labels;
   - sprint y datos de clasificación;
   - criterios de aceptación incompletos, ambiguos o contradictorios;
   - checklist aplicable a la definición actual;
   - decisiones o aclaraciones que convenga conservar en Jira.
3. Para cada recomendación, indicar:
   - qué convendría cambiar o revisar;
   - la evidencia que la justifica;
   - la modificación concreta propuesta.
4. Cuando exista una duda que deba responderse en Jira:
   - incluir la recomendación de añadir un comentario;
   - agrupar preguntas relacionadas para reducir el número de comentarios;
   - proponer el comentario completo en inglés, listo para copiar y pegar;
   - conservar el contexto mínimo necesario y formular preguntas concretas;
   - registrar la duda en `## Preguntas pendientes` para evitar que se pierda o se repita en la fase 3.
5. No revisar ni solicitar story points en esta fase.
6. Para evaluar una convención dudosa, consultar únicamente las tareas comparables mínimas necesarias.
7. Presentar las recomendaciones como una lista informativa. No usar casillas ni pedir que se marquen, apliquen o validen.
8. Si no existe ninguna recomendación material, indicarlo expresamente.
9. El agente no modifica Jira. Cualquier comentario o cambio propuesto queda sujeto a una instrucción explícita de Francisco.
10. Completar el paso cuando la lista de recomendaciones y los comentarios propuestos estén presentados y las dudas materiales estén registradas. Las recomendaciones pendientes no impiden continuar.

## Paso 8. Preparación de las ramas de trabajo

**Key:** `branches`

1. Tomar de la orientación técnica y del paso 7 los componentes afectados identificados.
2. Preguntar expresamente a Francisco de qué rama debe salir el trabajo:
   - proponer `develop` como opción predeterminada;
   - no asumirla ni ejecutar cambios hasta recibir confirmación;
   - considerar que una tarea urgente puede salir de `main`, de una rama `hotfix/x.y.z` existente o de otra rama indicada por Francisco.
3. Revalidar en los repositorios afectados la rama, `HEAD`, upstream, divergencia, working tree, índice, archivos sin seguimiento, commits locales, operaciones incompletas y worktrees.
4. Mostrar el estado encontrado, la rama de salida confirmada y los comandos exactos propuestos. Obtener autorización explícita antes de actualizar, cambiar de rama, crear una rama o crear un worktree.
5. Si un repositorio contiene cambios o está ocupado por otra tarea:
   - detener las modificaciones sobre ese repositorio;
   - mostrar los cambios y el riesgo;
   - pedir a Francisco una decisión;
   - ofrecer conservar la situación, usar un worktree, hacer `stash` u otra acción indicada por Francisco;
   - no seleccionar ni ejecutar una opción automáticamente.
6. Asegurar que la rama de salida confirmada continúa actualizada. Usar un avance seguro y detenerse ante divergencias o conflictos.
7. Determinar el nombre de la rama de trabajo según las reglas específicas del repositorio. Como fallback:

   | Tipo de trabajo | Rama |
   |---|---|
   | Tarea o funcionalidad | `feature/POE-<n>-<titulo-jira-kebab>` |
   | Bug | `bugfix/POE-<n>-<titulo-jira-kebab>` |
   | Hotfix de producción | `hotfix/x.y.z` |
   | Release | `release/x.y.z` |

8. Antes de crear una rama:
   - comprobar si ya existe localmente o en remoto;
   - comprobar, si existe, su base y contenido;
   - no sobrescribirla ni reutilizarla sin confirmación;
   - confirmar que la rama de salida coincide con la indicada por Francisco.
9. Crear o reutilizar la rama únicamente en los repositorios correspondientes a los componentes afectados.
10. Cuando otra tarea necesite conservar su rama o directorio de trabajo, proponer un worktree para mantener ambas tareas aisladas.
11. Completar el paso cuando:
   - cada componente afectado tenga la rama correcta;
   - todas las ramas salgan de la base confirmada;
   - estén registradas las ramas y los SHA;
   - no quede ninguna operación Git pendiente o ambigua.
12. Crear o actualizar el expediente mediante el procedimiento de persistencia aplicable cuando la fase haya sido evaluada.

**Resultado:** trabajo previo protegido, repositorios actualizados, tarea situada, contenido oficial accesible en español, orientación técnica suficiente, dudas tratadas, puntos clave revisados, claridad confirmada, recomendaciones para mejorar la definición de Jira y ramas de trabajo creadas desde la base acordada.

**Evidencia:** estado Git inicial y posterior; autorización, ramas y SHA; tarea y comentarios oficiales; contexto y relaciones materiales; traducción fiel; referencias mínimas al código y documentación; orientación técnica; dudas relevantes; síntesis de puntos clave, confirmación de claridad y explicaciones relevantes; recomendaciones sobre la definición de Jira; comentarios en inglés propuestos cuando correspondan; dudas registradas y expediente actualizado y verificado.

**Puerta de salida:**

Las dudas registradas para recopilarlas en la fase 3 no provocan `WAITING` ni `BLOCKED`.

- `DONE`: el trabajo previo está protegido; los repositorios estaban disponibles y quedaron actualizados; la tarea está vigente; el contexto necesario está identificado; la traducción conserva el contenido oficial; la orientación técnica permite distinguir el estado actual del cambio solicitado; cada duda declarada está respondida o registrada para su recopilación posterior, y Francisco distingue el contenido oficial de las preguntas todavía abiertas; Francisco ha revisado los puntos clave y ha confirmado cuáles tiene claros y cuáles necesita profundizar; las recomendaciones sobre la definición de Jira están presentadas; las dudas materiales están registradas; y las ramas de trabajo parten de la base confirmada.
- `IN_PROGRESS`: falta completar una comprobación, actualización, traducción, orientación, explicación, recomendación sobre Jira o preparación de ramas.
- `WAITING`: se ha solicitado una aclaración o actuación externa y están identificados el responsable y la condición de reanudación.
- `BLOCKED`: falta una decisión, acceso o información imprescindible, existe trabajo previo sin una decisión segura, o una contradicción, divergencia Git o aclaración no formulada impide continuar.

Una subtarea vacía de seguimiento no debe aparecer en el contexto, pero sí cuenta para comprobar la cobertura de componentes.

**Siguiente paso:** fase 2.
