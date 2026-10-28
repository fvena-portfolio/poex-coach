# Fase 10. Cierre y aprendizaje

**Objetivo:** confirmar la definición de terminado, cerrar compromisos y conservar aprendizajes basados en evidencia.

**Entrada:** todos los tickets integrados, resultado conjunto comprobado, feedback resuelto y estado de despliegue conocido.

**Acciones:**

1. Recuperar la definición de terminado desde Jira, documentación, repositorios, especificación y compromisos.
2. Comprobar el resultado completo y no solo el último ticket.
3. Diferenciar:
   - implementado;
   - integrado;
   - desplegado;
   - habilitado;
   - validado;
   - aceptado;
   - cerrado oficialmente.
4. Comprobar criterios, PR, checks, cross-stack, compatibilidad, migraciones, despliegue, observabilidad, QA, documentación y comunicaciones aplicables.
5. Si falta una validación, registrar responsable y condición de reanudación y mantener la tarea `IN_PROGRESS` o `WAITING`.
6. Si aparece un defecto material, volver a la fase correspondiente.
7. Cuando proceda, verificar el entorno desplegado mediante versión, pipeline, health checks, smoke tests, comprobación funcional, evidencia visual, logs o confirmación de QA.
8. No atribuir al código revisado un entorno con otra versión, configuración o flag.
9. Registrar seguimientos con motivo, propietario, fuente, condición y siguiente acción.
10. Comparar el estado real con Jira.
11. Preparar transición, comentario, enlaces y evidencia exactos. Francisco modifica Jira manualmente. El agente puede verificarlo en modo de solo lectura.
12. Mostrar y autorizar por separado cualquier comunicación o cambio en otro sistema externo.
13. No declarar cierre oficial mientras una fuente obligatoria siga siendo incompatible sin un responsable confirmado.
14. Completar:

```text
necesidad oficial
        ↓
criterio
        ↓
ticket
        ↓
PR y commits
        ↓
pruebas
        ↓
despliegue o validación
        ↓
evidencia final
```

15. Pedir a Francisco que invoque `$mattpocock-skills:retro` sobre las fuentes primarias. Leer primero `$mattpocock-skills:writing-for-agents`.
16. Buscar mejoras de navegación, comprobaciones automáticas, estándares, instrucciones, herramientas, no-ops y acceso a información.
17. Comprobar la configuración existente antes de proponer una nueva validación.
18. Preferir lint, hooks, tests o CI para errores mecánicos; estándares para decisiones de juicio; punteros para navegación.
19. Registrar evidencia, problema, impacto, cambio mínimo, propietario, coste y prioridad de cada candidato.
20. Eliminar candidatos especulativos o duplicados. `$mattpocock-skills:retro` no aplica cambios automáticamente.
21. Registrar solo métricas confirmadas: estimación, esfuerzo, espera, interrupciones, retrabajo, fases repetidas y defectos.
22. Distinguir hechos, observaciones, hipótesis, aprendizajes y experimentos.
23. Inspeccionar el estado local final y proponer cualquier limpieza con comandos y efectos exactos.
24. No eliminar ramas, worktrees, archivos ni cambios sin autorización.
25. Actualizar `TASK.md` automáticamente después de evaluar el resultado y verificar la escritura.
26. Marcar `DONE` únicamente cuando la definición de terminado se cumpla, las fuentes sean coherentes, los seguimientos tengan propietario, la evidencia sea reconstruible y Francisco confirme el cierre.

**Resultado:** tarea cerrada con evidencia, seguimientos y aprendizaje trazables.

**Evidencia:** criterios, matriz, PR, CI, despliegue, Jira verificado, comunicaciones, retro, métricas, estado local y expediente actualizado y verificado.

**Puerta de salida:**

- `DONE`: definición de terminado satisfecha, estado oficial coherente y expediente actualizado y verificado.
- `IN_PROGRESS`: falta una comprobación, actualización, comunicación, evidencia o aprobación.
- `WAITING`: una validación, un despliegue, una decisión o una dependencia externa ya se ha solicitado o está en curso y están identificados el responsable y la condición de reanudación.
- `BLOCKED`: falta formular, autorizar o dirigir una solicitud necesaria, o no existe una vía conocida para obtener la validación, despliegue, decisión o dependencia requerida.

**Siguiente paso:** flujo terminado. Otra tarea se inicia o reanuda mediante su propia clave.

