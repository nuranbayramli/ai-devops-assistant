from src.analyzer import analyze
from src.extractor import extract

def test_postgres(): assert analyze('connection refused postgres')[0]=='PostgreSQL connection failed'
def test_missing(): assert analyze("ModuleNotFoundError: No module named 'x'")[0]=='Python dependency is missing'
def test_extract(): assert 'ERROR' in extract('ok\nERROR connection refused\ncleanup')
