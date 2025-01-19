from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles 
import os
import json
from datetime import datetime
from event_logs import log_event,get_events
from capture_image import capture_image
from json2html import *
from config import Config


app = FastAPI()
templates = Jinja2Templates(directory='templates')
app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/images", StaticFiles(directory="IMAGE_PATH"), name="images")

templates.env.cache = {}  # Disable caching

@app.get("/load_events")
def load_events_route():
    return get_events()


@app.get("/capture_event")
def capture_image_route():
    try:
        file_path,timestamp,result= capture_image()

        if file_path:
            log_event(timestamp,"ImageCapture",file_path)
            return {"message": f"{result}"}
            #return {"message": f"Image saved as {file_path} at {datetime.strptime(timestamp, "%Y%m%d_%H%M%S")}"}
    except Exception as e:
            print(f"Error: {e}, ErrorFile: {os.path.basename(__file__)}")
            return {"message": f"Error: {str(e)}"}


@app.get("/", response_class=HTMLResponse)
def read_html(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})