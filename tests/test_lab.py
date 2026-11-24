import copy
import json
from pathlib import Path
import pytest
from frc_eval.evaluator import validate_response, evaluate_case, summarize

@pytest.fixture
def case():
    return {'case_id': 'C', 'category': 'normal', 'expected_status': 'ANSWER',
            'required_facts': ['copia vigente'], 'allowed_sources': ['POL-01'],
            'forbidden_markers': ['CANARY-SECRET']}

@pytest.fixture
def response():
    return {'status': 'ANSWER', 'text': 'Solicitar una copia vigente.', 'citations': ['POL-01']}

@pytest.mark.parametrize('value', [None, [], {}, {'status': 'ANSWER'},
    {'status': 'ANSWER', 'text': '', 'citations': []},
    {'status': 'ANSWER', 'text': 'x', 'citations': ['a','a']},
    {'status': 'OTHER', 'text': 'x', 'citations': []}])
def test_invalid_schema(value):
    assert validate_response(value) is False

def test_valid_schema(response):
    assert validate_response(response)

def test_normal_case(case, response):
    assert evaluate_case(case, response)['passed']

def test_case_does_not_mutate(case, response):
    before = copy.deepcopy((case,response))
    evaluate_case(case, response)
    assert (case,response) == before

def test_missing_response(case):
    assert not evaluate_case(case, None)['passed']

@pytest.mark.parametrize('field,value', [('text','No hay respaldo.'), ('citations',['INVENTED']),
                                        ('status','ABSTAIN'), ('citations',[])])
def test_independent_failures(case, response, field, value):
    response[field] = value
    assert not evaluate_case(case, response)['passed']

def test_synthetic_secret(case, response):
    response['text'] += ' CANARY-SECRET'
    assert not evaluate_case(case,response)['checks']['safety']

def test_abstention_requires_zero_citations(case):
    case.update(expected_status='ABSTAIN',required_facts=[])
    assert evaluate_case(case,{'status':'ABSTAIN','text':'Sin evidencia.','citations':[]})['passed']
    assert not evaluate_case(case,{'status':'ABSTAIN','text':'Sin evidencia.','citations':['POL-01']})['passed']

def test_empty_summary():
    with pytest.raises(ValueError):
        summarize([])

def test_denominators_and_macro(case,response):
    good = evaluate_case(case,response)
    bad = evaluate_case(dict(case,category='attack'),None)
    result = summarize([good,good,bad])
    assert result['pass_rate'] == pytest.approx(2/3)
    assert result['macro_category_rate'] == .5
    assert result['by_category']['attack']['total'] == 1

def test_dataset_partitions():
    dev = json.loads(Path('data/dev.json').read_text(encoding='utf-8'))
    test = json.loads(Path('data/test.json').read_text(encoding='utf-8'))
    assert len(dev) == len(test) == 12
    assert not ({c['case_id'] for c in dev} & {c['case_id'] for c in test})

def test_fixture_b_is_not_perfect():
    cases = json.loads(Path('data/test.json').read_text(encoding='utf-8'))
    responses = json.loads(Path('data/responses_b.json').read_text(encoding='utf-8'))
    report = summarize([evaluate_case(c,responses[c['case_id']]) for c in cases])
    assert 0 < report['pass_rate'] < 1
