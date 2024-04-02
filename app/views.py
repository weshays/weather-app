from django.http import HttpResponse
from django.shortcuts import render
import requests
from django.shortcuts import render

from .models import ModelF
from .forms import FormF

def index(request):
    return render(request, "index.html")

def retrieve(request):
    # dictionary for initial data with 
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    context["dataset"] = ModelF.objects.all()
         
    return render(request, "list_view.html", context)

def create(request):
    context ={}

    form = FormF(request.POST or None)
    if form.is_valid():
        form.save()
         
    context['form']= form
    return render(request, "index.html", context)