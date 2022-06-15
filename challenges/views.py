from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def january(request):
    return HttpResponse("Wake up early")

def february(request):
    return HttpResponse("exercise regularly")