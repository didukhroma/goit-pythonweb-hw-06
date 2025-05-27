from dotenv import load_dotenv
from enum import Enum
import os

load_dotenv()

class CONFIG(Enum):
    DB_NAME = os.getenv("DB_NAME")
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_PORT = os.getenv("DB_PORT")
    DB_HOST = os.getenv("DB_HOST")


url_to_db = f"postgresql://{CONFIG.DB_USER.value}:{CONFIG.DB_PASSWORD.value}@{CONFIG.DB_HOST.value}:{CONFIG.DB_PORT.value}/{CONFIG.DB_NAME.value}"
