import requests
import json

def get_initial_cookies():
  s = requests.Session()
  url = 'https://www.instagram.com/accounts/emailsignup/' 
  headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
  }
  r = s.get(url, headers=headers)
  cookies = {
    'csrftoken': r.cookies['csrftoken'],
    'mid': r.cookies['mid'],
    'ig_did': r.cookies['ig_did'],
    'ig_nrcb': r.cookies['ig_nrcb'],
  }
  print(cookies)
  return r.content

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
      'email': 'jskdjdsfjsd@ksdjf.ru',
      'enc_password': '#PWD_INSTAGRAM_BROWSER:10:1630432041:AQpQAK2NpjpV6rUaB/XL/4Wio/cRGlY5mJ3Esqb6ZDYqn3kPPgZm/zgw5pw7eP6bxyS/gWzgv8ypFVJSi8fhNJKztuP7ih5MVAWHzzve/A7PBY8XLpH6ELPiHK4RjZsmcsaLTKsJcdMC',
      'username': 'sdkjsdkfjsdf',
      'first_name': 'dmitry someone',
      'client_id': 'YS5chQAEAAF3m0_fNMUWgYMz5df7',
      'opt_into_one_tap': False,
      'seamless_login_enabled': '1',
  }

  headers = {
    'cookie': 'ig_did=73BA5476-FCF9-40E2-B51E-1BC08E78E28B; ig_nrcb=1; csrftoken=WGfJ3y5Pth68IzmVTdYRjbhNu8p4vWrw; mid=YS5chQAEAAF3m0_fNMUWgYMz5df7',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
    'x-csrftoken': 'WGfJ3y5Pth68IzmVTdYRjbhNu8p4vWrw',
  }

  r = s.post(url, cookies=cookies, data=data, headers=headers)
  print(r.content)
  return r.content

def check_age_ability():
  s = requests.Session()
  url = 'https://i.instagram.com/api/v1/accounts/send_verify_email/' 

  cookies = {
    'ig_did': '73BA5476-FCF9-40E2-B51E-1BC08E78E28B',
    'ig_nrcb': '1',
    'csrftoken': 'WGfJ3y5Pth68IzmVTdYRjbhNu8p4vWrw',
    'mid': 'YS5chQAEAAF3m0_fNMUWgYMz5df7',
  } 

  headers = {
    'cookie': 'ig_did=73BA5476-FCF9-40E2-B51E-1BC08E78E28B; ig_nrcb=1; csrftoken=WGfJ3y5Pth68IzmVTdYRjbhNu8p4vWrw; mid=YS5chQAEAAF3m0_fNMUWgYMz5df7',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
    'x-csrftoken': 'WGfJ3y5Pth68IzmVTdYRjbhNu8p4vWrw',
  }
  
  data = {
    'day': '6',
    'month': '9',
    'year': '1999',
  }
  r = s.post(url, cookies=cookies, data=data, headers=headers)
  print(r.content)
  return r.content
    
def send_verify_email():
  s = requests.Session()
  url = 'https://i.instagram.com/api/v1/accounts/send_verify_email/' 

  cookies = {
    'ig_did': '73BA5476-FCF9-40E2-B51E-1BC08E78E28B',
    'ig_nrcb': '1',
    'csrftoken': 'WGfJ3y5Pth68IzmVTdYRjbhNu8p4vWrw',
    'mid': 'YS5chQAEAAF3m0_fNMUWgYMz5df7',
  } 

  headers = {
    'cookie': 'ig_did=73BA5476-FCF9-40E2-B51E-1BC08E78E28B; ig_nrcb=1; csrftoken=WGfJ3y5Pth68IzmVTdYRjbhNu8p4vWrw; mid=YS5chQAEAAF3m0_fNMUWgYMz5df7',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
    'x-csrftoken': 'WGfJ3y5Pth68IzmVTdYRjbhNu8p4vWrw',
  }
  
  data = {
    'device_id': 'YS5chQAEAAF3m0_fNMUWgYMz5df7',
    'email': 'someemail@hui.com',
  }
  r = s.post(url, cookies=cookies, data=data, headers=headers)
  print(r.content)
  return r.content
  
def check_confirmation_code():
  s = requests.Session()
  url = 'https://i.instagram.com/api/v1/accounts/check_confirmation_code/' 

  cookies = {
    'ig_did': '73BA5476-FCF9-40E2-B51E-1BC08E78E28B',
    'ig_nrcb': '1',
    'csrftoken': 'WGfJ3y5Pth68IzmVTdYRjbhNu8p4vWrw',
    'mid': 'YS5chQAEAAF3m0_fNMUWgYMz5df7',
  } 

  headers = {
    'cookie': 'ig_did=73BA5476-FCF9-40E2-B51E-1BC08E78E28B; ig_nrcb=1; csrftoken=WGfJ3y5Pth68IzmVTdYRjbhNu8p4vWrw; mid=YS5chQAEAAF3m0_fNMUWgYMz5df7',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
    'x-csrftoken': 'WGfJ3y5Pth68IzmVTdYRjbhNu8p4vWrw',
  }
  
  data = {
    'code': '123123',
    'device_id': 'YS5chQAEAAF3m0_fNMUWgYMz5df7',
    'email': 'someemail@hui.com',
  }
  r = s.post(url, cookies=cookies, data=data, headers=headers)
  print(r.content)
  return r.content
