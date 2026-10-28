# POEX Coach

POEX Coach es un sistema personal de acompañamiento profesional. Se creó para mejorar mis resultados, recuperar mi fiabilidad ante el equipo y reducir un riesgo real de despido.

Combina archivos duraderos con un agente de IA para ayudarme a comprender, ejecutar, revisar y comunicar mi trabajo sin depender de la memoria ni delegar mi criterio.

El sistema se organiza alrededor de dos flujos principales:

1. realizar tareas de desarrollo;
2. revisar trabajo ajeno.

POEX Coach actúa como coach, ayudante y compañero de trabajo. Me aporta estructura, seguimiento, análisis y evidencia, pero no sustituye mi comprensión, mis decisiones ni mi responsabilidad profesional.

## Problema que resuelve

El proyecto nace de problemas repetidos de fiabilidad profesional que el esfuerzo y la memoria por sí solos no han corregido:

- comenzar a implementar antes de comprender completamente una tarea;
- estimar antes de investigar alcance, dependencias y pruebas;
- delegar demasiado criterio en la IA y no poder defender el resultado;
- revisar cambios grandes de forma superficial;
- validar sólo los caminos más evidentes;
- olvidar mensajes, decisiones, revisiones o compromisos;
- comunicar tarde dudas, bloqueos o cambios de alcance;
- considerar terminado un trabajo sin evidencia suficiente.

POEX Coach externaliza el proceso, el estado y los compromisos. Su objetivo no es añadir burocracia, sino hacer el trabajo más comprensible, verificable, previsible y fácil de reanudar.

## Cómo funciona

POEX Coach utiliza archivos Markdown pequeños y duraderos como memoria compartida entre sesiones. El agente parte de las reglas generales, localiza el expediente indicado y carga únicamente la fase y el contexto necesarios para la acción actual.

El proyecto se compone de:

- `AGENTS.md`: núcleo operativo, autorizaciones, fuentes de verdad, continuidad y acceso a repositorios.
- `COACHING.md`: contrato de acompañamiento, foco, cuestionamiento, comunicación y adaptación personal.
- `.agents/skills/poex-task/SKILL.md`: entrada al flujo para realizar tareas de desarrollo. Detecta una tarea nueva o un expediente existente, reanuda su estado y dirige una sola acción o decisión por turno.
- `.agents/skills/poex-task/references/`: fases y reglas especializadas que se cargan sólo cuando corresponden.
- `.scratch/<slug>/TASK.md`: expediente local de cada tarea. Conserva su estado, decisiones, evidencia, bloqueos, compromisos y siguiente acción.

Este diseño permite cambiar de sesión o agente sin depender del historial del chat y sin cargar toda la documentación en cada conversación.

## Principios de diseño

- **Control humano:** la IA ayuda a investigar, ordenar, cuestionar y evaluar; Francisco conserva la comprensión y las decisiones.
- **Evidencia antes que promesas:** el progreso se demuestra mediante resultados observables y fuentes trazables.
- **Contexto progresivo:** cada sesión carga sólo la información que necesita para el paso actual.
- **Una fuente para cada significado:** las reglas, el estado y la documentación tienen propietarios distintos para evitar contradicciones.
- **Garantía proporcional:** `assurance_level` adapta el análisis, la validación y la evidencia al riesgo y la complejidad sin estimar el esfuerzo.
- **Evolución basada en uso real:** sólo se añaden archivos, reglas o automatizaciones cuando resuelven una necesidad observada.

## Uso

No hay que instalar dependencias ni ejecutar una aplicación. El proyecto se usa desde una sesión de agente abierta en la raíz de POEX Coach.

### Iniciar una tarea

1. Abre la sesión en este directorio.
2. Proporciona la referencia de la tarea y pide comenzar, por ejemplo: `Quiero trabajar en POE-1234`.
3. El agente activará la skill `poex-task`, consultará las fuentes disponibles y empezará en la fase 1.
4. Si necesita crear `.scratch/poe-1234/TASK.md`, lo hará automáticamente, verificará el resultado e informará después de forma compacta.

La skill también puede invocarse de forma explícita: `Usa $poex-task para iniciar POE-1234`.

### Reanudar una tarea

Pide `Continúa POE-1234`. El agente buscará el expediente correspondiente en `.scratch/` y mostrará de forma compacta:

- tarea seleccionada;
- estado registrado y evaluación actual;
- fase y paso pendientes;
- siguiente acción concreta.

Si no indicas una clave y existe un único expediente abierto, el agente lo reanudará. Si existen varios, mostrará su clave, estado, fase y siguiente acción para que elijas cuál continuar. Puede haber varias tareas `IN_PROGRESS`.

### Trabajar con el flujo

