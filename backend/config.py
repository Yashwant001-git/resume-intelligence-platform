from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

UPLOAD_DIR = BASE_DIR / 'uploads'
UPLOAD_DIR.mkdir(exist_ok=True)
OUTPUT_DIR = BASE_DIR / 'outputs'
LOG_DIR = BASE_DIR / 'logs'

MAX_FILE_SIZE = 5*1024*1024

SUPPORTED_FORMATES = {
    '.pdf',
    '.docx',
    '.txt'
}

APP_NAME = 'Resume Intelligence Platform'

VERSION = '1.0.0'