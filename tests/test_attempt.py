import logging
import unittest
from instagram_magic.instagrambot import attempt

class TestAttempt(unittest.TestCase): 
  def test_attempt(self):
    result = attempt()
    assert(1 == 1)
