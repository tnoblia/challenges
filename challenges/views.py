from typing import NoReturn
from django.http.response import HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.
#Every view is a standalone funxtion

#def january(request):
#    return HttpResponse('Eat no meat for a month')


#def february(request):
#    return HttpResponse('Walk every day 20 minutes')

#def march(request):
#   return HttpResponse('Eat shit')

#def april(request):
#    return HttpResponse('Go fuck yourself')

monthly_challenges = {
    "january" : "Walk 5 kilometers every day",
    "february" : "Code every day",
    "march" : "Fight a turtle",
    "april" : "Make a gift to every member of your family",
    "may" : "Drink water every 2 hours",
    "june" : "Clean your room",
    "august": "10 push ups every day",
    "september" : "10 squats every day",
    "october" : "Learn chinese",
    "november" : "learn spanish",
    "december" : "Listen to a random 2022 american rapper's song every day without having your ears bleeding"
}

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())
    #Second lesson

    #First lesson
    #for month in months:
    #    capitalized_month = month.capitalize()
    #    month_path = reverse('month-base-challenge',args =[month] )
    #    list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"
    #    response_data = f"<ul>{list_items}</ul>"
    #return HttpResponse(list_items)
    return render(request,"challenges/index.html",{
            "months" : months
        })



#The monthly challenge function takes the <month> argument entered in urls.py from challenges.
def monthly_challenge(request, month):
    try:

        challenge_text= monthly_challenges[month]

        #First lesson
        #response_data = f"<h1>{challenge_text}</h1>"

        #Second lesson
        #response_data = render_to_string("challenges/challenge.html")
        #return HttpResponse(response_data)

        #THird lesson
        #We have to put request in first argument cause the render function
        #has to extract data from it.
        return render(request,"challenges/challenge.html",{
            "text" : challenge_text,
            "month_name": month
        })
        
    except :
        #FIRST LESSON
        ##Here we use render_to_string cause render can only give back
        #succesful responses
        #response_data = render_to_string('404.html')
        #return HttpResponseNotFound(response_data)

        raise Http404() #It's gonna automatically look for a 404.html file in the root


#We redirect the numbers to the string functions:
def monthly_challenge_by_number(request, month):
    if month >len(monthly_challenges) or month < 1:
        return HttpResponseNotFound('Invalid month')
    translated_month = list(monthly_challenges.keys())[month-1]
    redirect_path = reverse('month-base-challenge',args =[translated_month]) #/challenges/translated_month
    return HttpResponseRedirect(redirect_path)