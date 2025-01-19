import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    IMAGE_PATH = os.getenv("IMAGE_PATH")
    IMAGE_NAME_SUFFIX = os.getenv("IMAGE_NAME_SUFFIX")
    EVENTLOG_PATH = os.getenv("EVENTLOG_PATH")
    ERRORLOG_PATH = os.getenv("ERRORLOG_PATH")
    
    
config = Config()