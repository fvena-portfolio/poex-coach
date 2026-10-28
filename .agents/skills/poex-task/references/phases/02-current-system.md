# Fase 2. Investigación detallada y modelo del sistema actual

**Objetivo:** demostrar en profundidad cómo funciona el comportamiento afectado, cuáles son sus contratos y riesgos y dónde debe realizarse el cambio antes de diseñar la solución.

**Entrada:** tarea comprendida, orientación técnica inicial registrada y repositorios preparados.

**Acciones:**

1. Usar la orientación de la fase 1 como punto de partida, no como evidencia suficiente.
2. Verificar sus hechos, corregir sus hipótesis y ampliar los repositorios, módulos y capas cuando la evidencia lo exija.
3. Identificar repositorios, módulos, capas y sistemas implicados.
4. Leer las instrucciones y documentación aplicables de cada repositorio.
5. Registrar rama, `HEAD`, upstream, base esperada y estado del árbol sin modificarlo.
6. Contrastar con GitHub cuando la vigencia pueda cambiar una conclusión.
7. Separar el trabajo de la tarea de cambios previos o ajenos.
8. Localizar entradas, responsabilidades, productores, consumidores, validaciones, autorización, reglas de negocio, persistencia, transacciones, procesos asíncronos, errores, pruebas, configuración y despliegue.
9. Modelar el flujo proporcionalmente:

```text
usuario o proceso
        ↓
interfaz o automatización
        ↓
cliente o integración
        ↓
API y autorización
        ↓
lógica de negocio
        ↓
persistencia o sistema externo
        ↓
respuesta, estado, errores y observabilidad
```

10. Identificar la capa propietaria de cada decisión.
11. Comparar ambos extremos de rutas, métodos, payloads, tipos, enums, nullability, errores, permisos, versionado y compatibilidad.
12. Examinar qué demuestran realmente las pruebas existentes.
13. Reproducir el comportamiento actual cuando aporte evidencia y exista autorización.
14. Aplicar la lente cross-stack y registrar riesgos, dependencias y desconocidos.
15. Presentar el modelo del sistema actual y preguntar a Francisco qué dudas le ha generado.
16. Resolver una duda cada vez mediante la evidencia investigada o una consulta puntual.
17. Registrar en `## Preguntas pendientes` las dudas que no puedan resolverse y requieran una respuesta externa, conservando únicamente la pregunta exacta y el propietario esperado.
18. Las dudas registradas no cambian por sí solas el estado de la fase. Continuar la investigación y acumularlas para la fase 3.
19. Pedir a Francisco que explique el flujo y las responsabilidades.
20. Leer la referencia de nivel de garantía, recomendar `BASIC`, `STANDARD` o `HIGH` a partir de la evidencia observada y solicitar la confirmación de Francisco. Después de confirmarla, sustituir `PENDING` por el nivel acordado en `TASK.md` mediante el procedimiento de persistencia.

**Resultado:** modelo trazable del sistema actual, contratos, repositorios, riesgos y nivel de garantía confirmado.

**Evidencia:** estado Git, referencias al código y las pruebas, modelo end-to-end, contratos, explicación de Francisco y nivel de garantía confirmado.

**Puerta de salida:**

Las dudas registradas para recopilarlas en la fase 3 no provocan `WAITING` ni `BLOCKED`.

- `DONE`: el comportamiento y los contratos relevantes están explicados con evidencia vigente y el nivel de garantía está confirmado.
- `IN_PROGRESS`: falta investigar, verificar vigencia o corregir una explicación.
- `WAITING`: se ha solicitado una evidencia, un acceso o una aclaración externa y están identificados el responsable y la condición de reanudación.
- `BLOCKED`: falta formular, autorizar o dirigir una solicitud necesaria, no existe una vía conocida de resolución o no puede determinarse el comportamiento con seguridad.

**Siguiente paso:** fase 3.
