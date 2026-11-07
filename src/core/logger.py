from loguru import logger 
import sys

logger.remove()

logger.add(
    sys.stdout,
    colorize=True,
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
    level="INFO",
)

logger.add(
    "logs/app.log",
    rotation="10 MB",  # Rota cuando llega a 10MB
    retention="10 days",  # Conserva logs de los últimos 10 días
    compression="zip",  # Comprime logs viejos
    level="DEBUG",
    encoding="utf-8",
)