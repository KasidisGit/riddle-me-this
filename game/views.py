from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.utils import timezone
from .models import HardQuestion,MediumQuestion,EasyQuestion
from django.shortcuts import render_to_response
from django.template import RequestContext

def handler404(request, exception,*args, **argv):
    response = render_to_response('400.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response


def handler500(request, *args, **argv):
    response = render_to_response('500.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response

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
    return render(request,"hard-question.html",{
        "question": Question,
        'n' : range(len(Question.answer))
    })

def MediumPicture(request,question_id):
    Question = MediumQuestion.objects.get(pk=question_id)
    return render(request,"medium-question.html",{
        "question": Question,
        'n' : range(len(Question.answer))
    })

def EasyPicture(request,question_id):
    Question = EasyQuestion.objects.get(pk=question_id)
    return render(request,"easy-question.html",{
        "question": Question,
        'n' : range(len(Question.answer))
    })

