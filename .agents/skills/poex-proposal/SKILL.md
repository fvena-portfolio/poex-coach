---
name: poex-proposal
description: "Redacta un resumen breve de la solución propuesta para un repositorio POEX, listo para compartir con sus desarrolladores y pedir feedback desde la conversación de diseño."
---

# Propuesta breve por repositorio

Prepara un mensaje que Francisco pueda copiar para los desarrolladores originales del repositorio. Usa el contexto de la conversación de diseño, normalmente después de `grill-with-docs`. La salida es una propuesta para contrastar, no una especificación ni un encargo de implementación.

## Entrada y alcance

- Uso: `$poex-proposal frontend` o `$poex-proposal backend`. El argumento selecciona un repositorio; también admite su nombre completo o ruta y otros repositorios identificados en la tarea.
- Recupera de la conversación la clave, el título y la URL oficiales de Jira, el problema y la solución propuesta para ese repositorio. Si hace falta un dato, consulta solo la fuente pertinente ya referenciada, como TASK.md o Jira, en solo lectura.
- Si el repositorio o la tarea son ambiguos, o falta la propuesta que debe resumirse, solicita una sola aclaración. No diseñes una solución nueva para rellenar el mensaje.
- Usa los nombres de módulos, conceptos y contratos que los destinatarios conocen. Menciona otro repositorio solo cuando su interacción sea necesaria para entender la propuesta del repositorio elegido.

## Redacción

Entrega únicamente el mensaje listo para copiar, en el idioma solicitado o, por defecto, en español. Conserva el título oficial de la tarea. Usa este formato:

```markdown
**[<clave> — <título oficial>](<URL de Jira>)**

<Un párrafo breve que describa el problema y el resultado que se busca.>

**Propuesta para <repositorio>:** <Un párrafo breve que explique qué cambiaríamos, dónde a nivel de responsabilidad o módulo y cómo resolvería el problema.>
```

Busca unas 100–180 palabras como orientación, sin alargar una propuesta que pueda explicarse en menos. Escribe frases concretas y directas, adaptadas a personas que conocen el repositorio. Incluye nombres técnicos solo cuando ayuden a reconocer el cambio; evita explicar fundamentos, enumerar archivos o métodos, pegar código o desarrollar criterios de aceptación y planes de pruebas.

Distingue el comportamiento actual de lo propuesto y conserva el grado real de acuerdo. Una alternativa aún abierta no se presenta como una decisión tomada. Si una duda condiciona materialmente la propuesta, indícala en una frase al final del párrafo de solución; no copies la lista completa de preguntas de la tarea. Si se pide feedback sobre una elección concreta, incorpora esa pregunta de forma breve.

Los destinatarios deben poder entender el mensaje sin acceder al chat, TASK.md ni rutas locales. Conserva el enlace oficial de Jira y añade otra referencia compartible solo si resulta necesaria para interpretar la propuesta. Excluye datos sensibles e información personal innecesaria.

## Salida y límite

Devuelve el borrador en la conversación para que Francisco lo revise y comparta. La invocación no envía mensajes, publica contenido, crea archivos, modifica TASK.md ni cambia el estado de la tarea. No incluye instrucciones para otro agente ni un handoff técnico extenso.

Completa cuando el texto identifica la tarea, explica el problema y transmite fielmente la propuesta del repositorio solicitado, con las incertidumbres materiales visibles y sin introducir decisiones nuevas.
