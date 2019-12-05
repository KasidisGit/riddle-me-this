from django.shortcuts import render,redirect
from django.utils import timezone
from user.forms import UserForm
from user.models import User
from allauth.socialaccount.models import SocialAccount
from django.contrib.auth import login
from .models import *
from django.contrib.auth.models import User

def IndexView(request):
    form = UserForm()
    if request.method == "POST":
        form = UserForm(request.POST)
        player = User.objects.get(email= request.user)
        player.name = request.POST.get('name')
        player.save()
        form = UserForm()
        return redirect("game:index")
    if request.user.is_authenticated and request.user.name != 'guest':
        social_user = SocialAccount.objects.get(user=request.user)
        return render(request,"main-menu.html",{"social_user":social_user,"form":form})
    return render(request,"main-menu.html",{"form":form})

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
    key_give = question.answer
    if request.GET.get('hint-btn') == 'Hint':
        key = key_give[0]
        key_give = '0'
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
    return render(request,"hard_page.html",{
        "question": question,
        "next_question": next_question,
        "last_question": HardQuestion.objects.last(),
        "ans_length": (len(question.answer)),
        "key": key,
    })

# def MediumPicture(request,question_id):
#     user = request.user
#     Question = MediumQuestion.objects.get(pk=question_id)
#     if question_id < 20:
#         next_q = MediumQuestion.objects.get(pk=question_id+1)
#     else:
#         next_q = MediumQuestion.objects.get(pk=1)

#     if request.GET.get('hint-btn')== 'Hint':
#         if user.all_score >= 2:
#             user.all_score -= 2
#         else:
#             pass
#         user.save()

#     return render(request,"medium_page.html",{
#         "question": Question,
#         "question_id" : next_q,
#         'n' : range(len(Question.answer))
#     })

# def EasyPicture(request,question_id):
#     user = request.user
#     Question = EasyQuestion.objects.get(pk=question_id)
#     if question_id < 15:
#         next_q = EasyQuestion.objects.get(pk=question_id+1)
#     else:
#         next_q = EasyQuestion.objects.get(pk=1)
#     # print( request.POST.get('hint-btn'))
#     if request.GET.get('hint-btn')== 'Hint':
#         if user.all_score >= 2:
#             user.all_score -= 2
#         else:
#             pass
#         user.save()

#     return render(request,"easy_page.html",{
#         "question": Question,
#         "question_id" : next_q,
#         'n' : range(len(Question.answer))
#     })

# def hintforHard(request, question_id):
#     question = HardQuestion.objects.get(pk=question_id)
#     ans_q = question.answer
#     if request.method == 'POST':
#         for i in ans_q:
#             list_ans.append(i)
    
#     return render(request, "hard_page.html", {
#         "question_ans" : list_ans,
#     })
    

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
        "last_question": MediumQuestion.objects.last(),
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
        "last_question": EasyQuestion.objects.last(),
        "ans_length": (len(question.answer)),
    })

def create_guest(request):
    user = User.objects.filter(name='guest').order_by('id')
    new_user = User.objects.create(email=f'guest {len(user)+1}')
    new_user.save()
    login(request, new_user)
    return redirect("game:index")
