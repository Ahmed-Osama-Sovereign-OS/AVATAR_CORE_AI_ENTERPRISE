from reasoning import think
from planner import plan
from orchestrator import route
from memory import remember, context

def brain(prompt):
    remember(prompt)
    reasoning = think(prompt)
    steps = plan(reasoning)
    ctx = context()
    return route(prompt, ctx)
