import logging

from uvicorn.logging import DefaultFormatter

from app.core.config import settings

logger = logging.getLogger(settings.PROJECT_NAME)
logger.setLevel(logging.getLevelName(settings.LOGGING_LEVEL))

# Create a formatter
formatter = DefaultFormatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

# Create a console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.getLevelName(settings.LOGGING_LEVEL))
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)
