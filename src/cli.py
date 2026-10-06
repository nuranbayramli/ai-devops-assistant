import argparse
from pathlib import Path
from .extractor import extract
from .analyzer import analyze
from .llm_client import analyze_llm

def main():
    p=argparse.ArgumentParser(description='Analyze failed CI/CD logs')
    p.add_argument('log_file',type=Path); p.add_argument('--llm',action='store_true')
    a=p.parse_args(); relevant=extract(a.log_file.read_text(errors='replace'))
    if a.llm:
        d=analyze_llm(relevant); problem=d['problem']; cause=d['likely_cause']; fix=d['suggested_fix']; conf=d.get('confidence','medium')
    else: problem,cause,fix,conf=analyze(relevant)
    print(f'Problem: {problem}\nLikely cause: {cause}\nSuggested fix: {fix}\nConfidence: {conf}')
if __name__=='__main__': main()
