1. Go To VSCode powershell

2. Go To imagecapture folder

3. #Create Enviornment
    python -m venv env

4. #Activate
   .\env\Scripts\activate

5. #if enviornment not set (run the requirement.txt to install extensions)
	pip install -r requirements.txt

6. uvicorn index:app --reload 

7. run the command => fastapi dev index.py

For running unittest 
run the command => python -m unittest discover -s . -p "test_*.py"