from django.test import TestCase
from user.models import User,UserManager
from django.utils import timezone
import datetime
from django.urls import reverse, reverse_lazy
from django.core.management import call_command
from django.contrib.auth import login
from game.views import EasyPicture, MediumPicture, HardPicture
from game.models import MediumQuestion, EasyQuestion, HardQuestion

def create_user( email, days,current_e ,current_m ,current_h):
    time = timezone.now() + datetime.timedelta( days=days)
    return User.objects.create( email="test@gamil.com", date_joined =time, current_easy=current_e, current_medium=current_m, current_hard=current_h)

class GameViewTests(TestCase):

    def setUp(self):
        self.easy_url = reverse_lazy('game:e-picture',args=str(1))
        self.medium_url = reverse_lazy('game:m-picture',args=str(1))
        self.hard_url = reverse_lazy('game:h-picture',args=str(1))
        self.form_url = reverse('user:form')
        call_command('loaddata', 'user.json', verbosity=0)
        call_command('loaddata', 'social-auth.json', verbosity=0) 
        call_command('loaddata', 'game.json', verbosity=0)
        self.user = create_user('earnny13@gmail.com',1,1,1,1)

    def test_view_form(self):
        """
        Test that form can be accessed when user authenticated
        """
        response = self.client.get(self.form_url)
        if self.user.is_authenticated:
            self.assertEqual(response.status_code, 200)

    def test_htp_and_scoreboard(self):
        """
        Test that how to play and scoreboard can be accessed
        """
        response1 = self.client.get(reverse('game:htp'))
        self.assertEqual(response1.status_code, 200)
        response2 = self.client.get(reverse('game:scoreboard'))
        self.assertEqual(response2.status_code, 200)

    def test_stage_pages(self):
        """
        Test that all stage can be accessed when user authenticated
        """
        self.client.force_login(self.user)
        easy_stage = self.client.get(reverse('game:easy'))
        self.assertEqual(easy_stage.status_code, 200)
        medium_stage = self.client.get(reverse('game:medium'))
        self.assertEqual(medium_stage.status_code, 200)
        hard_stage = self.client.get(reverse('game:hard'))
        self.assertEqual(hard_stage.status_code, 200)         

    def test_easy_questions(self):
        """
        Test that easy question and post method can be accessed when user authenticated
        """
        response = self.client.get(self.easy_url)
        if self.user.is_authenticated:
            self.assertEqual(response.status_code, 200)
        response_post = self.client.post("/easy/15")
        self.assertEqual(response_post.status_code, 200)

    def test_medium_questions(self):
        """
        Test that medium question and post method can be accessed when user authenticated
        """
        response = self.client.get(self.medium_url)
        if self.user.is_authenticated:
            self.assertEqual(response.status_code, 200)
        response_post = self.client.post("/medium/20")
        self.assertEqual(response_post.status_code, 200)

    def test_hard_questions(self):
        """
        Test that hard question and post method can be accessed when user authenticated
        """
        response = self.client.get(self.hard_url)
        if self.user.is_authenticated:
            self.assertEqual(response.status_code, 200)
        response_post = self.client.post("/hard/15")
        self.assertEqual(response_post.status_code, 200)