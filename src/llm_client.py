import json, os, urllib.request

def analyze_llm(log):
    key=os.getenv('LLM_API_KEY')
    if not key: raise RuntimeError('LLM_API_KEY is not set')
    base=os.getenv('LLM_BASE_URL','https://api.openai.com/v1').rstrip('/')
    model=os.getenv('LLM_MODEL','gpt-5-mini')
    prompt='Return ONLY JSON with problem, likely_cause, suggested_fix, confidence. Analyze this CI log:\n'+log
    body=json.dumps({'model':model,'messages':[{'role':'user','content':prompt}],'response_format':{'type':'json_object'}}).encode()
    req=urllib.request.Request(base+'/chat/completions',data=body,headers={'Authorization':'Bearer '+key,'Content-Type':'application/json'})
    with urllib.request.urlopen(req,timeout=30) as r: data=json.loads(r.read())
    return json.loads(data['choices'][0]['message']['content'])
