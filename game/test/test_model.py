from django.test import TestCase
from game.models import HardQuestion, MediumQuestion, EasyQuestion

class HardQuestionModelTests(TestCase):

    @classmethod
    def setUpClass(cls):
        HardQuestion.objects.create(image="cowboy.",answer="asdasd")

    def test_less_than_max_length(self):
        self.assertequal()

    def test_equal_max_length(self):

    def test_more_than_max_length(self):
        AssertionError


class MediumQuestionModelTests(TestCase):


class EasyQuestionModelTests(TestCase):