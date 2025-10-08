"""
Very basic logging example.
"""
import logging

# Configure logging once, typically in the main script
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

logger.info("This is an info message.")
logger.warning("This is a warning.")
logger.error("Something went wrong!")
