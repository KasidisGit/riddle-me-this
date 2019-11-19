from .forms import UserForm,CustomUserForm
from .models import User
from django.shortcuts import render

def forms_view(request):
    form = CustomUserForm()
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid:
            User.objects.c
    context = {
        'form':form
    }
    return render(request, "user.html", context)