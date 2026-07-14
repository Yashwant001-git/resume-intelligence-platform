import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path
from datetime import datetime


def setup_logger(name: str = "ResumePipeline") -> logging.Logger:
    """
    Creates a logger.
    Every program execution creates a new log folder.

    logs/
        YYYY-MM-DD_HH-MM-SS/
            app.log
    """

    logger = logging.getLogger(name)

    # Prevent duplicate handlers
    if logger.hasHandlers():
        return logger

    logger.setLevel(logging.INFO)

    # Create timestamp folder
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    log_dir = Path("logs") / timestamp
    log_dir.mkdir(parents=True, exist_ok=True)

    log_file = log_dir / "app.log"

    # Log Format
    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)-8s | %(filename)s:%(lineno)d | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # Console Handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # File Handler
    file_handler = RotatingFileHandler(
        filename=log_file,
        maxBytes=5 * 1024 * 1024,
        backupCount=3,
        encoding="utf-8",
    )
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    # logger.info("=" * 70)
    # logger.info("Application Started")
    # logger.info(f"Log Directory : {log_dir}")
    # logger.info("=" * 70)

    return logger


logger = setup_logger()