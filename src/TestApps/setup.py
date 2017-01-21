import unittest
import os
from appium import webdriver

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class TestSetup(unittest.TestCase):
    
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.3'
        desired_caps['deviceName'] = 'Nexus4-3_18'
        desired_caps['app'] = PATH(
            '../../../../testAPK/twitter.apk'
            )
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)