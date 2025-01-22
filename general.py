import os
from dotenv import load_dotenv
from datetime import datetime
from error_logs import generate_log
import json

        
def read_json(file_path):
    try:
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                return json.load(file)
        return []
    except Exception as e:
        log_message(f"Failed to read file '{file_path}': {e}")
        raise

def write_json(file_path, data):
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        log_message(f"Failed to write file '{file_path}': {e}")
        raise

def get_timestamp() :
    try:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        return timestamp
    except Exception as e:
        log_message(f"Error: {e}")
        

def get_formatted_date() :
    try:
        timestamp = datetime.strptime(get_timestamp(), "%Y%m%d_%H%M%S")
        return timestamp
    except Exception as e:
        log_message(f"Error: {e}")

def log_message(message):
    print(message)
    generate_log(f"{message}, {os.path.basename(__file__)}, {get_formatted_date()}")


def print_test_comment_started(message):
    #print(f"\n----------------------------------------------------------------------")
    print(message)

def print_test_comment_completed(message):
    print(message)
    print(f"\n----------------------------------------------------------------------")