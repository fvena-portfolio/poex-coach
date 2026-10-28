# Fase 1. Comprender la tarea

**Objetivo:** ayudar a Francisco a entender la tarea, revisar su definición, resolver dudas y distinguir lo que está claro de lo que queda abierto. La preparación del espacio de trabajo corresponde a `initialize`.

**Entrada:** referencia explícita a una tarea oficial existente, legible y no cerrada ni cancelada; acceso autorizado de solo lectura a Jira y a los repositorios.

## Transición entre pasos

Al terminar un paso, presenta su resultado y la siguiente acción. Francisco puede plantear dudas antes de continuar. Su decisión de continuar no sustituye el criterio de finalización: registra `DONE` únicamente cuando el resultado del paso existe y está comprobado.

Al iniciar un paso, actualiza `current_step` con su key y actualiza `updated_at`. No registres el paso en `## Progreso`.

Francisco puede plantear una duda en cuanto aparezca. Responderla no requiere crear un paso nuevo. Si puede resolverse mediante las fuentes autorizadas ya disponibles o una consulta puntual, el agente la responde de inmediato. En caso contrario, la registra automáticamente y la conduce al paso 4 o a la fase correspondiente.

No volver a formular una duda ya respondida o registrada.

Si Francisco detiene el trabajo, `current_step` conserva el paso que debe reanudarse. Usa `PAUSED` únicamente cuando Francisco suspenda conscientemente la tarea.

## Paso 1. Contexto inicial

**Key:** `context`

1. Leer la tarea, sus comentarios y sus relaciones directas. Solicitar explícitamente el campo estándar `components`. Si la respuesta omite el campo, volver a consultarlo antes de evaluar el paso.
2. Buscar en Jira tareas potencialmente relacionadas aunque no estén enlazadas, mediante consultas acotadas por título, conceptos y componentes. Incluir únicamente los resultados que puedan cambiar la comprensión de la tarea y explicar la relación.
3. Limitar la consulta inicial de GitHub a:
   - PR, commits o ramas enlazados desde Jira;
   - coincidencias de la clave exacta de Jira en PR, commits o ramas;
   - trabajo anterior sobre exactamente el mismo cambio.
4. Reservar las búsquedas amplias de código, arquitectura o implementaciones similares para la orientación técnica y diseño (`design`).
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
   - reservar la detección y corrección de componentes ausentes para el paso 6.
9. Actualizar `components` en el YAML con la lista exacta devuelta por Jira. Usar `[]` cuando Jira devuelva una lista vacía.
10. Separar los hechos obtenidos de Jira de las limitaciones de consulta y los bloqueos. No incluir inferencias técnicas en el contexto inicial.
11. Completar el paso cuando los datos requeridos estén obtenidos de sus fuentes, el campo `components` se haya consultado explícitamente, el YAML refleje su valor oficial y cualquier carencia de consulta esté identificada.

## Paso 2. Traducción fiel

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

## Paso 3. Orientación técnica inicial

**Key:** `orientation`

1. Tomar como límites provisionales los componentes identificados y los requisitos técnicos expresamente incluidos en la tarea.
2. Consultar código solo cuando sea necesario para comprender la tarea. Leer las instrucciones aplicables y comprobar rama, SHA y cambios locales de la referencia consultada, en solo lectura. Declarar sus limitaciones y revalidar las conclusiones materiales en el workspace definitivo. Preparar ramas o worktrees corresponde a `initialize`. Limitar la consulta a:
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
7. Reservar para diseño (`design`):
   - el análisis exhaustivo de capas y responsabilidades;
   - la comparación detallada de contratos;
   - autorización, persistencia, transacciones y procesos asíncronos;
   - el análisis completo de pruebas;
   - la reproducción del comportamiento;
   - riesgos, alternativas y decisiones de diseño.
8. Registrar como pendiente cualquier incógnita que no sea imprescindible para comprender la tarea. No completar su contenido mediante suposiciones.
9. Completar el paso cuando Francisco pueda distinguir, a alto nivel, el comportamiento actual del cambio solicitado y entienda los requisitos técnicos incluidos en Jira.

## Paso 4. Resolución y registro de dudas

**Key:** `questions`

