#from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def index(request):
    data = {
        "Name": "Nicole Peacock",
        "Track": "Backend(Python)",
        "Message": "Hello, world"
    }

    return JsonResponse(data)