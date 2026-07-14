from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

UPLOAD_DIR = BASE_DIR / "uploads"
OUTPUT_DIR = BASE_DIR / "outputs"
LOG_DIR = BASE_DIR / "logs"

SUPPORTED_FORMATS = {
    ".pdf",
    ".docx",
    ".txt",
}

MAX_FILE_SIZE = 5 * 1024 * 1024