from agents import chat_agent, image_agent, video_agent, code_agent
from security import check

def route(prompt, ctx):
    if check(prompt):
        return "⚠️ تم إيقاف الطلب لأسباب أمنية"
    if "صورة" in prompt or "image" in prompt:
        return image_agent(prompt)
    if "فيديو" in prompt or "video" in prompt:
        return video_agent(prompt)
    if "كود" in prompt or "code" in prompt:
        return code_agent(prompt, ctx)
    return chat_agent(prompt, ctx)
