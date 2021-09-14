import requests
import json
from requests_toolbelt import MultipartEncoder
import os
import random, string
import base64
import datetime
import pprint

class InstagramBot:
  def __init__(self, *initial_data, **kwargs):
    for dictionary in initial_data:
      for key in dictionary:
       setattr(self, key, dictionary[key])	
    for key in kwargs:
       setattr(self, key, kwargs[key])

    self.session = requests.Session()
    self.session.headers.update({
      'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
    })

  def getAllData(self):
    return vars(self)

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
      'year': 1999,
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

  def igSsoUsers(self):
    url = 'https://www.instagram.com/fxcal/ig_sso_users/'
    response = self.session.post(url)
    print(self.session.cookies)
    return response

  def changeProfilePhoto(self, photo_url):
    url = 'https://www.instagram.com/accounts/web_change_profile_picture/'
    profile_pic = open(photo_url, 'rb').read()
    fields = {
      'profile_pic': ('cat1.jpeg', profile_pic, 'image/jpg'),
    }
    boundary = '----WebKitFormBoundary' + ''.join(random.sample(string.ascii_letters + string.digits, 16))
    m = MultipartEncoder(fields=fields, boundary=boundary)
    self.session.headers.update({
      'Content-Disposition': 'form-data; name="profile_pic"; filename="cat1.jpeg"',
      'Content-Type': m.content_type 
    })

    response = self.session.post(url, data=m) 
    print(self.session.cookies)
    return response

  def editProfile(self, bio_text):
    url = 'https://www.instagram.com/accounts/edit/' 
    data = {
      'first_name': self.first_name, 
      'email': self.email,
      'username': self.username,
      'phone_number': '',
      'biography': bio_text,
      'external_url': '',
      'chaining_enabled': 'on',
    }
    response = self.session.post(url, data=data)
    return response

  def uploadPost(self, photoUrl):
    dt = datetime.datetime.now()
    upload_id = int(dt.timestamp() * 10000) 
    url='https://i.instagram.com/rupload_igphoto/fb_uploader_'+str(upload_id)

    profile_pic = open(photoUrl, 'rb').read()

    self.session.headers.update({
      'Content-Length': str(len(profile_pic)),
      #'content-length': '1',
      'x-entity-length': str(len(profile_pic)),
      'x-entity-name': 'fb_uploader_'+str(upload_id),
      'offset': '0',
      'x-instagram-rupload-params': '{"media_type":1,"upload_id":"'+str(upload_id)+'","upload_media_height":1080,"upload_media_width":1080}',
    })

    print(str(upload_id))
    response = self.session.post(url, data=profile_pic)
    return response

  def login(self):
    url = 'https://www.instagram.com/accounts/login/ajax/' 
    data = {
      'username': self.username, 
      'enc_password': self.password,
      'queryParams': '{}',
      'optIntoOneTap': False,
      'stopDeletionNonce': '',
      'trustedDeviceRecords': {},
    }
    response = self.session.post(url, data=data)
    self.session.headers.update({
      'x-csrftoken': self.session.cookies['csrftoken'],
    })
    print('HEADERS', response.headers) 
    return response

  def configure(self, upload_id, caption):
    url = 'https://i.instagram.com/api/v1/media/configure/'
    self.session.headers.update({
      'x-ig-www-claim': '0', #TODO: you can get this from signup or login
    })
    data = {
      'source_type': 'library', 
      'caption': caption,
      'upcoming_event': '',
      'upload_id': str(upload_id),
      'usertags': '',
      'custom_accessibility_caption': '',
      'disable_comments': '0',
    }

    response = self.session.post(url, data=data)
    return response
