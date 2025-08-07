import streamlit as st
from dotenv import load_dotenv
from agents import linkedin_post_agent
from tasks import create_linkedin_task
from resume_parser import extract_resume_text
from crewai import Crew
import tempfile
import os
import time

load_dotenv()

st.set_page_config(page_title="LinkedIn Post Generator", layout="centered")
st.title("📄Linkedin About Me Agent")

uploaded_file = st.file_uploader("Upload your resume (.docx or .pdf)", type=["docx", "pdf"])

import re

def clean_output(result):
    if isinstance(result, list):
        result = "\n\n".join(r.strip() for r in result if isinstance(r, str))

    if isinstance(result, str):
        result = result.strip()
        # Remove <think>...</think> blocks entirely
        result = re.sub(r"<think>.*?</think>", "", result, flags=re.DOTALL)
        # Remove any leftover assistant-y preambles
        for prefix in ["thought:", "sure,", "here’s", "let's"]:
            if result.lower().startswith(prefix):
                result = result.split(":", 1)[-1].strip()

    return result.strip()



def generate_post_with_retries(resume_text, retries=2):
    task = create_linkedin_task(linkedin_post_agent, resume_text)

    for attempt in range(retries):
        try:
            crew = Crew(
                agents=[linkedin_post_agent],
                tasks=[task],
                return_output=True
            )
            output = crew.kickoff()

            # ✅ Only use final_output (not full results with thoughts)
            if hasattr(output, "final_output"):
                result = output.final_output
            elif hasattr(output, "results"):
                result = output.results
            else:
                result = str(output)

            # Clean result
            if isinstance(result, list):
                result = "\n\n".join(r.strip() for r in result if isinstance(r, str))
            result = result.strip()

            if result:
                return result

        except Exception as e:
            print(f"[Attempt {attempt+1}] Error: {str(e)}")
            time.sleep(1)

    return "⚠️ Could not generate a valid LinkedIn post. Try uploading a different resume or click again."


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

            if not resume_text.strip():
                st.error("❌ No text found in resume. Please upload a richer resume.")
            else:
                result = generate_post_with_retries(resume_text)
                if result.startswith("⚠️"):
                    st.error(result)
                else:
                    st.success("Post generated!")
                    st.markdown("### ✨ Your LinkedIn Post:")
                    st.text_area("Copy & Paste:", value=result, height=200)

        os.remove(tmp_path)
