from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

# Create your views here.

def monthly_challenge(request, month):
    challenge_text=None
    if month == "january":
        challenge_text = "Workout regularly"
    elif month == "february":
        challenge_text = "Eat healthy food"
    elif month == "march":
        challenge_text = "wakeup early"
    else:
        return HttpResponseNotFound("This month is not supported")
    return HttpResponse(challenge_text)