from pathlib import Path
import pandas as pd
import PyPDF2
from docx import Document

def read_txt(file_path: Path) -> str:
    """
    Read a text file and return its contents.
    """

    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def read_csv(file_path: Path) -> str:
    """
    Read a CSV file and convert it into text.
    """

    dataframe = pd.read_csv(file_path)

    return dataframe.to_string()


def read_pdf(file_path: Path) -> str:
    """
    Extract text from PDF files.
    """

    text = ""

    with open(file_path, "rb") as file:

        reader = PyPDF2.PdfReader(file)

        for page in reader.pages:
            text += page.extract_text() or ""

    return text

def read_docx(file_path: Path) -> str:
    """
    Extract text from a DOCX file.
    """

    document = Document(file_path)

    text = ""

    for paragraph in document.paragraphs:
        text += paragraph.text + "\n"

    return text

# Reader registry
READERS = {
    ".txt": read_txt,
    ".csv": read_csv,
    ".pdf": read_pdf,
    ".docx": read_docx
}

def read_file(file_path: Path) -> str:
    """
    Automatically select the correct reader
    based on file extension.
    """

    extension = file_path.suffix.lower()

    reader = READERS.get(extension)

    if reader:
        try:
            return reader(file_path)
        except Exception as error:
            print(f"Error reading {file_path.name}: {error}")
            return ""

    return ""