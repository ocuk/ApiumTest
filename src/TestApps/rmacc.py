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

class TestRemoveAccount(unittest.TestCase):
    
    def test_remove_account(self):
          
        # press home button
        self.driver.press_keycode(3)
          
        settings = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//android.widget.TextView[@text='Settings']")))
        self.assertIsNotNone(settings, 'no settings')
        sleep(2)
        settings.click()
        sleep(5)
          
        # find all options
        els = self.driver.find_elements_by_id("android:id/title")
        self.assertGreaterEqual(len(els), 5)
        self.driver.scroll(els[len(els)-1], els[0])
        els = self.driver.find_elements_by_id("android:id/title")
        self.assertGreaterEqual(len(els), 5)
         
        # find twitter in the options
        twitter = None
        for el in els:
            if el.text == 'Twitter':
                twitter = el
                 
        self.assertIsNotNone(twitter, 'no twitter')
        twitter.click()
         
        # click menu               
        menu = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "android.widget.ImageButton")))
        self.assertIsNotNone(menu, 'no menu in twitter account')
        menu.click()
           
        # choose to remove the account
        rm = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//android.widget.TextView[@text='Remove account']")))
        self.assertIsNotNone(rm, 'no remove option')
        rm.click()
           
        # confirm
        button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@text='Remove account']")))
        self.assertIsNotNone(rm, 'no remove button')
        button.click()
         
        # confirm twitter is not in the list         
        for el in els:
            if el.text == 'Twitter':
                tw = el
            else:
                tw = None
                 
        self.assertIsNone(tw, 'twitter not removed')