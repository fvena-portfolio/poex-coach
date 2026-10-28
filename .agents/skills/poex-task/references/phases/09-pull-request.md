# Fase 9. Pull request, comunicación y feedback

**Objetivo:** publicar un cambio revisable y procesar sus comprobaciones y feedback hasta integrarlo.

**Entrada:** commits revisados, validación satisfactoria, handoff de retorno y comprensión de Francisco.

**Acciones:**

1. Reconstruir ticket, ramas, commits, bases, comprobaciones, riesgos y dependencias.
2. Consultar en modo de solo lectura el estado remoto, reglas, plantilla, checks, revisores y trabajo paralelo.
3. Definir por repositorio base, commits, estado draft o ready, relaciones entre PR y orden de integración y despliegue.
4. Para trabajo cross-stack, comprobar compatibilidad entre versiones, bloqueos, feature flags y rollback.
5. Ejecutar `$mattpocock-skills:pr` y respetar la plantilla del repositorio.
6. Incluir, como mínimo:

```markdown
## Summary
<explicación o visualización mínima>

## Evidence
- **Before:** <evidencia>
- **After:** <evidencia>

## Merge Danger
**Door:** <one-way o two-way>
**Blast Radius:** <alcance>
```

7. Enlazar Jira, criterios, PR relacionados, dependencias, migraciones, flags, orden de despliegue, QA, riesgos y fuera de alcance cuando corresponda.
8. Mostrar repositorio, rama, commits, base, título, cuerpo, estado, revisores, etiquetas, relaciones y acciones exactas.
9. Obtener autorización antes de push, creación o edición del PR, revisores, etiquetas, relaciones entre PR o comunicaciones.
10. Publicar sin force push y verificar el resultado.
11. Preparar comunicaciones con estado comprobado, comportamiento, evidencia, riesgos, acción, ayuda y próxima actualización.
12. Diferenciar implementado, PR abierto, revisión pendiente, aprobado, integrado y desplegado.
13. Para actualizar Jira, preparar el elemento, campo, transición o comentario exacto. Francisco lo aplica manualmente.
14. Consultar CI, comentarios, revisiones, conflictos, base y dependencias.
15. Mientras se espera, utilizar `WAITING`, registrar la dependencia y permitir trabajar en otra tarea.
16. Investigar los fallos de CI antes de reejecutarlos.
17. Clasificar el feedback y contrastarlo con especificación, estándares y sistema real.
18. Mostrar las respuestas exactas antes de publicarlas.
19. Si el feedback exige código, volver por handoff a las fases 7 y 8. Si cambia alcance o decisiones, volver a la fase correspondiente.
20. Revisar después de cada actualización el diff acumulado, validación y coherencia cross-stack.
21. Antes del merge, comprobar aprobaciones, CI, conflictos, base, feedback, compatibilidad, migraciones, flags, despliegue y rollback.
22. No aprobar el propio PR ni ejecutar el merge sin autorización y proceso aplicable.
23. Verificar el merge y registrar referencia, fecha, PR y validaciones pendientes.

### Actualización del grafo

24. Considerar integrado el ticket solo cuando sus PR estén integrados, sus checks hayan terminado, sus criterios tengan evidencia y se conozca la validación posterior.
25. Marcarlo en el grafo, retirar sus bloqueos e identificar la nueva frontera.
26. Si quedan tickets:
   - seleccionar uno de la frontera;
   - conservar la misma especificación;
   - volver a la fase 6;
   - no avanzar a la fase 10.
27. Si cambian los supuestos de tickets pendientes, volver a la fase correspondiente.
28. Cuando todos estén integrados, comprobar el resultado conjunto contra especificación, criterios, trazabilidad, flujo cross-stack y despliegue.
29. Actualizar `TASK.md` automáticamente después de evaluar el resultado y verificar la escritura.

**Resultado:** ticket integrado o bloqueo externo trazable; estado y comunicación coherentes.

**Evidencia:** PR, commits, CI, revisiones, feedback, comunicaciones, merge y expediente.

**Puerta de salida:**

- `DONE`: el ticket está integrado y, si era el último, el resultado conjunto está comprobado.
- `IN_PROGRESS`: queda una acción de PR, CI, feedback, comunicación o merge.
- `WAITING`: CI, una revisión, una decisión o una dependencia externa ya está solicitada o en curso y están identificados el responsable y la condición de reanudación.
- `BLOCKED`: falta formular, autorizar o dirigir una solicitud necesaria, falta acceso sin una vía conocida de resolución o no se sabe cómo obtener la decisión, revisión o dependencia requerida.

**Siguiente paso:**

- si quedan tickets, fase 6;
- si todos están integrados y el resultado conjunto está comprobado, fase 10.

