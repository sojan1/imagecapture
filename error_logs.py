import os
from dotenv import load_dotenv
import logging
from pythonjsonlogger import jsonlogger
from config import Config 


def generate_log(messagelog : str) :
    try:
        # Set up logging
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)

        if not logger.hasHandlers(): 
            # Create a handler to append to the file
            handler = logging.FileHandler(Config.ERRORLOG_PATH)

            # Create a JsonFormatter and set it to the handler
            formatter = jsonlogger.JsonFormatter()
            handler.setFormatter(formatter)

            # Add the handler to the logger
            logger.addHandler(handler)

        # Log an event
        logger.info(messagelog)
    except Exception as e:
        print(f"Error: {e}")











# import logging
# import json
# from datetime import datetime

# class JsonLoggingHandler(logging.Handler):
#     def emit(self, record):
#         log_entry = {
#             "timestamp": datetime.now().isoformat(),
#             "level": record.levelname,
#             "message": self.format(record)
#         }
#         with open("event_log.json", "a") as file:
#             file.write(json.dumps(log_entry) + "\n")

# # Set up logging
# logger = logging.getLogger()
# logger.setLevel(logging.INFO)

# # Add the custom JSON logging handler
# logger.addHandler(JsonLoggingHandler())

# # Log an event
# logger.info("This is a simple event logged")
