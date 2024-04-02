from django.http import HttpResponse
from django.shortcuts import render
import requests
# Create your views here.

def ping(currentURL):
    return requests.post(currentURL).status_code

def index(request):
    context = {"path":request.path}
    return render(request, 'index.html', context=context)