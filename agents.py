from crewai import Agent
from langchain.llms import OpenAI
from langchain_groq import ChatGroq as Groq
import os

llm = Groq(temperature=0.5, groq_api_key=os.getenv("GROQ_API_KEY"),model_name="groq/llama3-8b-8192")

linkedin_post_agent = Agent(
    role="LinkedIn Content Creator",
    goal="Write an engaging LinkedIn post based on a resume",
    backstory="An experienced social media copywriter who helps professionals highlight their achievements on LinkedIn.",
    verbose=True,
    llm=llm
)
