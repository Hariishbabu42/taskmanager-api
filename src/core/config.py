import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    APP_NAME = os.getenv("APP_NAME", "TaskManager API")
    DEBUG = os.getenv("DEBUG", "True").lower() in ["true", "1", "yes"]
    DATABASE_URL = os.getenv("DATABASE_URL")


config = Config()