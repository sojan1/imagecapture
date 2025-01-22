import os
from dotenv import load_dotenv
import cv2
from config import Config 
from general import get_timestamp, log_message


def initialize_camera():
    #initialize camera
    camera = cv2.VideoCapture(0)
    if not camera.isOpened():
        raise RuntimeError("Unable to access the camera")
    return camera

def capture_frame(camera):
    #capture frame
    ret, frame = camera.read()
    if not ret:
        raise RuntimeError("Failed to capture an image")
    return frame

def save_image(frame, timestamp):
    #save image
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
        
        log_message(f"Image captured and saved, '{file_path}'")
        return file_name, timestamp, result
    except RuntimeError as e:
        log_message(f"Error: {e}")
    except Exception as e:
        log_message(f"Error: {e}")
    finally:
        camera.release()


    
        

