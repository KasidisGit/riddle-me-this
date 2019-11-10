from django.shortcuts import render
from django.views import generic
from django.utils import timezone
from .models import *

def IndexView(request):
    # q = Question.objects.get(pk=1)

    return render(request,"main-menu.html")
