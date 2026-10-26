# Fase 10. Validación integral y autorrevisión

**Objetivo:** demostrar que el ticket satisface la especificación, los estándares y el comportamiento cross-stack.

**Entrada:** fase 9 superada, evidencia red–green y contexto todavía disponible.

**Acciones:**

1. Revisar rama, `HEAD`, working tree y diff completo.
2. Comparar el diff con especificación, criterios, decisiones, contratos, fuera de alcance y reglas.
3. Detectar código accidental, logs, secretos, archivos inesperados, formato ajeno, comportamiento especulativo y pruebas insensibles.
4. Proponer commits atómicos. Para cada uno, mostrar finalidad, diff staged y mensaje; comprobar SCM y obtener autorización antes de stage o commit.
5. No incluir cambios ajenos ni hacer push.
6. Fijar el commit base o merge-base aprobado y verificar que el diff sea correcto y no vacío.
7. Francisco lee el diff completo y explica criterios, comportamiento, seams, contratos, riesgos, pruebas y validaciones pendientes.
8. Si no puede defender una parte material, mantener `REVISAR` y volver a la fuente o al incremento correspondiente.
9. Ejecutar `$poex-pr-guide` como segunda pasada independiente contra el punto fijo:
   - usar una evaluación focalizada para una rama local sin PR;
   - usar `Full PR review` cuando exista una PR;
   - usar `Follow-up revision` después de cambios posteriores.
10. Contrastar sus hallazgos con especificación, estándares, sistema real y evidencia.
11. Clasificar cada hallazgo como defecto, riesgo, sugerencia, discrepancia sin respaldo o trabajo fuera de alcance.
12. Francisco acepta o rechaza cada hallazgo material con una razón y evidencia.
13. Completar:

```text
criterio
   ↓
implementación
   ↓
prueba
   ↓
resultado
   ↓
evidencia
```

14. Ejecutar las comprobaciones del repositorio: lint, tipos, pruebas, contratos, generación, análisis, build y suite completa.
15. Añadir validación manual, permisos, migraciones, integración, QA u observabilidad cuando aporten una señal distinta.
16. Registrar comandos, repositorio, resultado, duración y diferencia respecto a la línea base.
17. Investigar cualquier fallo antes de atribuirlo o descartarlo.
18. Para defectos confirmados, volver al ciclo red–green de la fase 9.
19. Después de cambios materiales, repetir revisión y validación contra el mismo punto fijo.
20. Preparar un handoff de retorno con ticket, ramas, commits, informes, matriz, comandos, riesgos y siguiente acción.
21. Mostrar el handoff y la actualización de `TASK.md` antes de escribirlos.

**Resultado:** ticket conforme con especificación, estándares y contratos; commits locales revisados y evidencia completa.

**Evidencia:** punto fijo, commits, autorrevisión de Francisco, informe de `$poex-pr-guide`, matriz y comprobaciones.

**Puerta de salida:**

- `SUPERADO`: la autorrevisión y la segunda pasada cubren especificación, estándares y contratos; las comprobaciones pasan y no hay hallazgos materiales abiertos.
- `REVISAR`: existe un fallo, hallazgo, criterio sin evidencia, commit incorrecto o laguna de comprensión.
- `BLOQUEADO`: una dependencia o validación externa impide demostrar que el ticket está listo.

**Siguiente paso:** fase 11 mediante handoff.

