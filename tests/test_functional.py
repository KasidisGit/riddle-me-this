import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from user.models import User
from django.test import Client


class TestMainMenu(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        user = User.objects.create_superuser(name='ktmook',email='x@gmail.com',password='12345')
        user.save()


    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='tests/chromedriver')
        self.driver.get("http://127.0.0.1:8000/")
    

    def test_index_page(self):

        #check title page
        self.assertEqual('Main Menu',self.driver.title)

        check innerHTML of main-menu.html
        ele = self.driver.find_element_by_tag_name('h1')
        self.assertEqual('Riddle Me This',ele.get_attribute('innerHTML'))


    def test_how_to_play(self):
        self.driver.find_element_by_css_selector('#htp').click()

        ele = self.driver.find_element_by_tag_name('h1')
        self.assertEqual('How to Play',ele.get_attribute('innerHTML'))

        ele = self.driver.find_element_by_id('Rules')
        self.assertEqual('Rules',ele.get_attribute('innerHTML'))

        ele = self.driver.find_element_by_id('cell1-1')
        self.assertEqual('Stage',ele.get_attribute('innerHTML'))

        dot_2 = self.driver.find_element_by_id('dot-2')
        dot_2.click()
        ele = self.driver.find_element_by_id('hpt-medium')
        self.assertEqual('Medium',ele.get_attribute('innerHTML'))
        ele = self.driver.find_element_by_id('ans-medium')
        self.assertEqual('Pea + C(l)ock = Peacock',ele.get_attribute('innerHTML'))

        button_main_menu = self.driver.find_element_by_tag_name('a')
        button_main_menu.click()
        ele = self.driver.find_element_by_tag_name('h1')
        self.assertEqual('Riddle Me This',ele.get_attribute('innerHTML'))

        
    def tearDown(self):
        time.sleep(2)
        self.driver.close()



if __name__ == "__main__":
    unittest.main()

