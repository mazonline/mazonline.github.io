#!/usr/local/bin/python

from selenium import selenium
import unittest, time, re
   def setUp(self):
        self.verificationErrors = []
        # This is an empty array where we will store any verification errors
        # we find in our tests

        self.selenium = selenium("localhost", 4444, "*firefox","http://mazonline.github.io/index.html/")
        self.selenium.start()
        # We instantiate and start the browser
