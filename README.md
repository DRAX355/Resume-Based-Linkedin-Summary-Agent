# 🧠 Resume-Based LinkedIn Summary Agent

Generate professional LinkedIn posts from your resume — powered by **Agentic AI** using CrewAI, LangChain, and Qwen 32B.  
This project is my first exploration into **AI Agents**, and it’s deployed, open source, and ready to use!

---

## 🌐 Live Demo

▶️ Try it here: [resume-based-linkedin-summary-agent.onrender.com](https://resume-based-linkedin-summary-agent.onrender.com/)

---

## 📸 Overview

Upload a `.pdf` or `.docx` resume, and the app:
1. Extracts and parses your resume content
2. Sends it to an **AI agent** acting as a “LinkedIn Content Creator”
3. Returns a personalized, structured LinkedIn post based on your background

---

## 🚀 Tech Stack

| Component       | Tech Used                              |
|----------------|------------------------------------------|
| 🧠 LLM Backend   | Qwen 32B via Groq API                   |
| 🤖 AI Agent      | [CrewAI](https://docs.crewai.com/)      |
| 🧩 Prompt Chaining| [LangChain](https://www.langchain.com/)|
| 🧾 Resume Parsing| PyMuPDF, python-docx                   |
| 🌐 UI            | [Streamlit](https://streamlit.io/)      |
| 📦 Packaging     | Docker                                 |
| ☁️ Hosting       | Render                                 |

---

## 🛠️ Setup Instructions

### 1. Clone the repo

```
git clone https://github.com/DRAX355/Resume-Based-Linkedin-Summary-Agent.git
cd Resume-Based-Linkedin-Summary-Agent
```
### 2. Create a virtual environment
```
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```
### 3. Install dependencies
```
pip install -r requirements.txt
```
### 4. Add your API key
Create a .env file with your Groq API key:
```
GROQ_API_KEY=your_groq_api_key_here
```
🛑 Do not commit your .env file to GitHub.

### 🐳 Docker Deployment
Build the Docker image
```
docker build -t linkedin-agent-app .
```
Run the container
```
docker run --env-file .env -p 8501:8501 linkedin-agent-app
```
Then open: http://localhost:8501

### 🧠 About the Agent
The app uses a CrewAI agent called LinkedIn Content Creator, with the following behavior:

Reads and analyzes resume content

Summarizes it in a compelling, professional tone

Outputs a post without thoughts, reasoning, or explanation

### 📁 Project Structure
```
├── app.py                # Main Streamlit app
├── agents.py             # Defines AI agent and model
├── tasks.py              # Task logic for the agent
├── resume_parser.py      # PDF/DOCX parser
├── requirements.txt
├── Dockerfile
├── .gitignore
└── README.md
```
📌 Notes
This is my first Agentic AI project, and I plan to improve and expand it.

Future projects will include multi-agent collaboration, memory, and more complex logic flows.

🙋‍♂️ Author
Darshan CM
