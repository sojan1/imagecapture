import os
from dotenv import load_dotenv
from fastapi.responses import HTMLResponse
import logging
from config import Config 
from json2html import *
import json
from error_logs import generate_log
from general import get_formatted_date, read_json, write_json, log_message



def get_events():
    try:
        existing_data = read_json(Config.EVENTLOG_PATH)

        if existing_data:
            html_table = json2html.convert(json=existing_data)
        else:
            html_table = "<p>No data available to display</p>"

        return HTMLResponse(content=html_table)

    except Exception as e:
        error_message = f"Error retrieving events: {e}"
        log_message(error_message)
        return {"message": error_message}
    

def log_event(timestamp: str, event_type: str, image_filename: str):
    try:
        new_event = {
            "timestamp": timestamp,
            "event_type": event_type,
            "image_filename": image_filename
        }

        existing_data = read_json(Config.EVENTLOG_PATH)
        existing_data.append(new_event)
        write_json(Config.EVENTLOG_PATH, existing_data)

        log_message = f"Event logged: {new_event}"
        generate_log(f"{log_message}, {os.path.basename(__file__)}, {get_formatted_date()}")

    except Exception as e:
        error_message = f"Error logging event: {e}"
        log_message(error_message)
