import requests
import json

class InstagramBot:
  def __init__(self):
    self.session = requests.Session()
    self.session.headers.update({
      'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
    })

    self.email = 'ervinsmith1488@gmail.com'
    self.username = 'sarichev_121212'
    self.first_name = 'Dmitry Konovalov'
    self.password = '#PWD_INSTAGRAM_BROWSER:10:1630703426:AV1QAAWNJhYppwTf5JZxt0vr89oUNIArCbzsw6m/KCaARQgL4Ep/doi6+jsnGqAbtutf6jumuowIbezx/fLkrt9NwxnteY0Vu/bZ7rqGjtj5a3tc10OhZkqb67aIKXSvcG4fWIq8qfvgUcTTjVkB+m7wFGk='
    self.signup_code = 'csrHnwMI' 
    self.session.cookies.set("csrftoken", "pfEPUZ0GdCgcB5eDEatfv9xv9q127CRY", domain=".instagram.com")
    self.session.cookies.set("ig_did", "044E87C4-BF92-4BDD-B830-1C52F60CAB79", domain=".instagram.com")
    self.session.cookies.set("ig_nrcb", "1", domain=".instagram.com")
    self.session.cookies.set("mid", "YTKRgwAEAAHALoyLRbj7Bdu9CMWP", domain=".instagram.com")

    self.session.headers.update({
      'x-csrftoken': self.session.cookies['csrftoken'],
    })

  def getInitialCookies(self):
    url = 'https://www.instagram.com/accounts/emailsignup/' 
    response = self.session.get(url) 
    print('my session ', self.session.cookies)
    self.session.headers.update({
      'x-csrftoken': self.session.cookies['csrftoken'],
    })
    return response

  def attempt(self):
    url = 'https://www.instagram.com/accounts/web_create_ajax/attempt/' 
    data = {
      'email': self.email,
      'enc_password': self.password,
      'username': self.username,
      'first_name': self.first_name,
      'client_id': self.session.cookies['mid'],
      'opt_into_one_tap': False,
      'seamless_login_enabled': '1',
    }
    response = self.session.post(url, data=data)
    return response

  def checkAgeAbility(self):
    url = 'https://i.instagram.com/api/v1/accounts/send_verify_email/' 
    data = {
      'day': 6,
      'month': 9,
      'year': 1996,
    }
    response = self.session.post(url, data=data)
    return response

  def sendVerifyEmail(self):
    url = 'https://i.instagram.com/api/v1/accounts/send_verify_email/' 
    data = {
      'device_id': self.session.cookies['mid'],
      'email': self.email,
    }
    response = self.session.post(url, data=data)
    return response

  def checkConfirmationCode(self): 
    url = 'https://i.instagram.com/api/v1/accounts/check_confirmation_code/' 
    confirmation_code = input('Enter your confirmation code: ')
    data = {
      'code': confirmation_code,
      'device_id': self.session.cookies['mid'],
      'email': self.email,
    }
    response = self.session.post(url, data)
    data = response.json()
    print('SIGNUP_CODE!!! ', data['signup_code'])
    self.signup_code = data['signup_code']

    return response

  def webCreateAjax(self):
    url = 'https://www.instagram.com/accounts/web_create_ajax/'
    data = {
      'email': self.email,
      'enc_password': self.password,
      'username': self.username,
      'first_name': self.first_name,
      'month': 9,
      'day': 10,
      'year': 1999,
      'client_id': self.session.cookies['mid'],
      'seamless_login_enabled': 1,
      'tos_version': 'row',
      'force_sign_up_code': self.signup_code,
    }
    response = self.session.post(url, data=data)
    return response

  def signUp(self):
    self.getInitialCookies()
    self.attempt()
    self.checkAgeAbility()
    self.sendVerifyEmail()
    self.checkConfirmationCode()
    response = self.webCreateAjax()
