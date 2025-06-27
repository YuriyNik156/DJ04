from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    data = {
        'caption':'ZeroDjango'
    }
    return render(request, "main/index.html", data)

def new(request):
    return render(request, "main/new.html")



