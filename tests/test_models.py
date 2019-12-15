from django.test import TestCase
from game.models import *
from django.urls import reverse

class QuestionModelTests(TestCase):

    @classmethod
    def setUpClass(cls):
        """ 
        set up database for testing hard questions, medium questions and easy questions.
        """
        EasyQuestion.objects.create(answer="rainbow")
        EasyQuestion.objects.create(answer="facebook")
        MediumQuestion.objects.create(answer="combat")
        MediumQuestion.objects.create(answer="software")
        MediumQuestion.objects.create(answer="software")
        HardQuestion.objects.create(answer="tulip")
        HardQuestion.objects.create(answer="championship")

        # for i in MediumQuestion.objects.all():
        #     print(i.id)

    def test_query_for_easy_question(self):
        """
        test query set of easy questions
        """
        easy1_test = EasyQuestion.objects.get(id=1)
        self.assertEqual(easy1_test.answer,"rainbow")
        easy2_test = EasyQuestion.objects.get(answer="facebook")
        self.assertEqual(easy2_test.id, 2)

    def test_query_for_medium_question(self):
        """
        test query set of medium questions
        """
        medium_test = MediumQuestion.objects.filter(answer="software")
        self.assertEqual(medium_test[0].id,2)
        self.assertEqual(medium_test[1].id,3)
    
    def test_query_for_hard_question(self):
        """
        test query set of hard questions
        """
        hard_test = HardQuestion.objects.get(id=2)
        self.assertEqual(hard_test.answer, "championship")

    def test_for_add_latest_in_easy(self):
        """
        add answer at the latest position in query set of easy questions
        """
        easy_test = EasyQuestion.objects.create(answer="pillow")
        self.assertEqual(len(EasyQuestion.objects.all()), 3)
        self.assertEqual(EasyQuestion.objects.latest('id').answer, 'pillow')

    def test_for_delete_in_easy(self):
        """
        test for delete answer at any location in query set of easy questions
        """
        EasyQuestion.objects.get(answer="rainbow").delete()
        self.assertEqual(len(EasyQuestion.objects.all()),1)

    def test_for_insert_in_easy(self):
        """
        test for insert answer at any location in query set of medium questions
        """
        easy1_test = EasyQuestion(id=20,answer="watermelon")
        easy2_test = EasyQuestion(id=15,answer="carpet")
        easy1_test.save()
        easy2_test.save()
        self.assertEqual(len(EasyQuestion.objects.all()),4)

    def test_for_add_latest_in_medium(self):
        """
        add answer at the latest position in query set of medium questions
        """
        medium_test = MediumQuestion.objects.create(id=10, answer="billion")
        self.assertEqual(len(MediumQuestion.objects.all()), 4)
        self.assertEqual(MediumQuestion.objects.latest('id').answer, 'billion')
    
    def test_a_for_delete_in_medium(self):
        """
        test for delete answer at any location in query set of medium questions
        """
        MediumQuestion.objects.filter(id=2).delete()
        self.assertEqual(len(MediumQuestion.objects.all()),2)
    
    def test_for_insert_in_medium(self):
        """
        test for insert answer at any location in query set of medium questions
        """
        medium_test = MediumQuestion(id=5,answer="peasant")
        medium_test.save()
        self.assertEqual(len(MediumQuestion.objects.all()),4)

    def test_for_add_latest_in_hard(self):
        """
        add answer at the latest position in query set of hard questions
        """
        hard_test = HardQuestion.objects.create(answer="summary")
        self.assertEqual(len(HardQuestion.objects.all()), 3)
        self.assertEqual(HardQuestion.objects.latest('id').answer, 'summary')
    
    def test_a_for_delete_in_hard(self):
        """
        test for delete answer at any location in query set of hard questions
        """
        HardQuestion.objects.get(id=1).delete()
        self.assertEqual(len(HardQuestion.objects.all()),1)
    
    def test_for_insert_in_hard(self):
        """
        test for insert answer at any location in query set of hard questions
        """
        hard_test = HardQuestion(id=4,answer="sixty")
        hard_test.save()
        self.assertEqual(len(HardQuestion.objects.all()),3)

    @classmethod
    def tearDownClass(cls):
        pass