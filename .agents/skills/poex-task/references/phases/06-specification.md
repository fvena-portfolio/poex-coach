# Fase 6. Especificación

**Objetivo:** convertir lo aprendido en una especificación autosuficiente, comprobable y defendible.

**Entrada:** fases 1–5 superadas y decisiones materiales resueltas.

**Acciones:**

1. Pedir a Francisco que invoque `$mattpocock-skills:to-spec` como síntesis, no como una nueva entrevista.
2. Volver a la fase correspondiente si la redacción descubre una carencia material.
3. Describir el problema y la solución mediante comportamiento observable.
4. Incluir historias para actores, flujo principal, estados, errores, permisos, límites, compatibilidad y recuperación aplicables.
5. Convertir los criterios oficiales en condiciones inequívocas, observables y trazables.
6. Documentar decisiones ya acordadas sobre responsabilidades, contratos, datos, autorización, errores y despliegue.
7. Evitar rutas de archivos y código volátil, salvo una decisión precisa procedente de un prototipo.
8. Definir las decisiones de prueba y los seams antes de dividir el trabajo.
9. Preferir seams públicos, estables y existentes.
10. Incluir alcance, fuera de alcance, supuestos, dependencias, riesgos y preguntas no bloqueantes.
11. Mantener coherencia entre experiencia de usuario, frontend, API, backend, datos, autorización, QA, observabilidad y despliegue.
12. Comprobar:

```text
fuente oficial
      ↓
comportamiento
      ↓
criterio
      ↓
seam y evidencia previstos
```

13. Pedir a Francisco que explique problema, comportamiento, alcance, validación y riesgos.
14. Mostrar la especificación exacta antes de escribirla.
15. Con aprobación, pedir a Francisco que invoque `$mattpocock-skills:to-spec` y crear `.scratch/<slug>/spec.md`.
16. Si Jira necesita actualizarse, preparar el cambio exacto para que Francisco lo aplique manualmente.

Estructura mínima:

```markdown
## Problema
## Solución
## Historias de usuario
## Criterios de aceptación
## Decisiones de implementación
## Decisiones de prueba
## Contratos y compatibilidad
## Riesgos y dependencias
## Fuera de alcance
## Notas y preguntas no bloqueantes
```

**Resultado:** especificación aprobada, coherente y comprobable.

**Evidencia:** `.scratch/<slug>/spec.md`, fuentes, trazabilidad, seams aprobados y explicación de Francisco.

**Puerta de salida:**

- `SUPERADO`: la especificación es autosuficiente, comprobable y defendible.
- `REVISAR`: contiene ambigüedades, criterios débiles o contratos inconsistentes.
- `BLOQUEADO`: falta una decisión o fuente imprescindible.

**Siguiente paso:** fase 7.

