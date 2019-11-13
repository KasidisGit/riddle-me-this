from django.shortcuts import render
from django.views import generic
from django.utils import timezone
from .models import *

def IndexView(request):
    # q = Question.objects.get(pk=1)
    return render(request,"main-menu.html")

def LevelStage(request):
    return render(request,"stage.html",{
        "all_question":HardQuestion.objects.all()
    })

def QuestionDetail(request,question_id):
    return render(request,"hard_question.html",{
        "question":HardQuestion.objects.get(pk=question_id)
    })
