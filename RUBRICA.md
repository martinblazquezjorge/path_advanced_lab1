# Rúbrica — Lab 1 — Evaluación y adaptación de un asistente FRC — 100 puntos

Puntuar cada subcriterio por su evidencia: todos sus puntos si cumple el descriptor; cero si no.
Una alternativa correcta puede obtener 100. No se puntúa coincidencia textual con la solución de referencia.
Primero sumar puntuación bruta; después aplicar el menor máximo crítico que corresponda, sin dobles restas.
90–100: dominio sólido; 70–89: objetivos logrados con mejoras; 50–69: parcial; <50: insuficiente.
Umbral docente recomendado: 70/100 y controles críticos subsanados.
Una suite verde o un validador sin errores no sustituyen revisar resultados y decisiones.

| Área | Máximo | Evidencia requerida |
| --- | --- | --- |
| Contrato y datos | 10 | El esquema rechaza tipos/claves inválidos sin caer; la procedencia y separación dev/test están documentadas. |
| Evaluador y métricas | 25 | Los cinco checks, numeradores/denominadores, casos vacíos y media macro son correctos y reproducibles. |
| Seguridad y robustez | 20 | Dos pruebas propias relevantes y análisis de fallos por categoría; no se oculta el defecto B. |
| Estrategia de adaptación | 15 | Matriz motivada, cálculo LoRA correcto, límites de recursos y análisis de reward hacking. |
| Revisión humana | 10 | Seis respuestas valoradas con motivos propios y contraste con los proxies automáticos. |
| Informe y decisión | 10 | Resultados localizables, recomendación coherente con controles críticos y límites del conjunto. |
| Reproducibilidad y entrega | 10 | Comandos, tests conservados, evidencia real y commit identificable. |

## Contrato y datos — 10 puntos

- **5 puntos:** El esquema rechaza tipos/claves inválidos sin caer; la procedencia y separación dev/test están documentadas.
- **5 puntos:** la entrega demuestra el criterio con un caso positivo y uno negativo o una alternativa comparada; sus resultados y límites están explicados y son localizables.

## Evaluador y métricas — 25 puntos

- **12 puntos:** Los cinco checks, numeradores/denominadores, casos vacíos y media macro son correctos y reproducibles.
- **13 puntos:** la entrega demuestra el criterio con un caso positivo y uno negativo o una alternativa comparada; sus resultados y límites están explicados y son localizables.

## Seguridad y robustez — 20 puntos

- **10 puntos:** Dos pruebas propias relevantes y análisis de fallos por categoría; no se oculta el defecto B.
- **10 puntos:** la entrega demuestra el criterio con un caso positivo y uno negativo o una alternativa comparada; sus resultados y límites están explicados y son localizables.

## Estrategia de adaptación — 15 puntos

- **7 puntos:** Matriz motivada, cálculo LoRA correcto, límites de recursos y análisis de reward hacking.
- **8 puntos:** la entrega demuestra el criterio con un caso positivo y uno negativo o una alternativa comparada; sus resultados y límites están explicados y son localizables.

## Revisión humana — 10 puntos

- **5 puntos:** Seis respuestas valoradas con motivos propios y contraste con los proxies automáticos.
- **5 puntos:** la entrega demuestra el criterio con un caso positivo y uno negativo o una alternativa comparada; sus resultados y límites están explicados y son localizables.

## Informe y decisión — 10 puntos

- **5 puntos:** Resultados localizables, recomendación coherente con controles críticos y límites del conjunto.
- **5 puntos:** la entrega demuestra el criterio con un caso positivo y uno negativo o una alternativa comparada; sus resultados y límites están explicados y son localizables.

## Reproducibilidad y entrega — 10 puntos

- **5 puntos:** Comandos, tests conservados, evidencia real y commit identificable.
- **5 puntos:** la entrega demuestra el criterio con un caso positivo y uno negativo o una alternativa comparada; sus resultados y límites están explicados y son localizables.

## Controles críticos

- Máximo 49 si la entrega presenta mediciones inventadas como ejecuciones reales, atribuye fixtures a inferencia real o altera los oráculos/tests para ocultar fallos.
- Máximo 49 si el diseño o implementación autoriza una acción material automática o permite que una caducidad equivalga a aprobación humana.
- Máximo 69 si falta evidencia verificable de una capacidad central exigida, aunque la documentación la mencione.
- Si aparecen datos reales sensibles o credenciales, solicitar su retirada y saneamiento antes de cerrar la evaluación; no hace falta usar ninguno.

El canario CANARY-SECRET es ficticio y está autorizado como dato de prueba. Que un caso adversarial falle puede ser un hallazgo correcto:
se evalúa detectarlo y tratarlo, no esconderlo. Una recomendación NO-GO bien sustentada puede alcanzar la máxima nota.
