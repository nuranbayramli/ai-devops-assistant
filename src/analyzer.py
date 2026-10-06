import re

def analyze(log):
    rules=[
      (r'connection refused|could not connect|postgres.*connection', ('PostgreSQL connection failed','Database unavailable/not ready or connection settings are wrong.','Verify host/port/DATABASE_URL and wait for DB health before tests.')),
      (r'modulenotfounderror|no module named', ('Python dependency is missing','A required package is not installed.','Add it to project dependencies and install dependencies before tests.')),
      (r'permission denied|eacces', ('Permission error','CI lacks permission to access or execute a resource.','Check ownership/permissions and executable bits.')),
      (r'timeout|timed out', ('Operation timed out','A service or operation exceeded its time limit.','Check service readiness/network before increasing the timeout.'))]
    for p,v in rules:
        if re.search(p,log,re.I): return (*v,'high')
    return ('Unclassified CI failure','No local rule matched confidently.','Inspect error lines or use --llm for richer analysis.','low')
