import logging
import os
from logging.handlers import RotatingFileHandler

# Ensure logs directory exists
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
log_dir = os.path.join(BASE_DIR, "logs")
os.makedirs(log_dir, exist_ok=True)

# File paths
risk_log_file = os.path.join(log_dir, "risk_score.log")
django_log_file = os.path.join(log_dir, "django.log")

# Formatter
formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

# === Risk Logger ===
risk_logger = logging.getLogger("risk_logger")
risk_logger.setLevel(logging.DEBUG)

if not risk_logger.handlers:
    # Rotating file handler (5 MB per file, keep 5 backups)
    file_handler = RotatingFileHandler(risk_log_file, maxBytes=5*1024*1024, backupCount=5)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(formatter)

    risk_logger.addHandler(file_handler)
    risk_logger.addHandler(console_handler)

# === Django Logger ===
django_logger = logging.getLogger("django_logger")
django_logger.setLevel(logging.INFO)

if not django_logger.handlers:
    file_handler = RotatingFileHandler(django_log_file, maxBytes=5*1024*1024, backupCount=5)
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)

    django_logger.addHandler(file_handler)
    django_logger.addHandler(console_handler)
