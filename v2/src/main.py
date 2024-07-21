from gradio_interface import demo
from loguru import logger
from dotenv import load_dotenv 
import os

load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))
logger.add("logs/v2_app.log", rotation="1 day", retention="1 week", compression="zip")

if __name__ == "__main__":
    demo.launch(share=True)
