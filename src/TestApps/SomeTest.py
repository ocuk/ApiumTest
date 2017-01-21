#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
from time import sleep
import unittest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from matplotlib.widgets import Widget
from selenium.webdriver.common.keys import Keys
from wheel.signatures import assertTrue

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class SimpleAndroidTests(unittest.TestCase):
    
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.3'
        desired_caps['deviceName'] = 'Nexus4-3_18'
        desired_caps['app'] = PATH(
            '../../../../testAPK/twitter.apk'
        )

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        # end the session
        self.driver.quit()
        
#     def test_login(self):
#               
#         # 
#         self.assertTrue(self.driver.is_app_installed('com.twitter.android'))
#               
#         # 
#         login = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "com.twitter.android:id/log_in")))
#         self.assertIsNotNone(login)
#         login.click()
#         sleep(5)
#               
#         # 
#         email = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "com.twitter.android:id/login_identifier")))
#         self.assertIsNotNone(email, 'no email entry')
#         email.clear()
#         email.send_keys("overkholyak")
#         sleep(1)
#               
#         # 
#         passw = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "com.twitter.android:id/login_password")))
#         self.assertIsNotNone(passw, 'no password entry')
#         passw.clear()
#         passw.send_keys('urm4ffe68d')
#         sleep(1)
#               
#         # 
#         submit = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "com.twitter.android:id/login_login")))
#         self.assertIsNotNone(login, 'no login button')
#         submit.click()
#               
#         refuse = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "android:id/button2")))
#         self.assertIsNotNone(refuse, 'no dialog box after login')
#         refuse.click()
#               
#         menu = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "com.twitter.android:id/drawer_icon")))
#         self.assertIsNotNone(menu, 'no menu')
#         menu.click()
#               
#         name = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "com.twitter.android:id/name")))
#         self.assertEqual(u'Oxana Verkholyak', name.text)

    def test_twit(self): 
        #         
        location = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "android:id/button1")))
        location.click()
         
        twit = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "com.twitter.android:id/composer_write")))
        twit.click()
         
        poll = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "com.twitter.android:id/poll")))
        poll.click()
         
        question = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "com.twitter.android:id/tweet_text")))
        question.send_keys("To be or not to be?")
         
        choice1 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//android.widget.EditText[@text='Choice 1']")))
        choice1.send_keys("Yes")
        symbols = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//android.widget.TextView[@text='22']")))
        self.assertIsNotNone(symbols)
         
        choice2 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//android.widget.EditText[@text='Choice 2']")))
        choice2.send_keys("No")
        symbols = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//android.widget.TextView[@text='23']")))
        self.assertIsNotNone(symbols)
         
        add = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "com.twitter.android:id/poll_card_add_choice")))
        add.click()
         
        choice3 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//android.widget.EditText[@text='Choice 3 (optional)']")))
        choice3.send_keys("That's the question!")
        symbols = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//android.widget.TextView[@text='5']")))
        self.assertIsNotNone(symbols)
         
        question = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "com.twitter.android:id/tweet_text")))
        question.send_keys("To be or not to be?")
         
        sleep(2)
         
        tweet_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "com.twitter.android:id/composer_post")))
        tweet_button.click()
         
        sleep(2)
         
        up = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "com.twitter.android:id/up_button")))
        up.click()
         
        button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "android:id/button2")))
        button.click()
         
        twit = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "com.twitter.android:id/composer_write")))
        twit.click()
            
        text_box = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "com.twitter.android:id/tweet_text")))
        self.assertIsNotNone(text_box)
        sleep(2)
         
        text_box.clear()
        text_box.send_keys('?')
        sleep(2)
        tweet_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@text='Tweet']")))
                    
        self.assertTrue(tweet_button.is_active) 
        
        
        
