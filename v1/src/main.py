import os
from dotenv import load_dotenv
from loguru import logger

load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))
logger.add("logs/v1_app.log", rotation="1 day", retention="1 week", compression="zip")

from gradio_interface import launch_interface
# Launch the interface
launch_interface()
