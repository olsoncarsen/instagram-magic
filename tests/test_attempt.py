import logging
import unittest
from instagram_magic.instagrambot import attempt
from instagram_magic.instagrambot import get_initial_cookies 

class TestAttempt(unittest.TestCase): 
  def test_attempt(self):
    result = attempt()
    assert(1 == 1)
  def test_get_initial_cookies(self):
    get_initial_cookies()
    assert(1 == 1)
  
    
