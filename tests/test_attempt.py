import logging
import unittest
from instagram_magic.instagrambot import InstagramBot 

class TestAttempt(unittest.TestCase): 
  def test_attempt(self):
    bot = InstagramBot()

    result = bot.login()
    print(result.content)
    result = bot.uploadPost('/Users/dmitrygashilov/Downloads/dog.jpg')
    print(result.content) 

    assert(1 == 1)
