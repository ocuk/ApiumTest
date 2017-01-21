import unittest
import os
from appium import webdriver

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class TestTeardown(unittest.TestCase):

    def tearDown(self):
        # end the session
        self.driver.quit()