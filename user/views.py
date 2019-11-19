from .forms import UserForm
from .models import User
from django.shortcuts import render

def forms_view(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'form':form
    }
    return render(request, "user.html", context)