import pdfplumber
from docx import Document
import tempfile

def extract_text(file):
    suffix = file.filename.split(".")[-1]

    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(file.file.read())
        path = tmp.name

    if suffix == "pdf":
        with pdfplumber.open(path) as pdf:
            return " ".join(p.extract_text() for p in pdf.pages)
    elif suffix == "docx":
        doc = Document(path)
        return "\n".join(p.text for p in doc.paragraphs)
