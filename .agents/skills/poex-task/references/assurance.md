# Nivel de garantía proporcional

## Núcleo mínimo

Toda tarea debe demostrar:

1. fuente oficial y prioridad;
2. comprensión personal del problema;
3. conocimiento suficiente del sistema actual;
4. resolución de las decisiones materiales;
5. comportamiento esperado y validación definidos;
6. preparación segura de los repositorios;
7. implementación incremental;
8. revisión contra especificación y estándares;
9. evidencia del resultado;
10. estado oficial y continuidad conocidos.

Una fase puede ser breve. No puede marcarse `DONE` sin su resultado y evidencia.

## Niveles

### `BASIC`

Se utiliza cuando el comportamiento es conocido, el cambio es localizado y reversible, existe un patrón claro y no hay migraciones, riesgos materiales de seguridad o datos, contratos cross-stack nuevos ni dependencias externas inciertas.

Aplicación:

- contexto y modelo breves;
- especificación compacta;
- normalmente un solo ticket;
- pruebas focalizadas en seams existentes;
- comprobaciones obligatorias del repositorio;
- artefactos mínimos.

### `STANDARD`

Es el nivel predeterminado cuando la tarea no cumple todas las condiciones de `BASIC` ni presenta una señal clara de riesgo elevado.

Se aplica, por ejemplo, cuando existen varios módulos, cambios coordinados pero acotados, casos alternativos relevantes, incertidumbre moderada, varios tickets o coordinación con otra persona.

Aplicación:

- investigación completa de las capas afectadas;
- especificación y tickets explícitos;
- matriz de trazabilidad;
- pruebas por comportamiento;
- revisión cross-stack proporcional;
- validación completa del repositorio.

### `HIGH`

Se utiliza cuando aparece al menos una señal material:

- varios repositorios o capas;
- dinero o cálculos financieros;
- autenticación, autorización o seguridad;
- datos sensibles o de clientes;
- migraciones o cambios de esquema;
- concurrencia, idempotencia o transacciones;
- procesos asíncronos;
- integraciones externas;
- compatibilidad entre versiones;
- despliegue ordenado o feature flags;
- impacto operativo alto;
- cambio difícil de revertir;
- requisitos ambiguos o contradictorios;
- observabilidad insuficiente;
- hotfix de producción;
- riesgo de pérdida, corrupción o exposición de datos.

Aplicación:

- modelo end-to-end explícito;
- contratos comparados en ambos extremos;
- riesgos y alternativas documentados;
- alineación con los propietarios afectados;
- tipos de prueba que aporten señales distintas;
- revisión cross-stack completa;
- estrategia de despliegue y rollback;
- evidencia reforzada.

Una señal elevada obliga a controlar el riesgo que representa. No obliga a producir documentación irrelevante.

## Clasificación

`PENDING` indica que la tarea aún no ha sido clasificada. No es un nivel de garantía y solo puede mantenerse hasta completar la fase 2.

La clasificación inicial se realiza al final de la fase 2, después de investigar el sistema actual y sus riesgos, y se registra en `TASK.md`. Después de la confirmación de Francisco, sustituye `PENDING` por `BASIC`, `STANDARD` o `HIGH`.

`assurance_level` expresa cuánto análisis, validación y evidencia requiere la tarea. No estima esfuerzo ni story points.

El agente:

1. presenta las señales observadas;
2. recomienda un nivel;
3. explica qué profundidad añade;
4. solicita la confirmación de Francisco.

Los riesgos nuevos pueden elevar el nivel inmediatamente. Reducirlo requiere evidencia y confirmación de Francisco. Si existen señales distintas, prevalece el mayor riesgo material.

## Urgencia

La urgencia puede comprimir explicaciones, reuniones y artefactos. No reduce por sí sola una tarea de `HIGH` a `BASIC`.

Siempre deben conservarse:

- problema y resultado esperado;
- alcance y riesgo aceptado;
- propietario de la decisión;
- estado de los repositorios;
- comprobación sensible al cambio;
- revisión del diff;
- evidencia del resultado;
- comunicación y seguimiento pendientes.

Toda comprobación aplazada debe registrar qué falta, el riesgo aceptado, quién lo acepta, el responsable y la condición o fecha de seguimiento.
