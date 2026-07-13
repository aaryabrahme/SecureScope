from pathlib import Path

# Supported file extensions
SUPPORTED_EXTENSIONS = {
    ".txt",
    ".csv",
    ".pdf",
    ".docx"
}


class FileScanner:
    """
    Responsible for discovering supported files
    inside a directory.
    """

    def __init__(self, root_directory: str):
        self.root_directory = Path(root_directory)

    def discover_files(self):
        """
        Recursively discover supported files.
        """

        discovered_files = []

        for file in self.root_directory.rglob("*"):

            if file.is_file() and file.suffix.lower() in SUPPORTED_EXTENSIONS:
                discovered_files.append(file)

        return discovered_files