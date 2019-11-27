from django.views.generic import TemplateView
from django.shortcuts import render
from .forms import UserForm
from .models import User

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
            u.all_score = request.POST.get('all_score')
            # while u.all_score >0:
            if u.all_score >= 2:
                u.all_score -= 2;
                u.save()
            form = UserForm()

        args = {'form': form}
        return render(request, self.template_name , args)
    
    # def hintscore(self, request):
    #     u.all_score 