# Fase 6. Validación de repositorios y handoff

**Objetivo:** comprobar que los repositorios preparados en la fase 1 siguen listos para implementar y transferir un ticket disponible a un contexto nuevo.

**Entrada:** fase 5 superada, ticket de la frontera seleccionado, ramas preparadas en la fase 1 y autorización para cualquier actualización necesaria.

**Acciones:**

1. Confirmar comportamiento, criterios, bloqueadores, repositorios, contratos y evidencia del ticket.
2. Revalidar las instrucciones SCM y los comandos de validación que puedan haber cambiado desde la fase 1.
3. Comparar por repositorio la rama, `HEAD`, upstream, base, working tree, índice, archivos sin seguimiento, commits locales, operaciones incompletas y worktrees con el estado registrado en la fase 1.
4. Consultar GitHub en modo de solo lectura cuando sea necesario para comprobar la vigencia de la base o de la rama remota.
5. Detectar cambios posteriores en la rama base, divergencias, trabajo local inesperado o cambios en los componentes afectados.
6. Clasificar cualquier cambio local. No usar `stash`, `reset`, `clean`, cambio de rama, rebase, merge o modificación del índice sin decisión expresa.
7. Resolver dentro de esta fase los problemas operativos de Git: rama ausente, base incorrecta, rama desactualizada o estado local que impida usarla.
8. Si aparece un componente nuevo:
   - preparar su repositorio en esta fase cuando ya esté cubierto por la especificación y el ticket aprobados;
   - reabrir el resultado anterior afectado cuando cambie el alcance, los contratos, los criterios, la especificación o los tickets.
9. Para cada corrección operativa, mostrar el estado, el riesgo, los comandos exactos, las comprobaciones y el mecanismo de recuperación.
10. Obtener la decisión y autorización de Francisco antes de cambiar el estado del repositorio.
11. Con autorización, crear, reutilizar, cambiar o actualizar la rama necesaria. Preservar todos los cambios y detenerse ante divergencias, conflictos o resultados inesperados. No usar `reset --hard`, `clean` ni force push.
12. No modificar `poex-infra`.
13. Ejecutar la línea base proporcional: dependencias, generación, lint, tipos, pruebas, build o health check.
14. Separar fallos preexistentes de fallos introducidos.
15. Pedir a Francisco que invoque `$mattpocock-skills:handoff` hacia el repositorio de implementación.
16. El handoff temporal referencia ticket, especificación, criterios, decisiones, repositorios, rama, `HEAD`, línea base, validaciones, riesgos y evidencia esperada.
17. Mostrar el handoff exacto antes de escribirlo.
18. Actualizar `TASK.md` automáticamente después de evaluar el resultado y verificar la escritura.

**Resultado:** repositorios revalidados, línea base conocida y handoff autosuficiente.

**Evidencia:** estado Git anterior y posterior, autorización, commits base, línea base, handoff y expediente actualizado y verificado.

**Puerta de salida:**

- `DONE`: el ticket está disponible, las ramas siguen siendo correctas y están actualizadas respecto a la base acordada, el trabajo previo está protegido y la implementación puede comenzar.
- `IN_PROGRESS`: falta preservar, actualizar, validar o completar el handoff.
- `WAITING`: una decisión o actuación externa ya se ha solicitado y están identificados el responsable y la condición de reanudación.
- `BLOCKED`: falta formular, autorizar o dirigir una solicitud necesaria, no existe una vía conocida de resolución o un conflicto, divergencia, cambio desconocido o fallo impide avanzar.

**Siguiente paso:** fase 7 en un contexto nuevo del repositorio.
