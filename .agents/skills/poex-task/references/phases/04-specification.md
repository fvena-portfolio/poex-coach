# Fase 4. Especificar

**Entrada:** diseño `DONE` y elección de Francisco de continuar con `specify`. Es una fase opcional.

**Encargo:** `$mattpocock-skills:to-spec`. El prompt indica expresamente que se pega en la misma conversación de `grill-with-docs`. Sintetizar lo trabajado, enlazando Jira y las fuentes necesarias; distinguir decisiones confirmadas de cuestiones abiertas, sin inventar respuestas.

## Resultado y verificación

1. La propuesta conserva la estructura de la skill y permite observar comportamiento, actores, casos alternativos, errores, permisos, límites, compatibilidad y fuera de alcance relevantes.
2. Los criterios oficiales se relacionan con comportamiento verificable y decisiones ya acordadas. No se añaden requisitos durante la redacción.
3. Los puntos públicos donde probar se acuerdan con Francisco; se explica qué detecta y qué deja fuera cada uno. Preferir los existentes cuando sean adecuados.
4. Contrastar responsabilidades y contratos entre repositorios, riesgos, dependencias y pruebas. Evitar rutas y código volátiles salvo una decisión precisa surgida de un prototipo.
5. Francisco revisa la propuesta. La revisión del documento es el punto de control; no exigir una explicación adicional de todo el diseño como condición de cierre. Las preguntas pendientes no obligan por sí solas a volver a `design`; identificar qué partes de la especificación siguen condicionadas.
6. Mostrar el contenido exacto antes de escribir `.scratch/<slug>/spec.md`. Con aprobación, preparar la continuación de escritura en la misma sesión; verificar el archivo y su huella al retorno. No invocar una segunda síntesis si solo falta guardar el texto aprobado.
7. Preparar cualquier cambio necesario en Jira para su aplicación manual.

## Actualización de TASK.md

- Estado, inicio y fin de `specify` y ciclo del encargo.
- Enlace a `.scratch/<slug>/spec.md` una vez guardado y comprobado, con su versión o huella verificada.
- Preguntas nuevas en la lista común y retirada de las resueltas.
- Mantener decisiones y contenido en la especificación; el expediente solo la referencia.

**DONE:** Francisco ha revisado y aprobado la especificación; el archivo está guardado y el coach ha comprobado su existencia y correspondencia con lo aprobado. Las cuestiones abiertas están identificadas y no impiden por sí solas terminar esta fase.

**Siguiente:** cuando Francisco confirme que quiere continuar con el desglose, preparar `plan` en la misma conversación. Otra ruta requiere su decisión explícita y registro de las omisiones.
