from django.shortcuts import render
from .question import Question
from .models import Character, populate_from_csv

# Create your views here.


def index(request):
    return render(request, "akinator/index.html")


def ask_question(request):
    if len(Character.objects.all()) == 0:
        populate_from_csv("akinator/data/comics-combined-data.csv")
        print("Populated database")
    q = Question("Is your character from Marvel?")
    return render(request, "akinator/question.html", context={"obj": q})
