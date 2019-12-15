# import unittest
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import time
# from user.models import User
# from django.test import Client


# class TestMainMenu(unittest.TestCase):

#     @classmethod
#     def setUpClass(cls):
#         user = User.objects.create_superuser(name='ktmook',email='x@gmail.com',password='12345')
#         user.save()


#     def setUp(self):
#         self.driver = webdriver.Chrome()
#         self.driver.get("http://127.0.0.1:8000/")
    

#     def test_index_page(self):

#         #check title page
#         self.assertEqual('Main Menu',self.driver.title)

#         #check innerHTML of first polls
#         ele = self.driver.find_element_by_tag_name('h1')
#         self.assertEqual('Riddle Me This',ele.get_attribute('innerHTML'))
#         # self.driver.find_element_by_css_selector('#easy').click()
#         self.driver.find_element_by_css_selector('#htp').click()
        
#     def tearDown(self):
#         time.sleep(1)
#         self.driver.close()

# class TestHowtoPlay(unittest.TestCase):

#     @classmethod
#     def setUpClass(cls):
#         user = User.objects.create_superuser(name='ktmook',email='x@gmail.com',password='12345')
#         user.save()


#     def setUp(self):
#         self.driver = webdriver.Chrome()
#         self.driver.get("http://127.0.0.1:8000/how-to-play")
    

#     def test_index_page(self):

#         #check title page
#         self.assertEqual('How to Play',self.driver.title)

#         #check innerHTML of first polls
#         ele = self.driver.find_element_by_tag_name('h1')
#         self.assertEqual('How to Play',ele.get_attribute('innerHTML'))
#         # self.driver.find_element_by_css_selector('#easy').click()
#         # self.driver.find_element_by_css_selector('#htp').click()
        
#     def tearDown(self):
#         time.sleep(1)
#         self.driver.close()


# if __name__ == "__main__":
#     unittest.main()

