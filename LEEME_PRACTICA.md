# Qué debes completar — Lab 1 Advanced

Empieza por README.md y sigue GUIA_ALUMNO.md. Todo el material necesario está en este repositorio.

| Tarea | Código o entregable | Trabajo |
|---|---|---|
| 1 | src/frc_eval/evaluator.py: validate_response | Validar el esquema de respuestas, sin confundir formato y calidad |
| 2 | src/frc_eval/evaluator.py: evaluate_case y summarize | Comprobar cada caso y calcular métricas con denominadores |
| 3 | tests/test_student.py y deliverables/ | Añadir dos pruebas propias, revisar seis respuestas y redactar el informe QA |
| 4 | deliverables/adaptation.md | Comparar prompting/RAG/LoRA y analizar parámetros y reward hacking |

Hay tres funciones con NotImplementedError intencionado. normalized(), el CLI, los datos y los tests iniciales están proporcionados.
No hay que reescribir los componentes de apoyo ni entrenar o descargar un modelo.

## Entregables
- Código de las tres funciones y tests originales conservados.
- Al menos dos pruebas propias pertinentes en tests/test_student.py.
- deliverables/qa-report.md, deliverables/adaptation.md y deliverables/human-review.csv.
- EVIDENCIAS.md y evidencias pequeñas en evidences/ cuando hagan falta.

outputs/ está excluido de Git: conserva en evidences/ los resultados necesarios para justificar la entrega.
No edites los datos o los tests suministrados para mejorar resultados. Utiliza desarrollo antes de la evaluación final.
La guía y la rúbrica fijan los criterios. Tiempo total: cinco horas, incluida preparación ordinaria, descanso y entrega.
