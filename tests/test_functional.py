import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from user.models import User
from django.test import Client,TestCase
from django.urls import reverse
from allauth.socialaccount.models import SocialApp
from django.core.management import call_command

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

        # check innerHTML of main-menu.html
  
        #check innerHTML of main-menu.html
        ele = self.driver.find_element_by_tag_name('h1')
        self.assertEqual('Riddle Me This',ele.get_attribute('innerHTML'))

        self.driver.find_element_by_css_selector('#htp').click()

        ele = self.driver.find_element_by_tag_name('h1')
        self.assertEqual('How to Play',ele.get_attribute('innerHTML'))


    def test_button_play(self):

        btn_login = self.driver.find_element_by_id('btn-guest')
        btn_login.get_attribute('innerHTML')
        time.sleep(1)
        btn_login.click()

        button_play = self.driver.find_element_by_name('play_button')
        time.sleep(1)
        button_play.get_attribute('innerHTML')
        button_play.click()
        time.sleep(1)

        button_easy = self.driver.find_element_by_name('easy-stage')
        time.sleep(1)
        button_easy.get_attribute('innerHTML')
        button_easy.click()
        time.sleep(1)

        ele = self.driver.find_element_by_tag_name('h1')
        self.assertEqual('EASY',ele.get_attribute('innerHTML'))


    def test_how_to_play(self):
        """test button how to play and test how to play page."""  
        
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
        time.sleep(1)
        button_main_menu = self.driver.find_element_by_tag_name('a')
        time.sleep(1)
        button_main_menu.get_attribute('innerHTML')
        button_main_menu.click()
        ele = self.driver.find_element_by_tag_name('h1')
        self.assertEqual('Riddle Me This',ele.get_attribute('innerHTML'))

    def test_scoreboard(self):
        """test button scoreboard and test scoreboard page.""" 

        btn_login = self.driver.find_element_by_id('btn-guest')
        btn_login.get_attribute('innerHTML')
        time.sleep(1)
        btn_login.click()

        button_scoreboard = self.driver.find_element_by_name('scb_button')
        time.sleep(1)
        button_scoreboard.get_attribute('innerHTML')
        button_scoreboard.click()
        time.sleep(1)

        ele = self.driver.find_element_by_class_name('tracking-in-expand')
        self.assertIn('SCOREBOARD',ele.get_attribute('innerHTML'))
        ele = self.driver.find_element_by_name('haed-table-1')
        self.assertEqual('Picture',ele.get_attribute('innerHTML'))


    def tearDown(self):
        time.sleep(1)
        self.driver.close()


class TestStage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        user = User.objects.create_superuser(name='hanoey',email='abc@gmail.com',password='12345')
        user.save()


    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='C:\\Users\Admin\Downloads\chromedriver.exe')
        self.driver.get("http://127.0.0.1:8000/medium")

    def test_easy_stage(self):

        #login game
        self.driver.find_element_by_id('btn-guest').click()

        #check title page
        self.assertEqual('MEDIUM', self.driver.title)
  
        #check innerHTML of easy-stage.html
        ele = self.driver.find_element_by_tag_name('h1')
        self.assertEqual("MEDIUM", ele.get_attribute('innerHTML'))

        #can go to game page or not
        # ele  = self.driver.find_element_by_id('gopage')
        
        #from easy stage back to main menu
        tag = self.driver.find_element_by_tag_name('a')
        time.sleep(1)
        tag.get_attribute('innerHTML')
        tag.click()
        ele = self.driver.find_element_by_tag_name('h1')
        self.assertEqual('Riddle Me This',ele.get_attribute('innerHTML'))


    def tearDown(self):
        time.sleep(1)
        self.driver.close()
    
class TestGoogleAuth(TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='tests/chromedriver')
        self.driver.get("http://127.0.0.1:8000/")
        
    
    def test_change_name(self):

        #select login google button
        self.driver.find_element_by_css_selector('.g_btn').click()
        time.sleep(3)

        #fill up id
        ele = self.driver.find_element_by_id('identifierId')
        ele.click()
        ele.send_keys("hijimmybug@gmail.com")
        ele.send_keys(Keys.ENTER)
        time.sleep(1.5)

        #fill up password
        ele = self.driver.find_element_by_css_selector('.whsOnd.zHQkBf')
        time.sleep(1)
        ele.click()
        ele.send_keys('1qaz2wsx3edc4rfv5tgb6yhn7ujm')
        ele.send_keys(Keys.ENTER)
        time.sleep(1.5)

        #open sidnav and check google account name
        ele = self.driver.find_element_by_css_selector('#opennav.side_bar')
        ele.click()
        time.sleep(1)
        self.assertEqual('Welcome, hijimmybug ',ele.get_attribute('innerText'))

        #edit name
        ele = self.driver.find_element_by_id('edit-name')
        ele.click()
        time.sleep(1)
        ele = self.driver.find_element_by_id('id_name')
        ele.click()
        ele.send_keys("Hacker")
        ele.send_keys(Keys.ENTER)

        #check name was changed
        ele = self.driver.find_element_by_css_selector('#opennav.side_bar')
        ele.click()
        time.sleep(1)
        ele = self.driver.find_element_by_css_selector('.sidetext')
        self.assertEqual('Welcome, Hacker ',ele.get_attribute('innerText'))

    def tearDown(self):
        time.sleep(3)
        self.driver.close()

if User.objects.get(email='hijimmybug@gmail.com'):
    User.objects.get(email='hijimmybug@gmail.com').delete()
    
if __name__ == "__main__":
    unittest.main()

