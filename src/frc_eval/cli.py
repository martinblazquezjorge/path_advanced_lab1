"""Run frozen response evaluation, without calling a model."""
import argparse
import json
from pathlib import Path
from frc_eval.evaluator import evaluate_case, summarize

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--split', choices=['dev', 'test'], default='dev')
    p.add_argument('--version', choices=['a', 'b'], default='a')
    p.add_argument('--output', default='outputs/report.json')
    args = p.parse_args()
    cases = json.loads(Path(f'data/{args.split}.json').read_text(encoding='utf-8'))
    responses = json.loads(Path(f'data/responses_{args.version}.json').read_text(encoding='utf-8'))
    rows = [evaluate_case(case, responses.get(case['case_id'])) for case in cases]
    report = {'provenance': 'SYNTHETIC_FIXTURES_NO_MODEL_INFERENCE', 'split': args.split,
              'version': args.version, 'summary': summarize(rows), 'rows': rows}
    target = Path(args.output)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps(report['summary'], ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
