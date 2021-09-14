import logging
import unittest
import json
from instagram_magic.instagrambot import InstagramBot 

class TestInstagramBot(unittest.TestCase): 
  def test_get_all_data_at_start(self):
    bot = InstagramBot()
    res = bot.getAllData()
    assert(res['session'])

  def test_set_init_data(self):
    bot = InstagramBot(dog='cat')
    assert(bot.dog == 'cat')

  def test_get_initial_cookie(self):
    bot = InstagramBot()
    res = bot.getInitialCookies()
    assert(bot.session.cookies['csrftoken'])

  def test_attempt(self):
    data = {
      'email': 'asdfasdfasdfasdf@asdfasdfasdf.ru',
      'password': 'helloworld',
      'username': 'adsfasdfasdfsadf12323',
      'first_name': 'James Stoner',
    }
    bot = InstagramBot(data)
    bot.getInitialCookies()
    res = bot.attempt()
    assert(json.loads(res.content)['status'] == 'ok')

  def test_age_ability(self):
    data = {
      'email': 'asdfasdfasdfasdf@asdfasdfasdf.ru',
      'password': 'helloworld',
      'username': 'adsfasdfasdfsadf12323',
      'first_name': 'James Stoner',
    }
    bot = InstagramBot(data)
    bot.getInitialCookies()
    bot.attempt()
    res = bot.checkAgeAbility()
    assert(json.loads(res.content)['status'] == 'fail') #returns 'fail' but anyway lets regiser account

  def test_send_verify_email(self):
    data = {
      'email': 'asdfasdfasdfasdf@asdfasdfasdf.ru',
      'password': 'helloworld',
      'username': 'adsfasdfasdfsadf12323',
      'first_name': 'James Stoner',
    }
    bot = InstagramBot(data)
    bot.getInitialCookies()
    res = bot.sendVerifyEmail()
    assert(json.loads(res.content)['status'] == 'ok')
