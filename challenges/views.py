from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


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

def home(request):
    list_items=""
    months=list(monthly_challenges.keys())
    
    for month in months:
        capitalized_month=month.capitalize()
        month_path = reverse("month-chall", args=[month])
        list_items += f"<h2><li><a href='{month_path}'>{capitalized_month}</a></li></h2>"

    response_data=f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)

def monthly_challenge_by_number(request, month):
    months=list(monthly_challenges.keys())
    if month>12:
        return HttpResponseNotFound("Invalid month")

    get_month = months[month - 1]
    redirect_month=reverse("month-chall", args=[get_month])
    return HttpResponseRedirect(redirect_month)

def monthly_challenge(request, month):
    try:
        challenge_text=monthly_challenges[month]
        return render(request,'challenges/challenge.html', 
                      {'text':challenge_text, 'month_name':month})
    except:
        return HttpResponseNotFound("Month not supported!")
    #return HttpResponse(challenge_text)