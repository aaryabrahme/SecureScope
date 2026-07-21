from pathlib import Path
from typing import Callable

import pandas as pd
import PyPDF2
from docx import Document

from logger import logger

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
    Extract text from a PDF file.
    """
    with open(file_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)

        pages = [
            page.extract_text() or ""
            for page in reader.pages
        ]

    return "".join(pages)


def read_docx(file_path: Path) -> str:
    """
    Extract text from a DOCX file.
    """
    document = Document(file_path)

    return "\n".join(
        paragraph.text
        for paragraph in document.paragraphs
    )


# -------------------------------------------------------------------
# Reader Registry
# -------------------------------------------------------------------

READERS: dict[str, Callable[[Path], str]] = {
    ".txt": read_txt,
    ".csv": read_csv,
    ".pdf": read_pdf,
    ".docx": read_docx,
}


def read_file(file_path: Path) -> str:
    """
    Read a file using the appropriate reader based on its extension.
    """

    extension = file_path.suffix.lower()

    reader = READERS.get(extension)

    if reader is None:
        logger.warning(
            "Unsupported file type: %s",
            extension
        )
        return ""

    try:
        return reader(file_path)

    except Exception as error:
        logger.error(
            "Failed to read '%s': %s",
            file_path.name,
            error
        )
        return ""
