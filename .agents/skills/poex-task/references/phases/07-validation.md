# Fase 7. Validar la integración

**Entrada:** implementación y revisión `DONE`, con versiones identificadas por repositorio. Continuar en la misma conversación de implementación mientras conserve contexto útil.

## Encargo y verificación

1. Inventariar la evidencia ya obtenida y los criterios aún sin comprobar. Definir un encargo de validación con comandos, entornos, versiones y permisos. Las pruebas que escriban datos requieren un entorno y alcance autorizados.
2. Verificar el comportamiento conjunto: productores y consumidores, permisos, errores, compatibilidad, generación y QA pertinentes. Completar las comprobaciones obligatorias de cada repositorio y la evidencia adicional que aporte una señal distinta.
3. Si hace falta contraste POEX independiente, preparar un encargo con `$poex-pr-guide` y su checkpoint humano, indicando las cuestiones que la revisión anterior no cubre. La revisión previa sigue siendo evidencia, no se repite por defecto.
4. Contrastar criterio → cambio → prueba → resultado. Asociar cada prueba con el contenido real ejecutado, no solo con el último commit o el nombre de la rama.
5. Ante un fallo, distinguir defecto nuevo, fallo previo, entorno o ausencia de evidencia. Las correcciones reabren `implement`; un cambio de decisión reabre la fase correspondiente. Después, invalidar solo las comprobaciones cuyo resultado haya quedado afectado.
6. El coach comprueba los resultados accesibles y registra carencias y seguimientos. Una duda abierta no impide por sí sola avanzar; una validación necesaria pendiente mantiene abierto el resultado que depende de ella.

## Actualización de TASK.md

- Estado, inicio y fin de `validate`, con ticket cuando exista; encargo y sesión.
- Criterios comprobados, resultado y referencias al código y entorno realmente utilizados. Mantener informes extensos en sus fuentes.
- Fallos o comprobaciones pendientes, efecto y siguiente acción. Añadir preguntas nuevas y retirar las resueltas.
- Mantener el ticket abierto hasta satisfacer su condición de integración. Las correcciones reabren `implement` y solo invalidan la evidencia afectada.

**DONE:** criterios y funcionamiento conjunto comprobados sobre las versiones actuales, con evidencia trazable y sin fallos materiales ni validaciones necesarias pendientes.

**Siguiente:** `deliver`. La validación del conjunto de todos los tickets se comprueba también antes del cierre final.
