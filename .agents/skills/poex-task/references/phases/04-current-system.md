# Fase 4. Investigación y modelo del sistema actual

**Objetivo:** comprender el comportamiento actual y sus contratos antes de diseñar cambios.

**Entrada:** problema comprendido y repositorios potencialmente afectados.

**Acciones:**

1. Identificar repositorios, módulos, capas y sistemas implicados.
2. Leer las instrucciones y documentación aplicables de cada repositorio.
3. Registrar rama, `HEAD`, upstream, base esperada y estado del árbol sin modificarlo.
4. Contrastar con GitHub cuando la vigencia pueda cambiar una conclusión.
5. Separar el trabajo de la tarea de cambios previos o ajenos.
6. Localizar entradas, responsabilidades, productores, consumidores, validaciones, autorización, reglas de negocio, persistencia, transacciones, procesos asíncronos, errores, pruebas, configuración y despliegue.
7. Modelar el flujo proporcionalmente:

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

8. Identificar la capa propietaria de cada decisión.
9. Comparar ambos extremos de rutas, métodos, payloads, tipos, enums, nullability, errores, permisos, versionado y compatibilidad.
10. Examinar qué demuestran realmente las pruebas existentes.
11. Reproducir el comportamiento actual cuando aporte evidencia y exista autorización.
12. Aplicar la lente cross-stack y registrar riesgos, dependencias y desconocidos.
13. Pedir a Francisco que explique el flujo y las responsabilidades.

**Resultado:** modelo trazable del sistema actual, contratos, repositorios y riesgos.

**Evidencia:** estado Git, referencias al código y las pruebas, modelo end-to-end, contratos y explicación de Francisco.

**Puerta de salida:**

- `SUPERADO`: el comportamiento y los contratos relevantes están explicados con evidencia vigente.
- `REVISAR`: falta investigar, verificar vigencia o corregir una explicación.
- `BLOQUEADO`: falta acceso o no puede determinarse el comportamiento con seguridad.

**Siguiente paso:** fase 5.

