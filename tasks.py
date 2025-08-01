from crewai import Task

def create_linkedin_task(agent, resume_text):
    return Task(
        description=f"""You are an expert social media copywriter. Based on the following resume text, write a polished, professional LinkedIn post (5-10 sentences) suitable for announcing achievements or skills.

Resume content:
---
{resume_text}
---

Do not explain your reasoning. Just output the final LinkedIn post.""",
        expected_output="A LinkedIn-ready post only, no explanation or reasoning.",
        agent=agent
    )

