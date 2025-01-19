import os
from dotenv import load_dotenv
import cv2
from config import Config 
from datetime import datetime
from error_logs import generate_log
from general import get_timestamp, get_formatted_date


def initialize_camera():
    #Initialize the camera
    camera = cv2.VideoCapture(0)
    if not camera.isOpened():
        raise RuntimeError("Unable to access the camera")
    return camera

def capture_frame(camera):
    #Capture a frame from the camera
    ret, frame = camera.read()
    if not ret:
        raise RuntimeError("Failed to capture an image")
    return frame

def save_image(frame, timestamp):
    #Save the captured frame as an image
    file_name = f"{timestamp}{Config.IMAGE_NAME_SUFFIX}"
    file_path = f"{Config.IMAGE_PATH}{file_name}"
    result = cv2.imwrite(file_path, frame)
    return file_name, file_path, result

def capture_image():
    try:
        camera = initialize_camera()
        frame = capture_frame(camera)
        timestamp = get_timestamp()
        file_name, file_path, result = save_image(frame, timestamp)
        
        message = f"Image captured and saved, '{file_path}'"
        generate_log(f"{message}, {os.path.basename(__file__)}, {get_formatted_date()}")
        return file_name, timestamp, result
    except RuntimeError as e:
        print(f"Error: {e}, {os.path.basename(__file__)}, {get_formatted_date()}")
        generate_log(f"Error: {e}, {os.path.basename(__file__)}, {get_formatted_date()}")
    except Exception as e:
        print(f"Error: {e}, {os.path.basename(__file__)}, {get_formatted_date()}")
        generate_log(f"Error: {e}, {os.path.basename(__file__)}, {get_formatted_date()}")
    finally:
        camera.release()
 


# def capture_image() :
#     try:
#         # Open the camera
#         camera = cv2.VideoCapture(0)
#         # Check if the camera opened successfully
#         if not camera.isOpened():
#             raise RuntimeError("Unable to access the camera")
        
#         # Capture a single frame    
#         ret, frame = camera.read()

#         # Save the image
#         if not ret:
#             raise RuntimeError("Failed to capture an image")

#         timestamp = get_timestamp()
#         file_name = f"{timestamp}{Config.IMAGE_NAME_SUFFIX}"
#         file_path = f"{Config.IMAGE_PATH}{file_name}"

#         result = cv2.imwrite(file_path, frame) 
#         message=f"Image captured and saved, '{file_path}'"
#         #print(message)
#         generate_log(f"{message}, {os.path.basename(__file__)}, {get_formatted_date()}")
#         return file_name,timestamp,result
    
#     except RuntimeError as e:
#         print(f"Error: {e}, {os.path.basename(__file__)}, {get_formatted_date()}")
#         generate_log(f"Error: {e}, {os.path.basename(__file__)}, {get_formatted_date()}")

#     except Exception as e:
#         print(f"Error: {e}, {os.path.basename(__file__)}, {get_formatted_date()}")
#         generate_log(f"Error: {e}, {os.path.basename(__file__)}, {get_formatted_date()}")

#     finally:
#         #Release the camera
#         camera.release()
        

