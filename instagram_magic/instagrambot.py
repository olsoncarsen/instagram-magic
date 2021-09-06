import requests
import json
from requests_toolbelt import MultipartEncoder
import os
import random, string
import base64
import datetime

class InstagramBot:
  def __init__(self):
    self.session = requests.Session()
    self.session.headers.update({
      'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
    })

    self.email = 'ervinsmith1488@gmail.com'
    self.username = 'sarichev_121212'
    self.first_name = 'Dmitry Konovalov'
    self.password = '#PWD_INSTAGRAM_BROWSER:10:1630949284:AfxQAART9MOKGTwWIDUXUQqCQpoUQfAg0lPQQ3E6jpR1hJ4YOJ8eugc0t9OTW9PGmOxSmid4DXNYgl5RdgEpnJcKF6/tKiJojkL/9MOvRSLaso2aYWQu7BIY4wJQDQJ2rE2CHYITNI3+xcQU26vs'
    self.signup_code = 'csrHnwMI' 

    self.session.cookies.set("csrftoken", "4PbM3p8wOjRacwwkgoajyaaTQyVlUtHC", domain=".instagram.com")
    #self.session.cookies.set("ig_did", "044E87C4-BF92-4BDD-B830-1C52F60CAB79", domain=".instagram.com")
    #self.session.cookies.set("ig_nrcb", "1", domain=".instagram.com")
    #self.session.cookies.set("mid", "YTKRgwAEAAHALoyLRbj7Bdu9CMWP", domain=".instagram.com")
    #self.session.cookies.set("ds_user_id", "49302523346", domain=".instagram.com")
    #self.session.cookies.set("rur", "ODN\05449302523346\0541662401186:01f7b25b1742a6e787ed4faf5edcc2d215b8d3f79187b843f1ba661a6b761e36ea29f83f", domain=".instagram.com")
    #self.session.cookies.set("sessionid", "49302523346%3AY4ohX4Vs67sDAo%3A22", domain=".instagram.com")

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
    upload_id = int(dt.timestamp() * 1000) 
    url='https://i.instagram.com/rupload_igphoto/fb_uploader_'+str(upload_id)
    self.session.headers.update({
      'x-entity-name': 'fb_uploader_'+str(upload_id),
      'offset': '1',
      'x-instagram-rupload-params': '{"media_type":1,"upload_id":"'+str(upload_id)+'","upload_media_height":1079,"upload_media_width":1080}',
    })
    print(str(upload_id))
    profile_pic = open(photoUrl, 'rb').read()

    response = self.session.post(url, data=profile_pic)
    print(response.request.headers)
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
    print(self.session.cookies)
    self.session.headers.update({
      'x-csrftoken': self.session.cookies['csrftoken'],
    })
    
    return response

