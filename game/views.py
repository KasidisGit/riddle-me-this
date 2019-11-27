from django.shortcuts import render
from django.views import generic
from django.utils import timezone
from .models import *

def IndexView(request):
    # q = Question.objects.get(pk=1)
    return render(request,"main-menu.html")

def HowtoView(request):
    return render(request,"how-to-play.html")

def HardStage(request):
    return render(request,"hard-stage.html",{
        "all_question": HardQuestion.objects.all(),
    })

def MediumStage(request):
    return render(request,"medium-stage.html",{
        "all_question": MediumQuestion.objects.all(),
    })

def EasyStage(request):
    return render(request,"easy-stage.html",{
        "all_question": EasyQuestion.objects.all(),
    })

def HardPicture(request,question_id):
    Question = HardQuestion.objects.get(pk=question_id)
    if question_id < 15:
        next_q = HardQuestion.objects.get(pk=question_id+1)
    else:
        next_q = HardQuestion.objects.get(pk=1)

    return render(request,"hard_page.html",{
        "question": Question,
        "question_id" : next_q,
        'n' : range(len(Question.answer))
    })

def MediumPicture(request,question_id): 
    Question = MediumQuestion.objects.get(pk=question_id)
    if question_id < 20:
        next_q = MediumQuestion.objects.get(pk=question_id+1)
    else:
        next_q = MediumQuestion.objects.get(pk=1)

    return render(request,"medium_page.html",{
        "question": Question,
        "question_id" : next_q,
        'n' : range(len(Question.answer))
    })

def EasyPicture(request,question_id):
    Question = EasyQuestion.objects.get(pk=question_id)
    if question_id < 15:
        next_q = EasyQuestion.objects.get(pk=question_id+1)
    else:
        next_q = EasyQuestion.objects.get(pk=1)
    
    return render(request,"easy_page.html",{
        "question": Question,
        "question_id" : next_q,
        'n' : range(len(Question.answer))
    })

