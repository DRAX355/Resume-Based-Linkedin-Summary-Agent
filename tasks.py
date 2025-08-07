from crewai import Task

def create_linkedin_task(agent, resume_text):
    return Task(
        description=f"""You are a professional LinkedIn content creator. Based on the resume below, write a short, polished LinkedIn post (5–10 sentences) that showcases the user's professional achievements or skills.

Resume content:
---
{resume_text}
---

Output only the final LinkedIn post. Do NOT include explanations, thoughts, or assistant-like responses. Do NOT prefix with 'Thought:' or 'Here’s'. Only output the clean LinkedIn post. Do not output any reasoning or explanation.""",
        expected_output="A professional, post-ready LinkedIn summary with no extra explanation or reasoning.",
        agent=agent
    )