1. Recuperar las dudas surgidas durante el contexto, la traducción y la orientación técnica, y preguntar a Francisco si existe alguna más.
2. Cuando sea útil, sugerir un máximo de tres posibles dudas deducidas del contenido.
3. Tratar una sola duda cada vez.
4. Clasificar cada duda:
   - resoluble mediante fuentes autorizadas;
   - investigable durante diseño (`design`);
   - dependiente de una decisión o aclaración externa;
   - no relevante para el resultado de la tarea.
5. Para una duda resoluble, realizar únicamente la consulta necesaria, responder con información trazable y distinguir los hechos de la explicación.
6. Explicar los conceptos financieros desde sus fundamentos. Para backend o QA, utilizar primero un símil general y, cuando sea posible, un equivalente en JavaScript.
7. Registrar en `## Preguntas pendientes` toda duda que deba recuperarse después, tanto técnica como externa, con la pregunta exacta, contexto mínimo y destinatario o fase prevista si se conocen.
8. Si la duda requiere al product owner, registrar como propietario a la persona identificada en la tarea. No enviar la pregunta sin autorización.
9. Las dudas pendientes no cambian por sí solas el estado de la tarea durante la comprensión inicial. Registrarlas y continuar el recorrido para permitir que aparezcan nuevas dudas antes de recopilarlas en diseño (`design`).
10. Después de cada respuesta, preguntar si queda alguna duda.
11. Completar el paso cuando cada duda esté respondida o registrada para retomarla, sin inventar destinatarios ni respuestas. No es necesario resolver las preguntas destinadas a diseño (`design`).
12. Las dudas ya tratadas se incorporan a la síntesis solo cuando formen parte de los puntos clave.

## Paso 5. Síntesis de puntos clave

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
7. Si Francisco los tiene claros, continuar; esta confirmación se comprueba en la conversación y no se guarda como evaluación personal.
8. Si quiere profundizar, explicar un solo punto cada vez y volver a preguntar si necesita aclarar otro.
9. Cuando un punto no pueda resolverse mediante fuentes autorizadas, registrarlo como duda para recopilarlo en diseño (`design`). No cambiar por ello el estado de la tarea.
10. Completar el paso cuando Francisco confirme que los puntos están claros o haya identificado qué aspectos quiere profundizar y estos estén explicados o registrados.
11. Conservar en `TASK.md` únicamente las preguntas pendientes que afecten a la continuación, tanto técnicas como externas. No conservar la confirmación, una transcripción, puntuación ni resultado de examen.

## Paso 6. Recomendaciones para la definición de Jira

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
   - registrar la duda en `## Preguntas pendientes` para evitar que se pierda o se repita en diseño (`design`).
5. No revisar ni solicitar story points en esta fase.
6. Para evaluar una convención dudosa, consultar únicamente las tareas comparables mínimas necesarias.
7. Presentar las recomendaciones como una lista informativa. No usar casillas ni pedir que se marquen, apliquen o validen.
8. Si no existe ninguna recomendación material, indicarlo expresamente.
9. El agente no modifica Jira. Cualquier comentario o cambio propuesto queda sujeto a una instrucción explícita de Francisco.
10. Completar el paso cuando la lista de recomendaciones y los comentarios propuestos estén presentados y las dudas materiales estén registradas. Las recomendaciones pendientes no impiden continuar.

## Actualización de TASK.md

- Al crear el expediente, registrar identidad oficial, objetivo breve, estado y fechas. Mantener `components` con los valores oficiales consultados; una corrección propuesta no cambia ese campo.
- Actualizar `current_step`, el estado y las fechas de la fase. Los pasos no crean filas en `## Progreso`.
- Conservar solo las preguntas abiertas necesarias para reanudar o trasladar a otra fase. Retirarlas al resolverse.
- Presentar contexto, traducción, orientación, síntesis y recomendaciones en la conversación. No crear un informe de comprensión ni copiar esos contenidos al expediente.

**DONE:** contexto, cambio solicitado y puntos clave revisados; dudas respondidas o identificadas para retomarlas; recomendaciones sobre la definición presentadas. Completar esta fase no certifica que todas las ambigüedades estén resueltas.

Las dudas abiertas no provocan por sí solas `WAITING` ni `BLOCKED` ni impiden inicializar. Si falta un acceso o dato necesario para realizar una acción concreta, registrar el impedimento de esa acción, sin inventar la información.

Una subtarea vacía de seguimiento no aparece en el contexto, pero cuenta al revisar la cobertura de componentes.

**Siguiente:** `initialize`.
