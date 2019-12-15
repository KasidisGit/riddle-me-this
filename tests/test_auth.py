import datetime
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from user.models import UserManager, User

class AuthTest(TestCase):
    """ Some tests of authentication using user.models """
    
    def setUp(self):
        """ set up database for testing setting features """

        self.em = User.objects.create(email='abc@gmail.com')
        self.n = User.objects.create(name="First Name")
    
    def test_user_default_scores(self):
        """ test default scores of users """

        self.assertEqual(self.em.all_score, self.n.all_score)
        self.em.all_score = 10
        self.assertGreater(self.em.all_score, self.n.all_score)

    def test_date_join_user_login(self):
        """ test date that user login to join the game """

        time = timezone.now()
        self.em.date_joined = time
        self.assertIs(self.em.was_published_recently(), True)
    
    def test_user_is_staff(self):
        """ test that user is staff or not """

        self.assertFalse(self.em.is_staff)
        self.em.is_staff = True
        self.assertTrue(self.em.is_staff)
    
    def test_user_login(self):
        """ test name when user login """

        self.assertEqual(self.em.name, None)
        self.em.name = "WhoisTester"
        self.assertEqual(self.em.name, "WhoisTester")
        self.assertEqual(self.n.name, "First Name")
        self.assertNotEqual(self.n.name, "firstname")
    
    def test_profile_image_user(self):
        """ test images that users use to be their profile"""

        self.assertEqual(self.n.profile_image, 'profile_image/user.png')
        self.assertNotEqual(self.n.profile_image, 'img/easy/1rainbow.png')
    
    def test_current_page(self):
        """ test the page while they are in at that time. """

        self.assertEqual(self.n.current_easy, 1)
        self.assertLess(self.em.current_medium, 6)
        self.assertLessEqual(self.em.current_hard, 15)
