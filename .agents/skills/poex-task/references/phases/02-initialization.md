# Fase 2. Inicializar la tarea

**Objetivo:** preparar y verificar los espacios de trabajo conforme al alcance comprendido, preservando el trabajo existente.

**Entrada:** comprensión `DONE`; componentes oficiales e incógnitas disponibles. Las dudas abiertas no impiden por sí solas esta fase; se detienen únicamente las operaciones que necesiten sus respuestas.

## Pasos

Al iniciar cada paso, actualizar `current_step` y `updated_at`. Los pasos no crean filas en `## Progreso`.

1. **`repositories`: confirmar e inspeccionar.** Contrastar los repositorios afectados con los componentes de Jira y el alcance conocido. Leer sus instrucciones y comprobar ramas, SHA, cambios locales, worktrees y operaciones pendientes. Aclarar discrepancias antes de preparar el repositorio afectado. Conservar `poex-infra` como referencia de solo lectura. Completar cuando se conocen los repositorios necesarios y el trabajo que debe preservarse.
2. **`workspaces`: preparar.** Seguir [workspaces](../workspaces.md): acordar bases, ramas y rutas, mostrar las operaciones exactas y obtener autorización antes de ejecutarlas. Un espacio existente adecuado puede reutilizarse con autorización; no se exige limpiar árboles ni crear worktrees por rutina. Completar cuando los espacios necesarios están disponibles y autorizados.
3. **`verification`: verificar y localizar comprobaciones.** Comprobar identidad Git, ruta, rama o SHA, base y cambios locales. Identificar instrucciones, comandos, directorios y recursos que deban aislarse. Revalidar las conclusiones materiales de comprensión si usaron otra referencia. Reservar las pruebas de referencia para antes de modificar código. Completar cuando otra sesión puede localizar, verificar y utilizar los espacios preparados.

## Actualización de TASK.md

- Registrar estado, fechas y paso actual de `initialize`.
- Rellenar `workspaces` conforme a su contrato: identidad, ruta, rama, base acordada, último SHA y fecha de verificación.
- Conservar las autorizaciones con su alcance y procedencia. Añadir notas solo cuando haya trabajo previo que preservar, restricciones de ejecución, preparación incompleta o referencias necesarias para localizar las comprobaciones.
- Mantener las preguntas abiertas necesarias para continuar. No crear un informe narrativo de inicialización ni resultados de pruebas no ejecutadas.

**DONE:** espacios necesarios para el alcance conocido disponibles, autorizados y verificados; trabajo previo preservado y forma de validación identificada. Si diseño descubre otro repositorio necesario, prepararlo con autorización y actualizar el registro; reabrir la fase pertinente solo cuando su resultado haya quedado invalidado.

**Siguiente:** `design`, con un encargo de planificación abierto en POEX Coach.
