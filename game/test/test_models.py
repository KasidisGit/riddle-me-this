from django.test import TestCase
from game.models import *
from django.urls import reverse

class QuestionModelTests(TestCase):

    @classmethod
    def setUpClass(cls):

        """ set up database for testing hard questions, medium questions and easy questions."""

        EasyQuestion.objects.create(answer="rainbow")
        EasyQuestion.objects.create(answer="facebook")
        MediumQuestion.objects.create(answer="combat")
        MediumQuestion.objects.create(answer="software")
        MediumQuestion.objects.create(answer="software")
        HardQuestion.objects.create(answer="tulip")
        HardQuestion.objects.create(answer="championship")
        EasyQuestion.objects.get(id=2)
        MediumQuestion.objects.get(id=1)
        HardQuestion.objects.get(id=1)
        EasyQuestion.objects.filter(id=1)
        MediumQuestion.objects.filter(id=2)
        HardQuestion.objects.filter(id=2)

        # for i in MediumQuestion.objects.all():
        #     print(i.id)

    def test_query_for_question(self):
        easy1_test = EasyQuestion.objects.get(id=1)
        self.assertEqual(easy1_test.answer,"rainbow")
        easy2_test = EasyQuestion.objects.get(answer="facebook")
        self.assertEqual(easy2_test.id, 2)
        medium_test = MediumQuestion.objects.filter(answer="software")
        self.assertEqual(medium_test[0].id,2)
        self.assertEqual(medium_test[1].id,3)
        hard_test = HardQuestion.objects.get(id=2)
        self.assertEqual(hard_test.answer, "championship")

    def test_less_than_max_length(self):
        pass
        
#     def test_equal_max_length(self):
#         pass

#     def test_more_than_max_length(self):
#         pass

    @classmethod
    def tearDownClass(cls):
        pass
