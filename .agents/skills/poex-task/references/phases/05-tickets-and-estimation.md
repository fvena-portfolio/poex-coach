# Fase 5. Plan, tickets, validación y estimación

**Objetivo:** convertir la especificación en tickets verticales, trazables, ordenados y estimables.

**Entrada:** especificación aprobada, criterios comprobables y seams definidos.

**Acciones:**

1. Pedir a Francisco que invoque `$mattpocock-skills:to-tickets` sobre la especificación aprobada.
2. Crear tracer bullets verticales. Cada ticket debe entregar comportamiento end-to-end, ser comprobable, mantener el sistema válido y caber en un contexto nuevo.
3. Evitar divisiones horizontales por frontend, backend o pruebas sin valor independiente.
4. Para varios repositorios, definir responsabilidades, contratos, orden compatible y evidencia conjunta.
5. Crear prefactoring separado solo si reduce un riesgo concreto y puede validarse.
6. Para migraciones amplias, usar `expandir → migrar → contraer`; declarar una rama de integración si los estados intermedios no pueden aterrizar por separado.
7. Definir por ticket comportamiento, criterios, seams, repositorios, contratos, evidencia, riesgos, bloqueadores y estado.
8. Construir el grafo de dependencias y su frontera disponible.
9. Comprobar:

```text
criterio
   ↓
ticket
   ↓
implementación
   ↓
prueba
   ↓
evidencia
```

10. Aplicar la lente cross-stack y comprobar que no falten criterios ni existan tickets sin respaldo.
11. Validar con Francisco granularidad, bloqueadores y orden.
12. Si una duda solo puede resolverse ejecutando código, realizar un prototipo acotado mediante handoff y volver a aprobar la especificación.
13. Estimar después de aprobar el desglose.
14. Registrar rango, confianza, supuestos, riesgos, dependencias y trabajo excluido.
15. Separar esfuerzo de implementación, espera, revisión y despliegue.
16. Mostrar el desglose exacto antes de pedir la invocación de `$mattpocock-skills:to-tickets`.
17. Con aprobación, crear `.scratch/<slug>/issues/<NN>-<slug>.md`.
18. Ordenar por dependencia y marcar como disponibles solo los tickets de la frontera.
19. Preparar para Francisco cualquier actualización manual necesaria en Jira.

**Resultado:** tickets autosuficientes, grafo coherente, cobertura completa y estimación sustentada.

**Evidencia:** archivos locales, dependencias, matriz de trazabilidad, revisión cross-stack y estimaciones.

**Puerta de salida:**

- `DONE`: los tickets cubren la especificación, sus dependencias son correctas y la estimación tiene fundamento.
- `IN_PROGRESS`: existen cortes incorrectos, criterios sin cobertura, tickets grandes o estimaciones débiles.
- `WAITING`: una decisión, un prototipo o un compromiso externo ya se ha solicitado y están identificados el responsable y la condición de reanudación.
- `BLOCKED`: falta formular, autorizar o dirigir una solicitud necesaria, o no existe una vía conocida para obtener la decisión, investigación, prototipo o compromiso requerido.

**Siguiente paso:** fase 6.

