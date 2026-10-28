# Fase 7. Implementación incremental

**Objetivo:** implementar un ticket mediante incrementos observables y comprobables.

**Entrada:** ticket, handoff, rama, línea base, seams y autorización para modificar código.

**Acciones:**

1. Leer instrucciones, ticket, especificación, criterios, decisiones, contratos y handoff.
2. Comprobar repositorio, rama, `HEAD`, estado, upstream, bloqueadores y línea base.
3. Volver a la fase 6 si el estado material ha cambiado.
4. Ejecutar `$mattpocock-skills:tdd` y coordinar directamente la implementación según los pasos de esta fase.
5. Trabajar en ciclos:

```text
comportamiento pequeño
        ↓
prueba que falla por la razón esperada
        ↓
implementación mínima
        ↓
prueba que pasa
        ↓
siguiente comportamiento
```

6. Una prueba roja debe fallar por el comportamiento ausente, no por un entorno roto.
7. Las pruebas verifican comportamiento mediante interfaces públicas. Evitan métodos privados, estructura interna, snapshots sin intención y mocks de módulos propios.
8. Los mocks se reservan para límites como APIs externas, tiempo, aleatoriedad, sistema de archivos o infraestructura.
9. Si TDD no es viable, explicar la limitación, proponer evidencia alternativa y obtener confirmación.
10. No cambiar silenciosamente el seam acordado.
11. Implementar solo el comportamiento del ticket.
12. Clasificar cualquier hallazgo como necesario, cambio de especificación, trabajo futuro, defecto independiente o deuda.
13. Volver a la fase afectada cuando cambien prioridad, contexto, producto, modelo, decisión, especificación, tickets o estrategia Git.
14. Ejecutar regularmente pruebas focalizadas, tipos, lint rápido y generación necesaria.
15. Comparar ambos extremos de cualquier contrato modificado.
16. Registrar criterio, prueba, rojo, verde, archivos y decisiones de cada incremento.
17. Para varios repositorios, conservar el ticket como unidad end-to-end y usar handoffs entre directorios.
18. Después de cada incremento material, Francisco explica comportamiento, prueba, decisión y riesgo.
19. Comprobar al final criterios, pruebas, tipos, alcance y estado Git.
20. No realizar stage, commit, push ni publicación durante esta fase.

**Resultado:** comportamiento implementado con evidencia red–green y comprensión humana.

**Evidencia:** comandos, resultados, pruebas, diff, contratos, decisiones y explicación de Francisco.

**Puerta de salida:**

- `DONE`: los criterios del ticket están implementados, la evidencia es sensible y Francisco puede defender el cambio.
- `IN_PROGRESS`: falta un criterio, una prueba, una comprobación o comprensión.
- `WAITING`: una decisión, aclaración de contrato, acceso o dependencia externa ya se ha solicitado y están identificados el responsable y la condición de reanudación.
- `BLOCKED`: falta formular, autorizar o dirigir una solicitud imprescindible, o no existe una vía conocida para obtener la decisión, aclaración, acceso o dependencia requerida.

**Siguiente paso:** fase 8 en el mismo contexto.

