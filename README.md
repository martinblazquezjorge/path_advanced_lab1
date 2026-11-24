# Path Advanced · Lab 1

**Evaluación y adaptación de un asistente FRC.** Material del alumno: guía, rúbrica de 0 a 100, datos sintéticos, tests y código inicial para completar. Duración prevista: **5 horas**, con preparación ordinaria, descanso y margen de depuración incluidos. Entrega: **final de la semana 5**.

## Empieza aquí

1. Lee la [guía de inicio](./docs/GUIA_DE_INICIO.md) ([Word](./docs/GUIA_DE_INICIO.docx)) para preparar el entorno y entender el flujo de evaluación.
2. Sigue la [guía del alumno](./GUIA_ALUMNO.md) ([Word](./GUIA_ALUMNO.docx)), tarea por tarea.
3. Consulta [qué debes completar](./LEEME_PRACTICA.md), la [rúbrica](./RUBRICA.md) ([Word](./RUBRICA.docx)) y la plantilla [EVIDENCIAS.md](./EVIDENCIAS.md).

## 1. Haz tu copia

Este repositorio público es el punto de partida común. Para entregar tu trabajo, pulsa **Fork** y clona el repositorio de tu cuenta. Sustituye `TU_USUARIO` por tu usuario de GitHub:

```powershell
git clone https://github.com/TU_USUARIO/path_advanced_lab1.git
cd path_advanced_lab1
```

Si solo quieres explorar el material sin entregar cambios:

```powershell
git clone https://github.com/martinblazquezjorge/path_advanced_lab1.git
cd path_advanced_lab1
```

También puedes usar **Code → Download ZIP** y extraerlo. La entrega evaluable debe estar en tu fork. No necesitas copiar archivos de otro Lab ni acceder al repositorio del profesor.

## 2. Prepara el entorno

La versión de referencia comprobada es **Python 3.14 de 64 bits**. El código declara compatibilidad con Python 3.11 o posterior; no se afirma haber ejecutado todas esas versiones. Python, Git y un editor son prerrequisitos del itinerario.

Desde la raíz del repositorio, en PowerShell:

```powershell
python --version
python -m venv .venv
..venvScriptspython.exe -m pip install -r requirements.txt
..venvScriptspython.exe -m pytest --collect-only -q
```

La última orden debe recoger **21 casos de prueba**. Usar la ruta del intérprete evita activar el entorno o cambiar políticas de ejecución. Si activas `.venv`, podrás usar `python ...` en las instrucciones restantes. En macOS/Linux:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m pytest --collect-only -q
```

`requirements.txt` instala el paquete local en modo editable y fija pytest mediante `constraints.txt`. La primera instalación necesita conexión. Después, la ejecución usa solo archivos locales: sin cuenta AWS, API keys, GPU, modelos descargados ni servicios de pago. Si la organización bloquea la instalación, solicita al docente el entorno autorizado preparado.

## 3. Entiende los fallos iniciales

**Al empezar, los tests no pasan todos.** Las tres funciones pendientes lanzan `NotImplementedError("TODO ...")`. Los fallos son intencionados: no borres ni debilites pruebas para ponerlas en verde.

| Archivo | Qué debes completar |
|---|---|
| `src/frc_eval/evaluator.py` | `validate_response`: contrato de salida |
| `src/frc_eval/evaluator.py` | `evaluate_case`: checks por caso |
| `src/frc_eval/evaluator.py` | `summarize`: resultados y denominadores |

La función de normalización, el CLI, el corpus y las respuestas de entrada están proporcionados. Además del código, completarás los informes y dos pruebas propias indicadas en la guía. No se incluyen soluciones docentes ni implementaciones completas de estas tres funciones.

```powershell
..venvScriptspython.exe -m pytest -q
```

Al terminar deben pasar los 21 casos iniciales y tus pruebas adicionales. Sigue las comprobaciones por tarea de la guía.

## 4. Ejecuta tu aplicación al terminar

```powershell
..venvScriptspython.exe -m frc_eval.cli --split dev --version a --output outputs/dev-a.json
..venvScriptspython.exe -m frc_eval.cli --split dev --version b --output outputs/dev-b.json
```

Primero trabaja con `dev`. Cuando hayas fijado las comprobaciones, ejecuta la evaluación final y conserva su resultado sin retocar los datos para mejorarlo:

```powershell
..venvScriptspython.exe -m frc_eval.cli --split test --version a --output outputs/test-a.json
..venvScriptspython.exe -m frc_eval.cli --split test --version b --output outputs/test-b.json
```

El CLI compara respuestas A/B sobre 12 casos por partición y genera un JSON con checks y métricas. Las seis categorías son normal, abstención, inyección, robustez, privacidad y citas. Antes de completar las funciones, la evaluación puede fallar por TODO; `--help` sí funciona.

Los casos y respuestas A/B son **fixtures sintéticos**, no resultados de inferencia ni dos modelos reales. Aquí se evalúan contratos sobre muestras fijadas, no la seguridad general o calidad productiva de un LLM. Consulta la [procedencia de los datos](./data/PROVENANCE.md).

## 5. Entrega y evaluación

Completa [EVIDENCIAS.md](./EVIDENCIAS.md) con comandos y resultados reales, casos positivos y negativos, dos decisiones explicadas, una limitación y la ayuda consultada. Usa la [rúbrica de 100 puntos](./RUBRICA.md) para autoevaluarte.

Sube a **tu fork**:

- Código completado, tests iniciales y al menos dos pruebas propias.
- [Informe QA](./deliverables/qa-report.md), [estrategia de adaptación](./deliverables/adaptation.md) y [revisión humana](./deliverables/human-review.csv).
- EVIDENCIAS.md y resultados pequeños en `evidences/`. `outputs/` se ignora: no dejes allí la única copia de una evidencia que necesite el evaluador.

```powershell
git add .
git commit -m "Completar Lab01 Path Advanced"
git push origin HEAD
git rev-parse HEAD
```

Envía un email a [jorge.martinblazquez@emeal.nttdata.com](mailto:jorge.martinblazquez@emeal.nttdata.com) con el enlace a tu fork y el **hash completo del commit** entregado.

Asunto: **Lab01 Path Advanced NOMBRE_ALUMNO**, sustituyendo `NOMBRE_ALUMNO` por nombre y apellidos. Se evalúa exactamente el fork y commit indicados; si el repositorio es privado, comprueba que el evaluador tiene acceso.

Excluye entornos virtuales, cachés, credenciales y datos reales; `.gitignore` ya contempla esos archivos. No se envía ningún email automáticamente.

Las cinco horas son una estimación docente pendiente de piloto, no una duración medida. Si llevas ocho minutos bloqueado, anota entrada, salida esperada y primer error, y solicita una pista. Puedes usar ayuda si compruebas y explicas el resultado. Un informe que recomienda NO-GO puede obtener la máxima nota si está bien sustentado.
