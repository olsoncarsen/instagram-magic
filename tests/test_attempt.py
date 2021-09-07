import logging
import unittest
import json
from instagram_magic.instagrambot import InstagramBot 

class TestAttempt(unittest.TestCase): 
  def test_attempt(self):
    bot = InstagramBot()
    #bot.getInitialCookies()
    result = bot.login()
    print('______LOGIN_____')
    print(result.content)
    #result = bot.uploadPost('/Users/dmitrygashilov/Downloads/dog.jpg')
    #print('______UPLOADPOST_____')
    #print(result.content) 
    #decoded_result = json.loads(result.content)
    #print('UPLOAD_ID ', decoded_result['upload_id'])
    #result = bot.configure(decoded_result['upload_id'], 'It is posted with instagram-magic')
    #print('______CONFIGURE_____')
    #print(result.headers)
    #print(result.content)
    assert(1 == 1)
