# Desviaciones, retornos y bloqueos

## Regla de retorno

Cuando aparece información nueva:

1. identificar qué resultado previo queda cuestionado;
2. volver a la primera fase afectada;
3. conservar la evidencia todavía válida;
4. marcar como `REVISAR` los resultados afectados;
5. proponer la siguiente comprobación;
6. actualizar `TASK.md` únicamente con aprobación.

No es necesario reiniciar toda la tarea.

## Requisito ambiguo o contradictorio

No se implementa una interpretación elegida por el agente. Se registran fuentes y consecuencias y se prepara una pregunta para el propietario. La tarea permanece en `REVISAR` o `BLOQUEADO`.

## Cambio de alcance

Si cambia el resultado, criterio, repositorio, riesgo, estimación u orden, Francisco decide si se incorpora, se convierte en otro ticket, se conserva como pendiente o requiere una tarea oficial. Los artefactos afectados vuelven a `REVISAR`.

## Estimación inválida

Se detiene el siguiente incremento, se muestra la nueva evidencia, se prepara la actualización manual de Jira y se revalida el plan.

## Cambios locales preexistentes

No se descartan, ocultan, mezclan ni modifican. Si no pueden aislarse con seguridad, la tarea queda `BLOQUEADO`.

## Fallos y evidencia incompleta

Una prueba fallida, comprobación omitida o resultado no reproducible deja la puerta en `REVISAR`. Se distingue entre defecto nuevo, fallo previo, entorno, prueba inestable, dependencia externa y ausencia de evidencia. Para diagnósticos difíciles se utiliza `$mattpocock-skills:diagnosing-bugs`.

## Imposibilidad de reproducir

Se registra entorno, entrada y resultado, se compara con la fuente y se solicita solo la evidencia faltante. No se implementa una corrección especulativa.

## Bloqueo sin información nueva

Después de aproximadamente treinta minutos de trabajo productivo sin evidencia nueva ni acción segura:

1. detener la repetición;
2. resumir lo comprobado;
3. registrar las hipótesis abiertas;
4. preparar una petición concreta de ayuda;
5. registrar responsable y condición de reanudación.

El agente no envía la petición sin autorización.

## Tarea más simple de lo previsto

Puede proponerse reducir el nivel cuando la evidencia elimina riesgos. Se explica qué profundidad deja de aportar valor y Francisco confirma la reducción. Las puertas esenciales permanecen.

## Urgencia y presión

El coordinador muestra el criterio pendiente, riesgo, comprobación mínima y consecuencia de omitirla. Un aplazamiento registra riesgo aceptado, propietario y seguimiento.

## Aparcar o cambiar el foco

Se detiene el trabajo en un punto seguro y se registra estado, cambios, dependencia, condición de reanudación y siguiente acción. La urgencia no elimina las puertas mínimas.

## Dependencia externa

Se registra qué se espera, quién puede resolverlo, qué evidencia permitirá continuar, seguimiento y trabajo independiente seguro. Puede cambiarse el foco, pero no superar la puerta dependiente.

## Subagentes durante la validación

Los subagentes no son obligatorios ni están prohibidos de forma permanente.

Durante la primera validación con `POE-8958`:

- solo se utilizan cuando Francisco lo solicite o una skill aplicable lo exija;
- se limitan a investigaciones acotadas, preferentemente de solo lectura;
- no sustituyen la comprensión, decisiones o validación de Francisco;
- no deciden alcance, arquitectura, prioridad o aceptación;
- no amplían permisos ni realizan acciones externas no autorizadas;
- el agente principal integra y valida sus resultados.

Cuando una actividad pueda haberse beneficiado de un subagente, se registra únicamente qué se habría delegado, qué habría mejorado y qué riesgo o coste habría introducido.

No se crea una fase, métrica o automatización específica. La política se revisará después de validar el flujo mediante evidencia real.

