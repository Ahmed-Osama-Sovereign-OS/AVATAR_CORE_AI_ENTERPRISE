def check(prompt):
    blacklist=["hack","exploit","bypass"]
    return any(w in prompt.lower() for w in blacklist)
