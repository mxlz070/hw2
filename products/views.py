from django.shortcuts import render, HttpResponse
from datetime import datetime

# Create your views here.
def hello_view(request):
    if request.method == 'GET':
        return HttpResponse("Hello! Its my project")

def now_time_view(request):
    if request.method == "GET":
        date = datetime.now()
        return HttpResponse(f"{date}")

def goodbye_view(request):
    if request.method == "GET":
        return HttpResponse('Goodbye user !')
