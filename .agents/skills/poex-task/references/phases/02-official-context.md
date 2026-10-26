# Fase 2. Reconstrucción del contexto oficial

**Objetivo:** reunir el contexto necesario sin depender de la memoria ni de conclusiones de la IA.

**Entrada:** fase 1 superada y acceso autorizado de solo lectura.

**Acciones:**

1. Leer Jira, incluidos descripción, criterios, estado, comentarios, enlaces y dependencias.
2. Separar requisitos vigentes de requisitos sustituidos o limitados.
3. Consultar las fuentes relacionadas que puedan cambiar la comprensión: documentación, tareas, conversaciones, reuniones, PR, commits, incidencias o comportamiento documentado.
4. Identificar origen, motivo, actores, resultado de negocio, antecedentes, restricciones, compatibilidad, migraciones, feature flags, consumidores y orden de despliegue.
5. Separar hechos, observaciones, hipótesis, preguntas y contradicciones.
6. Enlazar cada hecho material con su fuente y comprobar su vigencia.
7. No resolver contradicciones silenciosamente.
8. Preparar un resumen limitado al contexto necesario.
9. Distinguir qué hechos debe investigar el agente y qué explicaciones o decisiones corresponden a Francisco.

**Resultado:** mapa trazable del contexto oficial y de sus incógnitas.

**Evidencia:** fuentes consultadas, requisitos sustituidos, contradicciones y resumen registrado.

**Puerta de salida:**

- `SUPERADO`: las fuentes relevantes están consultadas y el contexto material tiene respaldo.
- `REVISAR`: falta una fuente accesible o una afirmación importante carece de evidencia.
- `BLOQUEADO`: una fuente o contradicción impide reconstruir el contexto.

**Siguiente paso:** fase 3.

