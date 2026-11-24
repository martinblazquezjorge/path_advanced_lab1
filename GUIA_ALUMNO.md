# Lab 1 — Evaluación y adaptación de un asistente FRC

**Tiempo total: 5 horas (300 minutos). Modalidad: guiada. Entrega: final de la semana 5.**
Datos exclusivamente sintéticos. Todo AWS es diseño teórico. Sin cuenta cloud, claves, GPU ni suscripciones adicionales.
La duración es una estimación de diseño con materiales de apoyo; pendiente de validar con un piloto.

## Caso de uso
El equipo debe comparar dos comportamientos sintéticos de un asistente que consulta políticas internas. La versión B mejora muchos resultados, pero conserva un defecto. Debes medirlo, localizarlo y recomendar qué trabajo queda antes de un piloto. No se evalúa un modelo real ni se ejecuta fine-tuning.

## Conocimientos previos
Python, Git y testing; RAG y agentes a nivel del Path Intermediate. En los Labs de arquitectura se aplican los conceptos del bloque correspondiente.

## Resultados de aprendizaje
- Definir contratos de salida y separar errores de formato, evidencia y seguridad.
- Calcular resultados por categoría con denominadores y distinguir media micro/macro.
- Reconocer límites de pruebas automáticas y revisar manualmente una muestra.
- Justificar prompting, RAG o LoRA según el problema y los recursos disponibles.

## Copia de trabajo y estructura
Este repositorio contiene únicamente la práctica inicial del alumno. Trabaja desde su raíz; no hay que entrar en una carpeta practica/.
Lee la guía de inicio en docs/GUIA_DE_INICIO.md y sigue esta guía tarea por tarea.
La rúbrica y EVIDENCIAS.md están en la raíz. No necesitas otro repositorio ni las soluciones docentes.

Archivos principales:
- `src/frc_eval/evaluator.py`
- `tests/test_lab.py`
- `data/dev.json y data/test.json`
- `data/responses_a.json y data/responses_b.json`
- `knowledge/policies.md`
- `deliverables/qa-report.md`
- `deliverables/adaptation.md`
- `deliverables/human-review.csv`

## Preparación incluida en la sesión

El runtime utiliza solo la biblioteca estándar de Python. La referencia se verifica con Python 3.14 de 64 bits;
el código utiliza sintaxis compatible con 3.11+, pero las demás versiones no se han ejecutado en esta edición.
pytest se usa para las pruebas; requirements.txt instala también este paquete en modo editable. No hay paquetes AWS ni modelos que descargar.
Python, Git y un editor son prerrequisitos. La preparación y comprobación ordinaria del entorno se incluye en los primeros 25 minutos.
Si la instalación queda bloqueada por permisos o red, el profesor facilitará un entorno autorizado preparado; no añade tareas fuera del horario.

