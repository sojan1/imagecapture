#Create Enviornment
python -m venv env

#Activate
.\env\Scripts\activate


#if enviornment not set
	pip install opencv-python
	pip install python-json-logger
	pip install python-dotenv
	pip install "fastapi[standard]"
	pip install json2html
	pip install Jinja2
	
	
	uvicorn index:app --reload