from django.views.generic import TemplateView
from django.shortcuts import render,redirect
from .forms import UserForm
from .models import *
from django.template import RequestContext

class UserView(TemplateView):
    template_name = 'user.html'

    def get(self, request):
        form = UserForm()
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            u = User.objects.get(email = request.user)        
            u.name = request.POST.get('name')
            u.save()
            form = UserForm()

        args = {'form': form}
        return render(request, self.template_name , args)
