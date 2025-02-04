
# Project Setup & Instructions

Follow these steps to set up the environment and run the project on your local machine.

---

## Steps 

1. **Open VSCode PowerShell**
   - Open your terminal within VSCode.

2. **Navigate to the `imagecapture` folder**
   - Use the terminal to go to the folder where the project files are downloaded.

3. **Create the Python Environment**
   ```bash
   python -m venv env
   ```

4. **Activate the Virtual Environment**
   - **Windows:**
     ```bash
     .\env\Scripts\activate
     ```

5. **Install Required Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

6. **Reload the Server (if needed)**
   ```bash
   uvicorn index:app --reload
   ```

7. **Run the FastAPI Application**
   ```bash
   fastapi dev index.py
   ```
9. **Open the application in browser**
    - please type the application's local address in browser 
    - Get the address from powershell once the applicaiton starts running.
      eg: http://127.0.0.1:8000 

8. **Run Unit Tests**
   ```bash
   python -m unittest discover -s . -p "test_*.py"
   ```

---

## Information on online resources used 

Please refer to the `online_resources_usage.docx` file in captureimage folder.
