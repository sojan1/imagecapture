from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Serve static files for images
app.mount("/images", StaticFiles(directory="IMAGE_PATH"), name="images")

@app.get("/")
async def display_images():
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Images</title>
    </head>
    <body>
        <h1>Images</h1>
        <img src="/images/20250119_162914_image.jpg" alt="Image 3" style="max-width: 300px; margin: 10px;">
        <a href="/images/20250119_162914_image.jpg" target="_blank">Image 1</a>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)
