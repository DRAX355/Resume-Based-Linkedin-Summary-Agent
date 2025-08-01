import streamlit as st
from dotenv import load_dotenv
from agents import linkedin_post_agent
from tasks import create_linkedin_task
from resume_parser import extract_resume_text
from crewai import Crew
import tempfile
import os

load_dotenv()

st.set_page_config(page_title="LinkedIn Post Generator", layout="centered")
st.title("📄 Resume ➡️ LinkedIn Post Generator")

uploaded_file = st.file_uploader("Upload your resume (.docx or .pdf)", type=["docx", "pdf"])

if uploaded_file:
    suffix = ".docx" if uploaded_file.name.endswith(".docx") else ".pdf"
    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        tmp.write(uploaded_file.read())
        tmp_path = tmp.name

    st.info(f"✅ {uploaded_file.name} uploaded successfully!")

    if st.button("Generate LinkedIn Post"):
        with st.spinner("Generating post..."):
            resume_text = extract_resume_text(tmp_path)
            st.text_area("🔍 Extracted Resume Text", resume_text, height=300)
            task = create_linkedin_task(linkedin_post_agent, resume_text)
            crew = Crew(agents=[linkedin_post_agent], tasks=[task])
            result = crew.kickoff()
            if isinstance(result, str) and result.lower().startswith("thought:"):
                result = ""  # Clean up garbage thoughts if no output



        st.success("Post generated!")
        st.markdown("### ✨ Your LinkedIn Post:")
        st.text_area("Copy & Paste:", value=result, height=200)

        os.remove(tmp_path)
