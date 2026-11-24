# Guía de inicio · Lab 1 Advanced

Este Lab te enseña a evaluar un asistente FRC con evidencias, no a llamar a una API. El punto de partida contiene respuestas sintéticas de dos versiones y tres funciones de evaluación pendientes. La guía principal organiza cuatro tareas dentro de cinco horas.

## 1. Localiza la carpeta de trabajo

Abre la terminal donde están README.md, pyproject.toml, requirements.txt, data/, src/ y tests/. Todas las rutas parten de esa carpeta. Trabaja en el clon de tu fork si vas a entregar. No necesitas otro repositorio ni una subcarpeta practica/.

## 2. Instala sin mezclar intérpretes

Python 3.14 de 64 bits es la referencia comprobada. Desde la raíz, en PowerShell:

```powershell
python -m venv .venv
..venvScriptspython.exe -m pip install -r requirements.txt
..venvScriptspython.exe -m pytest --collect-only -q
```

Se deben recoger 21 casos. La instalación editable permite importar `frc_eval` sin configurar PYTHONPATH. Si no activas el entorno, usa la ruta completa a su Python en todos los comandos. En macOS/Linux el intérprete es `.venv/bin/python`.

La instalación necesita conexión; la ejecución posterior es local. Si hay un bloqueo corporativo, solicita un entorno autorizado al profesor. La preparación ordinaria está dentro de los primeros 25 minutos; instalar Python/Git desde cero no forma parte del Lab.

## 3. Entiende la estructura

| Archivo | Responsabilidad |
|---|---|
| data/dev.json | Doce casos para desarrollar las comprobaciones |
| data/test.json | Doce casos para la evaluación final |
| data/responses_a.json y responses_b.json | Respuestas de entrada sintéticas de dos versiones |
| data/PROVENANCE.md | Procedencia y límites de los datos |
| knowledge/policies.md | Dos políticas internas sintéticas |
| src/frc_eval/evaluator.py | Las tres funciones que completarás y normalización proporcionada |
| src/frc_eval/cli.py | Lectura de archivos, selección y exportación ya implementadas |
| tests/test_lab.py | Contratos iniciales que deben conservarse |
| deliverables/ | Informe QA, adaptación y revisión humana |
| EVIDENCIAS.md | Resultados reales, decisiones y autoevaluación |

## 4. Conceptos del ejercicio

Un **caso** contiene una consulta y criterios de referencia. La **respuesta** es el dato que se evalúa. Los criterios no deben reescribirse para que coincidan con una respuesta errónea.

El **esquema** valida forma y tipos. Una respuesta puede tener el esquema correcto y aun así carecer de respaldo. **ANSWER**, **ABSTAIN** y **BLOCK** tienen significados diferentes: responder con evidencia, reconocer falta de evidencia y bloquear una petición fuera de los límites.

Una **cita** identifica una fuente permitida; su presencia no demuestra por sí sola que todo el texto esté respaldado. Los checks de fragmentos textuales son proxies léxicos: requieren contraste humano y una declaración de límites.

**Micro** da el mismo peso a cada caso; **macro por categoría** da el mismo peso a cada categoría. Cada tasa debe incluir su numerador y denominador. No uses una media global para ocultar fallos críticos.

La **revisión humana** puntúa seis respuestas de desarrollo con motivos propios. No consiste en copiar checks automáticos. **LoRA** se trabaja como análisis de adaptación y parámetros; no se entrena un modelo.

## 5. Lee una prueba y su fallo

```powershell
..venvScriptspython.exe -m pytest -q tests/test_lab.py -k schema
```

Un test prepara entradas, ejecuta código y comprueba una propiedad. Parametrizar permite evaluar varios valores con la misma función: por eso hay 21 casos aunque haya menos funciones de test.

`NotImplementedError` indica una función pendiente. Un error de importación indica entorno o instalación. Una aserción fallida señala diferencia de comportamiento. No son el mismo problema. No borres ni relajes tests para conseguir verde.

## 6. Trabaja por tareas

Sigue GUIA_ALUMNO.md: contrato de esquema; evaluación/agregación; seguridad y revisión humana; decisión de adaptación. Implementa solo los puntos pendientes y añade las dos pruebas propias exigidas. El CLI y la normalización ya están proporcionados.

Ejecuta sobre desarrollo antes de la evaluación final. Los dos conjuntos tienen IDs separados, pero comparten familias: no equivalen a una validación externa. No atribuyas las respuestas A/B a modelos reales ni sus tiempos a inferencia.

Si te bloqueas ocho minutos, conserva entrada, resultado esperado y primer error y pide una pista. Declara y verifica la ayuda recibida.

## 7. Errores habituales

| Síntoma | Qué comprobar |
|---|---|
| ModuleNotFoundError: frc_eval | Instala requirements.txt con el Python de .venv desde la raíz |
| No se encuentra data/dev.json | Ejecuta el CLI desde la carpeta del README |
| NotImplementedError | Sigue la tarea que completa esa función |
| Activate.ps1 está bloqueado | Usa directamente .venv/Scripts/python.exe |
| Los porcentajes parecen buenos, pero una categoría falla | Revisa resultados por riesgo y denominadores |
| El informe no aparece en GitHub | outputs/ se ignora; conserva evidencia pequeña en evidences/ |

## 8. Antes de entregar

Ejecuta la suite y las cuatro evaluaciones del README, conserva resultados reales y completa los tres entregables. Revisa la rúbrica. Haz commit/push en tu fork y envía por email su URL y hash exacto, con el asunto indicado en el README.

Continúa en la [guía del alumno](../GUIA_ALUMNO.md) y consulta la [rúbrica](../RUBRICA.md).
