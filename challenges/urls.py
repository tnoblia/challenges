from django.urls import path
from . import views #Veut dire "accède à views depuis ce même dossier"

urlpatterns = [
    #Si on a une requête de type "january", exécute la fonction index fu fichier views.
    #path("january", views.january),
    #path("february", views.february),

    #I don't care about the concrete value. if I get anything, just pass the values from monthly_challenge
    #It's called dynamic path segment
    

    path("",views.index, name = 'index'), #/challenges/
    #path("<month>",views.monthly_challenge)
    #Even better thant this line, we have these two lines:
    path("<int:month>",views.monthly_challenge_by_number),
    #This means that we should pass an int for our month, if it's not an int then : 

    path("<str:month>",views.monthly_challenge, name= "month-base-challenge")
    #This means that we should pass a string for our month


    ]