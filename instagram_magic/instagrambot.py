import requests
import json

def attempt():
  s = requests.Session()
  url = 'https://www.instagram.com/accounts/web_create_ajax/attempt/' 
  cookies = {
    'ig_did': '73BA5476-FCF9-40E2-B51E-1BC08E78E28B',
    'ig_nrcb': '1',
    'csrftoken': 'WGfJ3y5Pth68IzmVTdYRjbhNu8p4vWrw',
    'mid': 'YS5chQAEAAF3m0_fNMUWgYMz5df7',
  } 
  data = {
      'email': 'hello@yandex.ru',
      'enc_password': '#PWD_INSTAGRAM_BROWSER:10:1630432041:AQpQAK2NpjpV6rUaB/XL/4Wio/cRGlY5mJ3Esqb6ZDYqn3kPPgZm/zgw5pw7eP6bxyS/gWzgv8ypFVJSi8fhNJKztuP7ih5MVAWHzzve/A7PBY8XLpH6ELPiHK4RjZsmcsaLTKsJcdMC',
      'username': 'hello',
      'first_name': 'dmitry someone',
      'opt_into_one_tap': False,
  }
  r = s.post(url, cookies=cookies, data=data)
  print(r.content)
  return r.content

def add_one(number):
  return number + 1
