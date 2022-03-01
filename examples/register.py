from instagram_magic.instagrambot import InstagramBot
import json

# make request
# store data in apropriate way
# that's all

if __name__ == '__main__':
  data = {
    'email': 'uyqjbtxoreednfqocj@zqrni.com',
    'username': 'SomeWorldClass12387',
    'password': '#PWD_INSTAGRAM_BROWSER:10:1631902003:AVBQADO9jab1S/eqx7yYp0uEvFbBUUXTU9uVNDvldNQCkc8HQlhDZitjr7Od7GmKRWnkjiN+mDSoJFeEiPcAunZmC7F5eqOY7wqv3ARQqzea0lO55Jd2ZTjh1rA4lD+gdiFaZBcnr5nUTHI5fjW8TQtLe17VnpL7sQ==',
    'first_name': 'Hello World',
  }

  bot = InstagramBot(data)
  res = bot.signUp()

  print(res.headers)
  print(res.cookies)
  print(res.content)

  bot_data = bot.getAllData()
  cookies = bot_data.session.cookies
  headers = bot_data.session.headers
  encoded_bot_data = json.dumps([cookies, headers, bot_data])

  with open('output.json', 'a') as out:
    out.write(encoded_bot_data)

