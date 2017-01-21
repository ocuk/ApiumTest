import unittest
import os
from time import sleep
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class TestLogin(unittest.TestCase):
    
    def test_login(self):
           
        # 
        self.assertTrue(self.driver.is_app_installed('com.twitter.android'))
           
        # 
        login = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "com.twitter.android:id/log_in")))
        self.assertIsNotNone(login)
        login.click()
        sleep(5)
           
        # 
        email = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "com.twitter.android:id/login_identifier")))
        self.assertIsNotNone(email, 'no email entry')
        email.clear()
        email.send_keys("overkholyak")
        sleep(1)
           
        # 
        passw = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "com.twitter.android:id/login_password")))
        self.assertIsNotNone(passw, 'no password entry')
        passw.clear()
        passw.send_keys('urm4ffe68d')
        sleep(1)
           
        # 
        submit = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "com.twitter.android:id/login_login")))
        self.assertIsNotNone(login, 'no login button')
        submit.click()
           
        refuse = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "android:id/button2")))
        self.assertIsNotNone(refuse, 'no dialog box after login')
        refuse.click()
           
        menu = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "com.twitter.android:id/drawer_icon")))
        self.assertIsNotNone(menu, 'no menu')
        menu.click()
           
        name = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "com.twitter.android:id/name")))
        self.assertEqual(u'Oxana Verkholyak', name.text)