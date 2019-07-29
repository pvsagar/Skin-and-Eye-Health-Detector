This is a full scale machine learning application which can be used to detect 4 different eye diseases and 8 different skin diseases. 

This is built using Google Cloud and Django

Follow instructions given below to run the code.

# Requirements
1. Python 3.6 or later from https://www.python.org/downloads/ 
2. make sure you have pip installed
3. Open command prompt(Windows) or Terminal(Mac) navigate to the  enter 'pip install -r requirements.txt'


# Instructions
1. Download or clone the repository
2. Open command prompt(Windows) or Terminal(Mac) navigate to downloaded folder and enter 'pip install -r requirements.txt'
3. Copy the JSON file paths into the os.environ functions to connect the appliaction with Google Cloud.
4. Run “python manage.py runserver” you will now have a local server at “http://127.0.0.1:8000/”
5. Open any web browser go to “http://127.0.0.1:8000/disease” 
6. You can test the model and check results.
7. if you are launching the model for the very first time, it may take some time to load.
