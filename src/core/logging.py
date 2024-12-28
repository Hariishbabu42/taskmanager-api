import logging
from logging.config import dictConfig

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        },
        "detailed": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(pathname)s:%(lineno)d - %(message)s",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "default",
        },
        "file": {
            "class": "logging.FileHandler",
            "formatter": "detailed",
            "filename": "app.log",
        },
    },
    "root": {
        "level": "INFO",
        "handlers": ["console", "file"],
    },
}

def setup_logging():
    dictConfig(LOGGING_CONFIG)

setup_logging()


logger = logging.getLogger("TaskManager")
logger.info("Logging has been configured.")
