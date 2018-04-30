import os
import sys
import unittest

from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

os.environ['MOZ_HEADLESS'] = '1'

class MailingListTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_two_visits(self):
        self.fail("There is nothing here!")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
