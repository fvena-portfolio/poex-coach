# Fase 3. Preguntas, alineación y decisiones

**Objetivo:** resolver las preguntas materiales que no pueden cerrarse mediante fuentes, código o pruebas.

**Entrada:** modelo actual, riesgos y preguntas pendientes.

**Acciones:**

1. Recuperar de `## Preguntas pendientes` todas las preguntas registradas. No volver a preguntar las que ya estén respondidas.
2. Deduplicarlas, conservar su contexto y agruparlas por propietario.
3. Investigar primero los hechos que todavía puedan resolverse sin intervención externa.
4. Preparar una única consulta compacta para cada propietario con las preguntas que sigan abiertas.
5. Clasificar cada cuestión como hecho investigable, contradicción, decisión de producto, decisión técnica, dependencia, supuesto aceptable o asunto no relevante.
6. Para cada decisión material, presentar hechos, incertidumbre, opciones, trade-offs, recomendación, propietario, reversibilidad, impacto y evidencia necesaria.
7. Elegir el mecanismo proporcional:
   - pregunta breve;
   - conversación;
   - pedir a Francisco que invoque `$mattpocock-skills:to-questionnaire` para varias respuestas relacionadas.
8. Solicitar intervención únicamente a los propietarios afectados.
9. Mostrar a Francisco cualquier comunicación exacta antes de crearla o enviarla.
10. Registrar decisión, propietario, fecha, fuente, alcance, razones, supuestos y condiciones de revisión.
11. Dar a cada pregunta abierta un propietario y una siguiente acción.
12. Eliminar de `## Preguntas pendientes` cada pregunta resuelta. Eliminar la sección cuando quede vacía.
13. Volver a la fase afectada cuando una respuesta cambie prioridad, contexto, comprensión o modelo.
14. Si existe bloqueo, preparar una petición de ayuda con objetivo, comprobaciones, conclusión, impacto y pregunta concreta.

**Resultado:** decisiones y alineación suficientes para especificar el trabajo.

**Evidencia:** respuestas, decisiones, confirmaciones, cuestionario y preguntas abiertas con seguimiento.

**Puerta de salida:**

- `DONE`: las cuestiones que pueden cambiar alcance, contratos, solución o validación están resueltas o aceptadas explícitamente.
- `IN_PROGRESS`: falta investigación, propietario, pregunta concreta o confirmación.
- `WAITING`: una respuesta o decisión externa ya se ha solicitado y están identificados el responsable y la condición de reanudación.
- `BLOCKED`: falta formular, autorizar o dirigir una solicitud imprescindible, no se conoce al propietario o no existe una vía conocida de resolución.

**Siguiente paso:** fase 4.
