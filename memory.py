import json
FILE="memory.json"

def load():
    try:
        return json.load(open(FILE,"r",encoding="utf-8"))
    except:
        return {"facts":[]}

def save(mem):
    json.dump(mem, open(FILE,"w",encoding="utf-8"), indent=2, ensure_ascii=False)

def remember(text):
    mem=load()
    if text not in mem["facts"]:
        mem["facts"].append(text)
    save(mem)

def context():
    return str(load())