#     def test_subscribe(self):
#         
#         location = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "android:id/button1")))
#         location.click()
#         
#         # проверить кол-во текущих подписчиков
#         menu = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "com.twitter.android:id/drawer_icon")))
#         menu.click()
#          
#         profile = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//android.widget.TextView[@text='Profile']")))
#         profile.click()
#          
#         sleep(2)
#          
#         numbers = self.driver.find_elements_by_id('com.twitter.android:id/value')
#         number_followers = numbers[0].text
#                 
#         self.driver.back()
#         
#         # Найти нового подписчика         
#         menu = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "com.twitter.android:id/drawer_icon")))
#         menu.click()
#           
#         connect = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//android.widget.TextView[@text='Connect']")))
#         connect.click()
#           
#         search = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "com.twitter.android:id/toolbar_search")))
#         search.click()
#           
#         person = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//android.widget.EditText[@text='Search for people']")))
#         new_subscriber = 'Donald'
#         new_tag = "follow @realDonaldTrump"
#         person.send_keys(new_subscriber + "\n")
#         sleep(2)
#         
#         # Подписаться  
#         follow_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, new_tag)))
#         self.assertIsNotNone(follow_button)
#         follow_button.click()
#         sleep(5)
#            
#         self.driver.back()
#         self.driver.back()
#           
#         # Проверить список подписчиков
#         menu = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "com.twitter.android:id/drawer_icon")))
#         menu.click()
#           
#         profile = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//android.widget.TextView[@text='Profile']")))
#         profile.click()
#           
#         following = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//android.widget.TextView[@text='FOLLOWING']")))
#         following.click()
#           
#         sleep(5)
#          
#         # Найти всех текущих подписчиков 
#         followers = self.driver.find_elements_by_id('com.twitter.android:id/name_item')
#         self.assertGreater(len(followers), number_followers, 'Number of followers did not increase')    # Кол-во подписчиков должно увеличиься на 1
#          
#         names = []
#         for i in range(len(followers)):
#             names.append(followers[i].text)
#              
#         # Проверить, что новый подписчик в списке текущих
#         assert(new_subscriber in names)
        
        
#     def test_remove_account(self):
#            
#         # press home button
#         self.driver.press_keycode(3)
#            
#         settings = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//android.widget.TextView[@text='Settings']")))
#         self.assertIsNotNone(settings, 'no settings')
#         sleep(2)
#         settings.click()
#         sleep(5)
#            
#         # find all options
#         els = self.driver.find_elements_by_id("android:id/title")
#         self.assertGreaterEqual(len(els), 5)
#         self.driver.scroll(els[len(els)-1], els[0])
#         els = self.driver.find_elements_by_id("android:id/title")
#         self.assertGreaterEqual(len(els), 5)
#           
#         # find twitter in the options
#         twitter = None
#         for el in els:
#             if el.text == 'Twitter':
#                 twitter = el
#                   
#         self.assertIsNotNone(twitter, 'no twitter')
#         twitter.click()
#           
#         # click menu               
#         menu = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "android.widget.ImageButton")))
#         self.assertIsNotNone(menu, 'no menu in twitter account')
#         menu.click()
#             
#         # choose to remove the account
#         rm = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//android.widget.TextView[@text='Remove account']")))
#         self.assertIsNotNone(rm, 'no remove option')
#         rm.click()
#             
#         # confirm
#         button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@text='Remove account']")))
#         self.assertIsNotNone(rm, 'no remove button')
#         button.click()
#           
#         # confirm twitter is not in the list         
#         for el in els:
#             if el.text == 'Twitter':
#                 tw = el
#             else:
#                 tw = None
#                   
#         self.assertIsNone(tw, 'twitter not removed')
        
#     def test_add_widget(self):
#          
#         driver = self.driver
#         driver.press_keycode(3) 
#         sleep(2)
#          
#      
#         apps = driver.find_element_by_android_uiautomator('new UiSelector().description("Apps")')
#         apps.click()
#         sleep(5)
#           
#         wid = driver.find_element_by_android_uiautomator('new UiSelector().description("Widgets")')
#         wid.click()
#         sleep(5)
#           
#         self.driver.swipe(475, 500, 75, 500, 400)
#         self.driver.swipe(475, 500, 75, 500, 400)
#         widgets = driver.find_elements_by_id("com.android.launcher:id/widget_preview")
#          
# #         driver.tap([(widgets[2].location['x'], widgets[2].location['y'])], 1000)
#          
#         act = TouchAction(driver)
#         act.long_press(widgets[5], 200).release().perform()
#         sleep(5)
#          
# #         primary = driver.find_element_by_xpath("//android.widget.TextView[@text='Primary']")
#         
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleAndroidTests)
unittest.TextTestRunner(verbosity=2).run(suite)
