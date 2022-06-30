from django.shortcuts import render
from .question import Question

# Create your views here.


def index(request):
    return render(request, "akinator/index.html")


def ask_question(request):
    q = Question("Is your character from Marvel?")
    return render(request, "akinator/question.html", context={"obj": q})
