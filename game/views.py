from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import *

def IndexView(request):
    # q = Question.objects.get(pk=1)
    return render(request,"main-menu.html")

def HowtoView(request):
    return render(request,"how-to-play.html")

def HardStage(request):
    user = request.user
    return render(request,"hard-stage.html",{
        "range_available": HardQuestion.objects.filter(id__lte=user.current_hard),
        "range_lock": HardQuestion.objects.filter(id__gte=user.current_hard+1),
    })

def MediumStage(request):
    user = request.user
    return render(request,"medium-stage.html",{
        "range_available": MediumQuestion.objects.filter(id__lte=user.current_medium),
        "range_lock": MediumQuestion.objects.filter(id__gte=user.current_medium+1),
    })

def EasyStage(request):
    user = request.user
    return render(request,"easy-stage.html",{
        "range_available": EasyQuestion.objects.filter(id__lte=user.current_easy),
        "range_lock": EasyQuestion.objects.filter(id__gte=user.current_easy+1),
    })

def HardPicture(request,question_id):
    question = HardQuestion.objects.get(pk=question_id)
    user = request.user
    if request.method == 'POST':
        if request.POST.get('textfield',None) == question.answer or request.POST.get('button') == question.answer:
            if user.current_hard > question_id:
                pass
            elif user.current_hard == question.id:
                user.current_hard += 1
                user.all_score += question.score
            elif user.current_hard < question.id:
                pass
            user.save()
    if question_id < 15:
        next_question = HardQuestion.objects.get(pk=question_id+1)
    else:
        next_question = HardQuestion.objects.get(pk=1)
    return render(request,"hard-question.html",{
        "question": question,
        "next_question": next_question,
        "ans_length": (len(question.answer)),
    })

def MediumPicture(request,question_id):
    question = MediumQuestion.objects.get(pk=question_id)
    user = request.user
    if request.method == 'POST':
        if request.POST.get('textfield',None) == question.answer or request.POST.get('button') == question.answer:
            if user.current_medium > question_id:
                pass
            elif user.current_medium == question.id:
                user.current_medium += 1
                user.all_score += question.score
            elif user.current_medium < question.id:
                pass
            user.save()
    if question_id < 20:
        next_question = MediumQuestion.objects.get(pk=question_id+1)
    else:
        next_question = MediumQuestion.objects.get(pk=1)
    return render(request,"medium-question.html",{
        "question": question,
        "next_question": next_question,
        "ans_length": (len(question.answer)),
    })

def EasyPicture(request,question_id):
    question = EasyQuestion.objects.get(pk=question_id)
    user = request.user
    if request.method == 'POST':
        if request.POST.get('textfield',None) == question.answer or request.POST.get('button') == question.answer:
            if user.current_easy > question_id:
                pass
            elif user.current_easy == question.id:
                user.current_easy += 1
                user.all_score += question.score
            elif user.current_easy < question.id:
                pass
            user.save()
    if question_id < 15:
        next_question = EasyQuestion.objects.get(pk=question_id+1)
    else:
        next_question = EasyQuestion.objects.get(pk=1)
    return render(request,"easy-question.html",{
        "question": question,
        "next_question": next_question,
        "ans_length": (len(question.answer)),
    })

#def HintClick(request):

        









