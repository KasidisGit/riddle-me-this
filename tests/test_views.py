from django.test import TestCase
from user.models import User
from django.utils import timezone
import datetime
from django.urls import reverse, reverse_lazy
from django.core.management import call_command
from django.contrib.auth import login
from game import views
from game.models import MediumQuestion


def create_user( email, days,current_e ,current_m ,current_h):
    time = timezone.now() + datetime.timedelta( days=days)
    return User.objects.create( email="test@gamil.com", date_joined =time, current_easy=current_e, current_medium=current_m, current_hard=current_h)


class UserViewTests(TestCase):

    def setUp(self):
        self.medium_url = reverse_lazy('game:e-picture',args=str(1))
        self.medium_url = reverse_lazy('game:m-picture',args=str(1))
        self.hard_url = reverse_lazy('game:m-picture',args=str(1))
        self.form_url = reverse('user:form')
        call_command('loaddata', 'user.json', verbosity=0)
        call_command('loaddata', 'social-auth.json', verbosity=0) 
        call_command('loaddata', 'game.json', verbosity=0)
        self.user = create_user('earnny13@gmail.com',1,1,1,1)

    def test_view_form(self):
        response = self.client.get(self.form_url)
        if self.user.is_authenticated:
            self.assertEqual(response.status_code, 200)


    def test_view_easy(self):
        response = self.client.get(self.form_url)
        if self.user.is_authenticated:
            self.assertEqual(response.status_code, 200)

    def test_view_medium(self):
        response = self.client.get(self.medium_url)
        if self.user.is_authenticated:
            self.assertEqual(response.status_code, 200)

    
    def test_view_hard(self):
        response = self.client.get(self.hard_url)
        if self.user.is_authenticated:
            self.assertEqual(response.status_code, 200)

