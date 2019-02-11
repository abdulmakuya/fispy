from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def event(request):
    return HttpResponse("<h1>List of events will be here</h1>")
