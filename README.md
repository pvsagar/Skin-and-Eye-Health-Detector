Follow the below instructions to run the code.

# Requirements
1. Python 3.6 or later from https://www.python.org/downloads/ 
2. make sure you have pip installed
3. Open command prompt(Windows) or Terminal(Mac) navigate to the  enter 'pip install -r requirements.txt'


# Instructions
1. Download or clone the repository
2. Open command prompt(Windows) or Terminal(Mac) navigate to downloaded folder and enter 'pip install -r requirements.txt'
3. Navigate to the downloaded folder "hackwithus > json" and copy the filepaths for "eye-disease-detector-08301b47f0be.json" and "skin-disease-detector-d93f6d7e3c63" files.
4. Open views.py file in "hackwithus > disease" folder and provide above copied filepaths in os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="filepaths" in 'resultseye(request)' function and 'resultsskin(request)' functins respectively.
5. Run “python manage.py runserver” you will now have a local server at “http://127.0.0.1:8000/”
6. Open any web browser enter “http://127.0.0.1:8000/disease” and hit enter. You should see the home page of web application with welcome message.
7. You can test the model and check results.
8. if you are launching the model for the very first time, it may take some time to load.
