
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
   - **macOS/Linux:**
     ```bash
     source env/bin/activate
     ```

5. **Install Required Dependencies**
   If the environment is not set up, you can install the necessary extensions:
   ```bash
   pip install -r requirements.txt
   ```

6. **Reload the Server (if needed)**
   To reload the server (useful in case of changes):
   ```bash
   uvicorn index:app --reload
   ```

7. **Run the FastAPI Application**
   To start the FastAPI application, use the following command:
   ```bash
   fastapi dev index.py
   ```

8. **Run Unit Tests**
   To execute unit tests, run:
   ```bash
   python -m unittest discover -s . -p "test_*.py"
   ```

---

## Information on Online resources used 

Please refer to the `online_resources_usage.docx` file in captureimage folder.
