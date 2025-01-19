import os
from dotenv import load_dotenv
from fastapi.responses import HTMLResponse
import logging
from config import Config 
from json2html import *
import json
from error_logs import generate_log
from general import get_formatted_date

def get_events():
    try:
        if os.path.exists(Config.EVENTLOG_PATH):
            # Read the existing data
            with open(Config.EVENTLOG_PATH, 'r') as file:
                existing_data = json.load(file)
                if existing_data:
                    html_table = json2html.convert(json=existing_data)
                else:
                    html_table = "<p>No data available to display</p>"
                return HTMLResponse(content=html_table)
        else:
            existing_data = []

    except Exception as e:
            print(f"Error: {e}, {os.path.basename(__file__)}, {get_formatted_date()}")
            generate_log(f"Error: {e}, {os.path.basename(__file__)}, {get_formatted_date()}")
            return {"message": f"Error: {str(e)}"}
    

def log_event(timestamp: str, event_type: str, image_filename: str):
    try:
        new_event = {
            "timestamp": timestamp,
            "event_type": event_type,
            "image_filename": image_filename
        }
        
        if os.path.exists(Config.EVENTLOG_PATH):
            # Read the existing data
            with open(Config.EVENTLOG_PATH, 'r') as file:
                existing_data = json.load(file)
        else:
            # If file doesn't exist, start with an empty list
            existing_data = []

        # Append the new event to the existing data
        existing_data.append(new_event)

        # Write the updated data back to the file
        with open(Config.EVENTLOG_PATH, 'w') as file:
            json.dump(existing_data, file, indent=4)

        message=f"logs: {new_event}"
        #print(f"{message}: {get_formatted_date()}")
        generate_log(f"{message}, {os.path.basename(__file__)}, {get_formatted_date()}")
        
    except Exception as e:
        print(f"Error: {e}, {os.path.basename(__file__)}, {get_formatted_date()}")
        generate_log(f"Error: {e}, {os.path.basename(__file__)}, {get_formatted_date()}")
        



