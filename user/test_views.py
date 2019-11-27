from django.test import TestCase
from .models import User
from django.utils import timezone
import datetime
from django.urls import reverse


def create_user( email, days):
    time = timezone.now() + datetime.timedelta( days = days)
    return User.objects.create( email="test@gamil.com", date_joined=time)


class UserViewTests(TestCase):

    def setUp(self):
        self.easy_url = reverse('game:easy')
        self.medium_url = reverse('game:medium')
        self.hard_url = reverse('game:hard')
        self.form_url = reverse('user:form')

    def test_view_form(self):
        response = self.client.get(self.form_url)
        self.assertEqual(response.status_code, 200)

    def test_view_easy(self):
        response = self.client.get(self.easy_url)
        self.assertEqual(response.status_code, 200)

    def test_view_medium(self):
        response = self.client.get(self.medium_url)
        self.assertEqual(response.status_code, 200)
    
    def test_view_hard(self):
        response = self.client.get(self.hard_url)
        self.assertEqual(response.status_code, 200)
