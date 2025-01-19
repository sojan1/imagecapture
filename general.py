import os
from dotenv import load_dotenv
from datetime import datetime
from error_logs import generate_log


def get_timestamp() :
    try:
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        return timestamp
    
    except Exception as e:
        generate_log(f"Error: {e}, ErrorFile: {os.path.basename(__file__)}")
        print(f"Error: {e}, ErrorFile: {os.path.basename(__file__)}")
        

def get_formatted_date() :
    try:
        
        timestamp = datetime.strptime(get_timestamp(), "%Y%m%d_%H%M%S")
        return timestamp
    
    except Exception as e:
        generate_log(f"Error: {e}, ErrorFile: {os.path.basename(__file__)}")
        print(f"Error: {e}, ErrorFile: {os.path.basename(__file__)}")
        