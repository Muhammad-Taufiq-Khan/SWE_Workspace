from django.shortcuts import render
from django.http import HttpResponse
from models import *
# Create your views here.


def upload(request):
    if request.method == 'POST':
        handle_uploaded_file(request.FILES['file'], str(request.FILES['file']))
        return HttpResponse("Successful")

    return HttpResponse("Failed")


def handle_uploaded_file(file, filename):
    for s in file.read().split(','):
        myobject = File(file=s)
        myobject.save()