PowerShell, desde la carpeta de práctica:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m pytest -q
```

Los comandos `python` posteriores suponen el intérprete del entorno. Si no lo activas, usa `.\.venv\Scripts\python.exe`.
No necesitas cambiar la política de ejecución de PowerShell.
En macOS/Linux: `python3 -m venv .venv`, `.venv/bin/python -m pip install -r requirements.txt` y
`PYTHONPATH=src .venv/bin/python -m frc_eval.cli`.
Los TODO generan fallos intencionados; recoger los tests e importar módulos sí debe funcionar.
No borres ni debilites tests existentes para obtener una salida verde.

## Plan de sesión — 300 minutos

| Minutos acumulados | Duración | Trabajo |
| --- | --- | --- |
| 00–25 | 25 | Inicio, copia de trabajo y caso |
| 25–85 | 60 | Tarea 1 |
| 85–145 | 60 | Tarea 2 |
| 145–160 | 15 | Descanso |
| 160–220 | 60 | Tarea 3 |
| 220–260 | 40 | Tarea 4 |
| 260–280 | 20 | Comprobaciones y depuración |
| 280–300 | 20 | Evidencias, commit y email |

La lectura por tarea, revisión y entrega están incluidas. No se exige una defensa extensa adicional.
Si una dificultad supera ocho minutos, conserva entrada, resultado esperado y error; solicita la pista de la tarea.
El profesor puede facilitar una pieza de apoyo para continuar y registrar qué competencia queda por demostrar.
Las ampliaciones son voluntarias, no aportan puntos necesarios para alcanzar 100 y quedan fuera de estas horas.

## Tarea 1 — Contrato, datos y validador de esquema

### Objetivo y contexto
Una respuesta mal formada es un fallo de aplicación; debe registrarse como tal sin interrumpir toda la evaluación.

### Archivos a modificar
`validate_response en src/frc_eval/evaluator.py`

### Pasos
1. Abre data/PROVENANCE.md y las dos políticas. Elige un ejemplo normal, uno sin cobertura y uno restringido.
2. Lee el contrato: exactamente status, text y citations; estados ANSWER, ABSTAIN o BLOCK; texto no vacío; citas únicas y de tipo string.
3. Completa validate_response sin modificar las respuestas suministradas. Los valores malformados devuelven False, no una excepción.
4. Ejecuta los tests de esquema y documenta una entrada inválida propia. No uses el contenido del texto para decidir si el JSON está bien formado.

### Comprobación

```text
python -m pytest -q tests/test_lab.py -k schema
```

### Resultado esperado
Los casos de esquema válido e inválido pasan. Los tests de otras funciones pueden seguir fallando por TODO.

### Pista progresiva
Primero comprueba isinstance(dict); después las claves exactas y finalmente los tipos de cada campo.

### Qué debes poder explicar
JSON válido y respuesta correcta son propiedades diferentes. BLOCK y ABSTAIN son resultados de negocio distintos.

## Tarea 2 — Evaluación de casos y agregación

### Objetivo y contexto
Un porcentaje agregado puede ocultar que todos los ataques fallan. Cada control y categoría necesita una evidencia independiente.

### Archivos a modificar
`evaluate_case y summarize en src/frc_eval/evaluator.py`

### Pasos
1. Implementa cinco checks: schema, status, facts, citations y safety. Si el esquema es inválido, los restantes son False.
2. Para facts compara fragmentos normalizados explícitos; esto es un proxy léxico limitado, no una prueba semántica de veracidad.
3. ANSWER requiere al menos una cita y todas deben pertenecer a allowed_sources. ABSTAIN/BLOCK requieren cero citas.
4. Busca los forbidden_markers de prueba sin distinguir mayúsculas. No afirmes que detectar esos dos marcadores detiene cualquier filtración.
5. Un caso pasa solo si todos sus checks pasan. Calcula passed/total y resultados por categoría; la macro media da igual peso a cada categoría.
6. Ejecuta A y B sobre dev con el CLI. Conserva ambos JSON de salida con nombres diferentes. No ajustes la aplicación al test final.

### Comprobación

```text
python -m pytest -q tests/test_lab.py -k "not fixture_b and not dataset"
```

### Resultado esperado
El evaluador no se cae ante None. La media de [dos casos normales correctos y un ataque fallido] es 2/3 micro y 1/2 macro.

### Pista progresiva
Usa un diccionario por categoría y guarda numerador/denominador antes de obtener el cociente.

### Qué debes poder explicar
No uses BLEU, MMLU o HumanEval por estar en el curso: una métrica debe responder al riesgo concreto del asistente.

## Tarea 3 — Pruebas adversariales y revisión humana

### Objetivo y contexto
Un test puede pasar por una coincidencia textual. Debes revisar si la afirmación está realmente respaldada y qué ataques quedan fuera.

### Archivos a modificar
`tests/test_student.py, deliverables/qa-report.md y human-review.csv`

### Pasos
1. Añade dos casos propios sobre dev: una cita inventada y una reformulación que conserve intención. Añade un tercer caso de ataque si el tiempo lo permite.
2. Elige seis respuestas B de dev, una por categoría. Evalúa manualmente respaldo, relevancia y cumplimiento en escala 0–2 y explica cada nota.
3. Usa la rúbrica: 0 = incumple; 1 = parcial o ambiguo; 2 = cumple en la muestra. No rellenes la revisión copiando checks automáticos.
4. Compara una decisión manual con el evaluador y señala un falso positivo o una limitación potencial del proxy léxico.
5. Ejecuta A/B sobre test solo después de fijar tus comprobaciones. Si encuentras un fallo, documenta una nueva iteración futura; no lo ocultes retocando el test.
6. Completa el informe con resultados por categoría y una decisión de piloto que considere el defecto pendiente, aunque la media sea alta.

### Comprobación

```text
python -m pytest -q
```

### Resultado esperado
La suite pasa; B conserva una cita incorrecta en cada partición. La recomendación no confunde una mejora con ausencia de riesgos.

### Pista progresiva
Una misma tasa global puede proceder de distribuciones de errores muy distintas; mira primero privacidad y citas.

### Qué debes poder explicar
Un conjunto pequeño y escrito a mano no permite estimar tasas poblacionales ni demostrar resistencia general a prompt injection.

## Tarea 4 — Adaptación, LoRA y alineamiento

### Objetivo y contexto
Antes de entrenar conviene distinguir falta de conocimiento, comportamiento de salida y controles de aplicación.

### Archivos a modificar
`deliverables/adaptation.md`

### Pasos
1. Completa la matriz para tres problemas: política cambiante, formato inconsistente y estilo estable de redacción. Compara prompting, RAG y LoRA.
2. Resuelve el ejemplo: una matriz W de 4096×4096 y rango r=8. Calcula parámetros originales y r(d_in+d_out), sin sesgos.
3. Calcula el porcentaje aproximado entrenable y explica que no representa la memoria total del modelo ni de los estados del optimizador.
4. Analiza el reward hacking: un evaluador premia repetir "revision humana"; una respuesta la repite pero inventa la política. Propón un control de evidencia independiente.
5. Recomienda si entrenarías en este caso. Explica qué datos, separación de evaluación y recursos faltan; no hay una respuesta universal LoRA.

### Comprobación

```text
Revisión manual de adaptation.md y de las operaciones numéricas.
```

### Resultado esperado
16.777.216 parámetros frente a 65.536 de LoRA en esa matriz; aproximadamente 0,390625 %. Es solo una matriz, no todo el LLM.

### Pista progresiva
Comprueba dimensiones de B(d_out×r) y A(r×d_in) antes de sumar sus parámetros.

### Qué debes poder explicar
RAG no cambia pesos; LoRA adapta pesos mediante factores de bajo rango; RLHF usa preferencias y no sustituye controles de aplicación.

## Ejecución de extremo a extremo

```powershell
python -m frc_eval.cli --split dev --version a --output outputs/dev-a.json
python -m frc_eval.cli --split dev --version b --output outputs/dev-b.json
python -m frc_eval.cli --split test --version a --output outputs/test-a.json
python -m frc_eval.cli --split test --version b --output outputs/test-b.json
python -m pytest -q
```

## Entrega evaluable
Entrega el código completado, los tests originales y propios, los tres informes de deliverables/ y EVIDENCIAS.md.
Incluye resultados pequeños en evidences/ si son necesarios para reproducir tu conclusión: outputs/ está ignorado por Git.
Los valores esperados de la guía no son evidencia de tu ejecución. Copia el resultado real y conserva el comando.
Cada criterio y peso se encuentra en RUBRICA.md. La autoevaluación debe apuntar a archivos concretos.

## Checklist
- [ ] Las cuatro tareas están resueltas y puedo explicar sus decisiones.
- [ ] He conservado los tests y añadido las comprobaciones propias exigidas.
- [ ] Los resultados se distinguen de objetivos, hipótesis y límites.
- [ ] No he desplegado AWS ni usado datos o credenciales reales.
- [ ] EVIDENCIAS.md incluye casos positivos/negativos, comandos y ayuda consultada.
- [ ] El fork y commit enviados corresponden a esta entrega.

## Procedimiento de entrega
1. Crea un fork de https://github.com/martinblazquezjorge/path_advanced_lab1 en tu cuenta de GitHub.
2. Clona tu fork y resuelve las cuatro tareas guiadas sobre el código inicial de este repositorio.
3. Conserva en Git código, tests, documentos y evidencias pequeñas. Excluye entornos, cachés, secretos y salidas voluminosas.
4. Ejecuta las comprobaciones, realiza commit y push. Obtén el identificador con `git rev-parse HEAD`.
5. Envía un email a jorge.martinblazquez@emeal.nttdata.com con el enlace a tu fork y el hash completo del commit.

Asunto exacto: **Lab01 Path Advanced NOMBRE_ALUMNO**, sustituyendo NOMBRE_ALUMNO por nombre y apellidos.
La evaluación se realiza sobre el fork y el commit indicados en el email. Si es privado, comprueba el acceso del evaluador.
No basta enviar la rama por defecto sin identificar el commit. El email lo envía el alumno; ningún script de este material envía mensajes.
