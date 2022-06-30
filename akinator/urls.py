from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("question/", views.ask_question, name="question"),
]
