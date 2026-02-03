import os, importlib

def load_plugins():
    plugins=[]
    for f in os.listdir():
        if f.startswith("plugin_") and f.endswith(".py"):
            plugins.append(importlib.import_module(f[:-3]))
    return plugins
