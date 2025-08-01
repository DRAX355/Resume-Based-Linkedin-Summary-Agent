from docx import Document
import fitz  # PyMuPDF

def extract_docx_text(docx_path):
    doc = Document(docx_path)
    return "\n".join([para.text for para in doc.paragraphs if para.text.strip() != ""])

def extract_pdf_text(pdf_path):
    text = ""
    with fitz.open(pdf_path) as doc:
        for page in doc:
            text += page.get_text("text")  # Try "text", "blocks", or "dict" if needed
    return text.strip()


def extract_resume_text(file_path):
    if file_path.endswith(".docx"):
        return extract_docx_text(file_path)
    elif file_path.endswith(".pdf"):
        return extract_pdf_text(file_path)
    else:
        raise ValueError("Unsupported file format. Only .docx and .pdf are allowed.")
