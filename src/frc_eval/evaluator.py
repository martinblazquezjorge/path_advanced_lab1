"""Checks of supplied structured responses; not a semantic truth oracle."""
from collections import defaultdict
import unicodedata

def normalized(text):
    return ' '.join(unicodedata.normalize('NFKC', text).casefold().split())

def validate_response(response):
    """Return False, not a crash, for malformed untrusted responses."""
    raise NotImplementedError("TODO schema")

def evaluate_case(case, response):
    """Evaluate explicit contracts, with independent, interpretable checks."""
    raise NotImplementedError("TODO evaluate")

def summarize(rows):
    """Rates always include their denominator; fail loudly on empty input."""
    raise NotImplementedError("TODO summarize")
