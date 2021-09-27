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

  def test_get_initial_cookies(self):
    bot = InstagramBot()
    res = bot.getInitialCookies()
    assert(bot.session.cookies['csrftoken'])

  def test_attempt(self):
    bot = InstagramBot(data)
    bot.loadFromFile()
    bot.getInitialCookies()
    res = bot.attempt()
    assert(json.loads(res.content)['status'] == 'ok')

  def test_age_ability(self):
    bot = InstagramBot()
    bot.loadFromFile()
    bot.getInitialCookies()
    bot.attempt()
    res = bot.checkAgeAbility()
    assert(json.loads(res.content)['status'] == 'fail') #returns 'fail' but anyway lets regiser account

  def test_send_verify_email(self):
    bot = InstagramBot(data)
    bot.loadFromFile()
    bot.getInitialCookies()
    res = bot.sendVerifyEmail()
    assert(json.loads(res.content)['status'] == 'ok')

  def test_login(self):
    bot = InstagramBot()
    bot.loadFromFile()
    res = bot.login()
    print('headers', res.headers)
    print('cookies ', res.cookies)
    print('content', res.content)
    bot.storeAllData()
    assert(1 == 1)
    
  def test_signup(self):
    data = {
      'email': 'iafewznzuocikcbidj@mrvpm.net',
      'username': 'idfvge1284ddf',
      'password': '#PWD_INSTAGRAM_BROWSER:10:1631902003:AVBQADO9jab1S/eqx7yYp0uEvFbBUUXTU9uVNDvldNQCkc8HQlhDZitjr7Od7GmKRWnkjiN+mDSoJFeEiPcAunZmC7F5eqOY7wqv3ARQqzea0lO55Jd2ZTjh1rA4lD+gdiFaZBcnr5nUTHI5fjW8TQtLe17VnpL7sQ==',
      'first_name': 'Someone Else',
    }

    bot = InstagramBot(data)
    res = bot.signUp() 
    bot.storeAllData()

  def test_ig_sso_users(self):
    bot = InstagramBot()
    bot.loadFromFile()
    res = bot.igSsoUsers()
    bot.storeAllData()
    print(res.content)
    assert(1 == 1)

  def test_change_bio(self):
    bot = InstagramBot()
    bot.loadFromFile()

    res = bot.editProfile('hello world')
    bot.storeAllData()
    print(res.content)
    assert(1 == 1)

  def test_proxy(self):
    bot = InstagramBot()
    print(bot.session.get("http://httpbin.org/ip").text)
    assert(1 == 1)

  def test_upload_avatar(self):
    bot = InstagramBot()
    bot.loadFromFile()
    res = bot.changeProfilePhoto('/Users/dmitrygashilov/Downloads/andrey.jpg')
    print(res.content)
    assert(1 == 1)

  def test_upload_post(self):
    bot = InstagramBot()
    bot.loadFromFile()
    res = bot.uploadPost('/Users/dmitrygashilov/Downloads/dog.jpg', 'Hello it is me, Parker') 
    print(res.content)
    assert(1 == 1)

  def test_configure(self):
    bot = InstagramBot()
    bot.loadFromFile()
    res = bot.configure('1632685489601', 'Hello it is me, Parker') 
    print(res.content)
    print(bot.session.headers)
    assert(1 == 1)

  def test_configure_to_story(self):
    bot = InstagramBot()
    bot.loadFromFile()
    res = bot.configure_to_story('1632689507987', '') 
    print(res.content)
    print(bot.session.headers)
    assert(1 == 1)

  def test_like(self):
    bot = InstagramBot()
    bot.loadFromFile()
    res = bot.like('2653539106451643407') 
    print(res.content)
    print(bot.session.headers)
    assert(1 == 1)

  def test_unlike(self):
    bot = InstagramBot()
    bot.loadFromFile()
    res = bot.unlike('2653539106451643407') 
    print(res.content)
    print(bot.session.headers)
    assert(1 == 1)

  def test_comment(self):
    bot = InstagramBot()
    bot.loadFromFile()
    res = bot.comment('2671480161700016831', 'it is my new comment!') 
    print(res.content)
    print(bot.session.headers)
    assert(1 == 1)

  def test_follow(self):
    bot = InstagramBot()
    bot.loadFromFile()
    res = bot.follow('31356058676') 
    print(res.content)
    print(bot.session.headers)
    assert(1 == 1)

  def test_unfollow(self):
    bot = InstagramBot()
    bot.loadFromFile()
    res = bot.unfollow('31356058676') 
    print(res.content)
    print(bot.session.headers)
    assert(1 == 1)

  def test_recent_searches(self):
    bot = InstagramBot()
    bot.loadFromFile()
    res = bot.recentSearches() 
    print(res.content)
    print(bot.session.headers)
    assert(1 == 1)

  def test_search(self):
    bot = InstagramBot()
    bot.loadFromFile()
    res = bot.search('hello') 
    print(res.content)
    print(res.status_code)
    assert(1 == 1)