El flujo de realización contiene 10 fases, desde la comprensión y definición de la tarea hasta el cierre y aprendizaje. Durante el trabajo:

1. El agente carga sólo la fase actual y las referencias condicionales necesarias.
2. Propone una sola acción, pregunta o decisión verificable.
3. Francisco ejecuta o autoriza la acción y aporta la evidencia necesaria.
4. El agente actualiza el estado usando `PENDING`, `IN_PROGRESS`, `WAITING`, `BLOCKED`, `PAUSED` o `DONE`.
5. El agente actualiza automáticamente el expediente, verifica la escritura e informa después de forma compacta.
6. Sólo avanza de fase cuando todos sus criterios están superados y el estado evaluado ha quedado registrado.

Tareas, fases y pasos comparten el mismo vocabulario de estado. Una fase sólo avanza desde `DONE`. El estado local no cambia el estado oficial de Jira.

El expediente registra el inicio y fin de la tarea, de cada fase y de cada paso o tarea verificable. También conserva el progreso de cada fase y las reaperturas sin sobrescribir su historia.

### Autorizaciones y sistemas externos

POEX Coach trabaja en modo de solo lectura por defecto. Consultar fuentes no autoriza a modificarlas.

- Todo cambio dentro de POEX Coach se presenta primero y requiere aprobación, excepto la creación y actualización automática de `.scratch/*/TASK.md`.
- Jira permanece en modo de solo lectura; el agente prepara las actualizaciones para que Francisco las aplique manualmente.
- Modificar repositorios de trabajo, GitHub, Teams u otros sistemas requiere una instrucción explícita para esa acción concreta.

### Cerrar o cambiar de sesión

Indica que vas a detenerte o cambiar de agente. El cierre debe dejar registrados los resultados, decisiones, bloqueos, compromisos y la siguiente acción. Si continuarás en otra sesión, el agente también preparará un prompt de reanudación que apunte al expediente, sin duplicar todo su contenido.

Mientras no exista todavía un flujo aprobado para el tipo de trabajo solicitado, POEX Coach debe tratarlo como una capacidad en construcción.

## Estado actual

POEX Coach está en su primera versión.

La base operativa, el contrato de acompañamiento y el flujo para realizar tareas de desarrollo ya están definidos. El siguiente hito es validar el flujo mediante trabajo real y ajustar sólo aquello que demuestre fricción o falta de cobertura.

El flujo para revisar trabajo ajeno todavía no existe. Se diseñará después de validar el primero y aplicar sus aprendizajes.

Esta versión no es una aplicación y no utiliza base de datos, automatizaciones complejas ni integraciones permanentes. El formato Markdown es intencional: permite comprobar el proceso antes de invertir en infraestructura.

## Evolución prevista

Después de validar los dos flujos principales, POEX Coach podrá incorporar:

- agenda diaria asistida y seguimiento de compromisos;
- inicio y cierre guiados de la jornada;
- integración de lectura con Jira, GitHub y, si resulta viable, Teams;
- actualización asistida del estado de las tareas;
- recordatorios y seguimiento de bloqueos;
- informes de progreso para el tech lead;
- técnicas de motivación o gamificación que hayan demostrado utilidad;
- skills para procedimientos estables y repetidos.

Esta lista expresa posibilidades, no compromisos. Cada ampliación deberá responder a un problema observado y aportar más valor que complejidad.

## Privacidad y seguridad

POEX Coach es un proyecto personal y permanece separado de los repositorios compartidos de la empresa.

Sólo conserva el contexto necesario para acompañar el trabajo. No debe almacenar credenciales, secretos, datos de clientes ni copias completas de información oficial que pueda quedar desactualizada.

Los archivos deben enlazar Jira, GitHub o Teams cuando el enlace sea suficiente. El proyecto no se publicará ni sincronizará con servicios remotos sin una decisión explícita de Francisco.

Las reglas operativas y de autorización detalladas están en `AGENTS.md`.

## Criterios de éxito

La primera etapa se considerará validada cuando:

- `POE-8958` haya recorrido el flujo de realización de tareas hasta su cierre;
- cada paso completado tenga resultado y evidencia;
- una sesión nueva pueda reconstruir correctamente el estado;
- las dudas, bloqueos y compromisos sobrevivan a los cambios de contexto;
- el proceso evite avanzar sin la comprensión y validación necesarias;
- pueda identificarse qué aportó valor, qué causó fricción y qué debe eliminarse;
- los cambios del sistema respondan a problemas observados durante el trabajo real;
- el flujo resultante pueda aplicarse a la siguiente tarea.

El éxito no se mide por la cantidad de archivos, reglas o automatizaciones. Se mide por una ejecución más comprensible, fiable, verificable y fácil de reanudar.
