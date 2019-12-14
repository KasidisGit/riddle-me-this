import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from django.contrib.auth.models import User
from django.test import Client


class TestPolls(unittest.TestCase):
    """
    IMPORTANT: loaddata polls.json to run test collectly
    """

    @classmethod
    def setUpClass(cls):
        user = User.objects.create_superuser(username='testuser',email='x@gamil.com',password='12345')
        user.save()


    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://127.0.0.1:8000/")
    

    def test_index_page(self):

        #check title page
        self.assertEqual('Polls app',self.driver.title)

        #check innerHTML of first polls
        ele = self.driver.find_element_by_tag_name('h1')
        self.assertEqual('Please <a href="/accounts/login/">login</a> to vote for a topic.',ele.get_attribute('innerHTML'))

        #check first polls
        a = self.driver.find_element_by_xpath('//ul//li//a')
        self.assertEqual('Solve : 200 - 10 * 10 - 10 * 10',a.get_attribute('innerHTML'))


    def test_to_question_detail(self):

        #to first polls
        a = self.driver.find_element_by_xpath('//ul//li//a')
        a.click()

        #find topic of poll
        ele = self.driver.find_element_by_tag_name('h1')
        self.assertEqual('Solve : 200 - 10 * 10 - 10 * 10',ele.get_attribute('innerHTML'))


    def tearDown(self):
        time.sleep(1)
        self.driver.close()

if __name__ == "__main__":
    unittest.main()