import requests
import json
import pprint

class InstagramAuth:
  def __init__(self, *initial_data, **kwargs):
    self.use_proxy=False
    for dictionary in initial_data:
      for key in dictionary:
       setattr(self, key, dictionary[key])
    for key in kwargs:
       setattr(self, key, kwargs[key])

    self.session = requests.Session()

    if self.use_proxy:
      self.session.proxies = {
          'http':'socks5://127.0.0.1:9050',
          'https':'socks5://127.0.0.1:9050'
      }

    self.session.headers.update({
      'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; motorola one Build/OPKS28.63-18-3; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.80 Mobile Safari/537.36 Instagram 72.0.0.21.98 Android (27/8.1.0; 320dpi; 720x1362; motorola; motorola one; deen_sprout; qcom; pt_BR; 132081645)'
    })

  def _checkClaimHeader(self, response):
    if 'x-ig-set-www-claim' in response.headers:
      print('claim is setted!')
      self.claim = response.headers['x-ig-set-www-claim']

  def _getAllData(self):
      pprint.pprint(vars(self))
      return vars(self)

  def getInitialCookies(self):
    response = self.session.get('https://www.instagram.com/accounts/login/?__a=1')
    self.session.headers.update({
      'x-csrftoken': self.session.cookies.get('csrftoken', domain=".instagram.com"),
    })

  def attempt(self):
    self.getInitialCookies()
    url = 'https://www.instagram.com/accounts/web_create_ajax/attempt/'
    data = {
      'email': self.email,
      'enc_password': self.password,
      'username': self.username,
      'first_name': self.first_name,
      'client_id': self.session.cookies.get('mid', domain=".instagram.com"),
      'opt_into_one_tap': False,
      'seamless_login_enabled': '1',
    }

    response = self.session.post(url, data=data)
    decoded_response = response.json()

    if decoded_response['status'] == 'ok':
        if 'errors' in decoded_response:
            raise Exception(decoded_response['errors'])
        elif 'dryrun_passed' in decoded_response:
            return decoded_response['dryrun_passed']
    else:
        raise Exception('status is not ok, something gone wrong')

  def sendVerifyEmail(self):
    url = 'https://i.instagram.com/api/v1/accounts/send_verify_email/'
    data = {
      'device_id': self.session.cookies.get('mid', domain=".instagram.com"),
      'email': self.email,
    }
    response = self.session.post(url, data=data)
    decoded_response = response.json()
    print(decoded_response)
    if decoded_response['status'] == 'ok':
        if 'errors' in decoded_response:
            raise Exception(decoded_response['errors'])
        elif 'email_sent' in decoded_response:
            return decoded_response['email_sent']
    else:
        if 'errors' in decoded_response:
            raise Exception(decoded_response['errors'])
        else:
            raise Exception('status is not okay without errors, probably its a bug')

  def checkConfirmationCode(self, confirmation_code):
    url = 'https://i.instagram.com/api/v1/accounts/check_confirmation_code/'

    data = {
      'code': confirmation_code,
      'device_id': self.session.cookies.get('mid', domain=".instagram.com"),
      'email': self.email,
    }

    response = self.session.post(url, data)
    self._checkClaimHeader(response)

    decoded_response = response.json()
    self.signup_code = data['signup_code']

    if decoded_response['status'] == 'ok':
        if 'errors' in decoded_response:
            raise Exception(decoded_response['errors'])
        else:
            return True
    else:
        if 'errors' in decoded_response:
            raise Exception(decoded_response['errors'])
        else:
            raise Exception('status is not okay without errors, probably its a bug')

  def checkAgeAbility(self):
    url = 'https://www.instagram.com/web/consent/check_age_eligibility/'
    data = {
      'day': 6,
      'month': 9,
      'year': 1980,
    }
    response = self.session.post(url, data=data)
    try:
        decoded_response = response.json()
    except:
        return response

    return response

