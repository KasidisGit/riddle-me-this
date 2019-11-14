from django.shortcuts import render
from django.views import generic
from django.utils import timezone
from .models import Question

def MenuView(request):
    return render(request,"main-menu.html")

def HowtoView(request):
    return render(request,"how-to-play.html")
