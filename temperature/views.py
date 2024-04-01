from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    context = {"Date":"2024-4-1", "name":"Ben Hays"}
    return render(request, 'temperature_structure.html',context=context)
