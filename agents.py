from openai_engine import chatgpt
from gemini_engine import gemini

def chat_agent(prompt, ctx):
    try:
        return gemini(prompt, ctx)
    except:
        return chatgpt(prompt, ctx)

def image_agent(prompt):
    return f"[IMAGE GENERATED]: {prompt}"

def video_agent(prompt):
    return f"[VIDEO GENERATED]: {prompt}"

def code_agent(prompt, ctx):
    return chatgpt(prompt, ctx + "\nYou are a senior software engineer.")
