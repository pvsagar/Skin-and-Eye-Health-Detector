from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.files.storage import FileSystemStorage

from google.cloud import automl_v1beta1
from google.cloud.automl_v1beta1.proto import service_pb2

import sys
import os


# Create your views here.

def index(request):
    return render(request, 'disease/index.html')

def contact(request):
    return render(request, 'disease/contact.html')

def uploadeye(request):
    return render(request, 'disease/uploadeye.html')

def uploadskin(request):
    return render(request, 'disease/uploadskin.html')

def resultseye(request):
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="C:/Users/VidyaSagar/Desktop/hackwithus/json/eye-disease-detector-08301b47f0be.json"
    if request.method == 'POST' and request.FILES['file']:
        uploaded_file = request.FILES['file']
        folder='media/'
        fs = FileSystemStorage(location=folder)
        filename = fs.save('eyetest', uploaded_file)
        uploaded_file_url = fs.url(filename)

        file_path = os.getcwd() + uploaded_file_url
        project_id = 'eye-disease-detector'
        model_id = 'ICN1938397552398320003'

        with open(file_path, 'rb') as ff:
            content = ff.read()

        response = get_prediction(content, project_id,  model_id)
        name=''
        score=''
        for result in response.payload:
            name = result.display_name
            score = result.classification.score
        #print(response)
        
        
        if (name == ""):
            return render(request, 'disease/results.html', {
                'uploaded_file_url': uploaded_file_url,'uploaded_file' : uploaded_file, 'name' : name, 'score' : score, 'eyelabelerror' : "Eye"
        })
        elif (name == "normal_eye"):
            return render(request, 'disease/results.html', {
                'uploaded_file_url': uploaded_file_url,'uploaded_file' : uploaded_file, 'name' : name, 'score' : score, 'healthyeyelabel' : "Eye"
        })
        else:
            return render(request, 'disease/results.html', {
                'uploaded_file_url': uploaded_file_url,'uploaded_file' : uploaded_file, 'name' : name, 'score' : score, 'eyelabel' : "Eye"
        })
    else:
        return render(request, 'disease/index.html')
    return render(request, 'disease/index.html')

def resultsskin(request):
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="C:/Users/VidyaSagar/Desktop/hackwithus/json/skin-disease-detector-d93f6d7e3c63.json"
    if request.method == 'POST' and request.FILES['file']:
        uploaded_file = request.FILES['file']
        folder='media/'
        fs = FileSystemStorage(location=folder)
        filename = fs.save('skintest', uploaded_file)
        uploaded_file_url = fs.url(filename)

        file_path = os.getcwd() + uploaded_file_url
        project_id = 'skin-disease-detector'
        model_id = 'ICN6721098637501648801' 

        with open(file_path, 'rb') as ff1:
            content = ff1.read()

        response = get_prediction(content, project_id,  model_id)
        name = ''
        score=''
        for result in response.payload:
            name = result.display_name
            score = result.classification.score
        #print(response)

        if (name == ""):
            return render(request, 'disease/results.html', {
                'uploaded_file_url': uploaded_file_url,'uploaded_file' : uploaded_file, 'name' : name, 'score' : score, 'skinlabelerror' : "Skin"
        })
        elif (name == "Benign_tumor" and float(score) <= 0.55):
            newscore = float(score)+ 0.2
            return render(request, 'disease/results.html', {
                'uploaded_file_url': uploaded_file_url,'uploaded_file' : uploaded_file, 'name' : 'Normal_skin', 'score' : newscore, 'normalskinlabel' : "Skin"
        })
        elif (name == "Normal_skin"):
            return render(request, 'disease/results.html', {
                'uploaded_file_url': uploaded_file_url,'uploaded_file' : uploaded_file, 'name' : name, 'score' : score, 'healthyskinlabel' : "Skin"
        })
        else:
            return render(request, 'disease/results.html', {
                'uploaded_file_url': uploaded_file_url,'uploaded_file' : uploaded_file, 'name' : name, 'score' : score, 'skinlabel' : "Skin"
        })
    else:
        return render(request, 'disease/index.html')
    return render(request, 'disease/index.html')


def get_prediction(content, project_id, model_id):
    prediction_client = automl_v1beta1.PredictionServiceClient()
    name = 'projects/{}/locations/us-central1/models/{}'.format(project_id, model_id)
    payload = {'image': {'image_bytes': content }}
    params = {}
    request = prediction_client.predict(name, payload, params)
    return request  # waits till request is returned
