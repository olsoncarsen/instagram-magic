import logging
import unittest
from instagram_magic.instagrambot import InstagramBot 

class TestAttempt(unittest.TestCase): 
  def test_attempt(self):
    bot = InstagramBot()
    bot.getInitialCookies()
    print('bots cookies ', bot.session.cookies)
    result = bot.attempt()
    print(result.content)
    result = bot.checkAgeAbility()
    print(result.content)
    result = bot.sendVerifyEmail()
    print(result.content)
    result = bot.checkConfirmationCode()
    print(result.content)
    result = bot.webCreateAjax()
    print(result.content)
    assert(1 == 1)
