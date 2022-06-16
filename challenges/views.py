from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render


monthly_challenges={
    "january":"Workout regularly",
    "february":"Eat healthy food",
    "march":"wakeup early",
    "april":"learn python",
    "may":"learn django",
    "june":"learn java",
    "july":"learn hibernate",
    "august":"learn html",
    "september":"learn keyboard",
    "october":"play games",
    "november":"drink green tea",
    "december":"jog daily"
}
# Create your views here.
def monthly_challenge_by_number(request, month):
    months=list(monthly_challenges.keys())
    if month>12:
        return HttpResponseNotFound("Invalid month")

    get_month = months[month - 1]
    return HttpResponseRedirect("/challenges/" + get_month)

def monthly_challenge(request, month):
    try:
        challenge_text=monthly_challenges[month]
    except:
        return HttpResponseNotFound("Month not supported!")
    return HttpResponse(challenge_text)