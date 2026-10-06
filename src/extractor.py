import re
PAT=re.compile(r'error|failed|failure|exception|fatal|refused|timeout|not found|permission denied|cannot|unable',re.I)
def extract(text, context=1):
    lines=text.splitlines(); ids=set()
    for i,line in enumerate(lines):
        if PAT.search(line):
            ids.update(range(max(0,i-context),min(len(lines),i+context+1)))
    return '\n'.join(lines[i] for i in sorted(ids)) if ids else '\n'.join(lines[-80:])
