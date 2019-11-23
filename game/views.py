from django.shortcuts import get_object_or_404, render
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
    question = HardQuestion.objects.get(pk=question_id)
    if question_id < 15:
        next_question = HardQuestion.objects.get(pk=question_id+1)
    else:
        next_question = HardQuestion.objects.get(pk=1)
    return render(request,"hard-question.html",{
        "question": question,
        "next_question": next_question,
        'ans_length' : (len(Question.answer))
    })

def MediumPicture(request,question_id):
    question = MediumQuestion.objects.get(pk=question_id)
    if question_id < 20:
        next_question = MediumQuestion.objects.get(pk=question_id+1)
    else:
        next_question = MediumQuestion.objects.get(pk=1)
    return render(request,"medium-question.html",{
        "question": question,
        "next_question": next_question,
        'ans_length' : (len(Question.answer))
    })

def EasyPicture(request,question_id):
    question = EasyQuestion.objects.get(pk=question_id)
    if question_id < 15:
        next_question = EasyQuestion.objects.get(pk=question_id+1)
    else:
        next_question = EasyQuestion.objects.get(pk=1)
    return render(request,"easy-question.html",{
        "question": question,
        "next_question": next_question,
        "ans_length" : (len(Question.answer))
    })