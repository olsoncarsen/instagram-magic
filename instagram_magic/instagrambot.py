import requests
import json
from PIL import Image
from requests_toolbelt import MultipartEncoder
import os
import io
import sys
import random, string
import base64
import datetime
import pprint

class InstagramBot:
  def __init__(self, *initial_data, **kwargs):
    self.use_proxy=False
    for dictionary in initial_data:
      for key in dictionary:
       setattr(self, key, dictionary[key])
    for key in kwargs:
       setattr(self, key, kwargs[key])

    self.session = requests.Session()

    if self.use_proxy:
      self.session.proxies = {'http':'socks5://127.0.0.1:9050', 'https':'socks5://127.0.0.1:9050'}

    self.session.headers.update({
      'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; motorola one Build/OPKS28.63-18-3; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.80 Mobile Safari/537.36 Instagram 72.0.0.21.98 Android (27/8.1.0; 320dpi; 720x1362; motorola; motorola one; deen_sprout; qcom; pt_BR; 132081645)',
    })

  def checkClaimHeader(self, response):
    if 'x-ig-set-www-claim' in response.headers:
      print('claim is setted!')
      self.claim = response.headers['x-ig-set-www-claim']

  def setClaimHeader(self):
    if hasattr(self, 'claim') and self.claim:
      self.session.headers['x-ig-www-claim'] = self.claim
    else:
      self.session.headers['x-lg-www-claim'] = '0'

  def getAllData(self):
    return vars(self)

  def storeToFile(self, file_path=''):
    bot_data = self.getAllData()
    cookies = [
      {'name': c.name, 'value': c.value, 'domain': c.domain, 'path': c.path}
      for c in bot_data['session'].cookies
    ]

    del bot_data['session']

    encoded_bot_data = json.dumps([cookies, bot_data])

    if file_path:
      out = open(file_path, 'w')
    else:
      out = open('output.json', 'w')
    out.write(encoded_bot_data)

  def loadFromFile(self, file_path=''):
    if file_path:
      fo = open(file_path, "r+")
    else:
      fo = open("output.json", "r+")
    encoded_data = fo.read()
    decoded_data = json.loads(encoded_data)
    self.__init__(decoded_data[1])
    for cookie in decoded_data[0]:
      self.session.cookies.set(cookie['name'], cookie['value'], domain=cookie['domain'])

    self.session.headers.update({
      'x-csrftoken': self.session.cookies.get('csrftoken', domain=".instagram.com")
    })

  def getInitialCookies(self):
    url = 'https://www.instagram.com/accounts/login/?__a=1'
    response = self.session.get(url)

    self.session.headers.update({
      'x-csrftoken': self.session.cookies.get('csrftoken', domain=".instagram.com"),
    })

    print('TOKEN ', self.session.cookies.get('csrftoken', domain=".instagram.com"))
    print('MY SESSION COOKIES AT getinitialcookies ', self.session.cookies);
    print('my session headers ', self.session.headers)

    return response

  def attempt(self):
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

    print('TOKEN ', self.session.cookies.get('csrftoken', domain=".instagram.com"))
    response = self.session.post(url, data=data)
    print(response.content)
    return response

  def checkAgeAbility(self):
    url = 'https://i.instagram.com/api/v1/accounts/send_verify_email/'
    data = {
      'day': 6,
      'month': 9,
      'year': 1999,
    }
    print('TOKEN ', self.session.cookies.get('csrftoken', domain=".instagram.com"))
    response = self.session.post(url, data=data)
    return response

  def sendVerifyEmail(self):
    url = 'https://i.instagram.com/api/v1/accounts/send_verify_email/'
    data = {
      'device_id': self.session.cookies.get('mid', domain=".instagram.com"),
      'email': self.email,
    }
    response = self.session.post(url, data=data)
    print('TOKEN ', self.session.cookies.get('csrftoken', domain=".instagram.com"))
    print(response.content)
    return response

  def checkConfirmationCode(self, confirmation_code):
    url = 'https://i.instagram.com/api/v1/accounts/check_confirmation_code/'

    data = {
      'code': confirmation_code,
      'device_id': self.session.cookies.get('mid', domain=".instagram.com"),
      'email': self.email,
    }

    response = self.session.post(url, data)
    self.checkClaimHeader(response)

    data = response.json()
    print('CODE DATA ---> ', data);
    print('TOKEN ', self.session.cookies.get('csrftoken', domain=".instagram.com"))
    print('SIGNUP_CODE!!! ', data['signup_code'])
    print(response.content)
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
      'client_id': self.session.cookies.get('mid', domain=".instagram.com"),
      'seamless_login_enabled': 1,
      'tos_version': 'row',
      'force_sign_up_code': self.signup_code,
    }
    response = self.session.post(url, data=data)
    self.checkClaimHeader(response)
    return response

  def signUp(self):
    self.getInitialCookies()
    response = self.attempt()
    self.checkAgeAbility()
    response = self.sendVerifyEmail()
    self.checkConfirmationCode()
    response = self.webCreateAjax()
    self.igSsoUsers()
    return response

  def igSsoUsers(self):
    url = 'https://www.instagram.com/fxcal/ig_sso_users/'
    self.setClaimHeader()
    self.session.headers['x-ig-app-id'] = self.session.cookies.get('ds_user_id', domain=".instagram.com")
    self.session.headers['x-instagram-ajax'] = 'a043e3868c2a'
    self.session.headers['x-requested-with'] =  'XMLHttpRequest'
    response = self.session.post(url)
    self.checkClaimHeader(response)
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
    self.checkClaimHeader(response)
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

  def uploadPost(self, photoUrl, caption):
    dt = datetime.datetime.now()
    upload_id = int(dt.timestamp() * 1000)
    self.setClaimHeader()

    url='https://i.instagram.com/rupload_igphoto/fb_uploader_'+str(upload_id)

    buffer = io.BytesIO()
    img = Image.open(photoUrl)
    img = img.resize((1080, 1080), Image.NEAREST)
    format = "JPEG"
    img.save(buffer, format)

    self.session.headers.update({
      'content-length': str(len(buffer.getvalue())),
      'x-entity-length': str(len(buffer.getvalue())),
      'x-entity-name': 'fb_uploader_'+str(upload_id),
      'x-entity-type': 'image/jpeg',
      'offset': '0',
      'x-instagram-ajax': 'a043e3868c2a',
      'x-asbd-id': '198387',
      'x-ig-app-id': self.session.cookies.get('ds_user_id', domain=".instagram.com"),

      'x-instagram-rupload-params': '{"media_type":1,"upload_id":"'+str(upload_id)+'","upload_media_height":1080,"upload_media_width":1080}',
    })


    response = self.session.post(url, data=buffer.getvalue())
    print('UPLOAD RESPONSE ', response.content)
    return response

  def configure(self, upload_id, caption):
    url = 'https://i.instagram.com/api/v1/media/configure/'

    self.setClaimHeader()
    self.session.headers['x-ig-app-id'] = self.session.cookies.get('ds_user_id', domain=".instagram.com")
    self.session.headers['accept-encoding'] = 'gzip, deflate, br'
    self.session.headers['content-type'] = 'application/x-www-form-urlencoded'
    self.session.headers['x-requested-with'] =  'XMLHttpRequest'
    self.session.headers['set-fetch-dest'] = 'empty'
    self.session.headers['sec-fetch-mode'] = 'cors'
    self.session.headers['sec-fetch-site'] = 'same-site'

    data = {
      'source_type': 'library',
      'caption': caption,
      'upcoming_event': '',
      'upload_id': str(upload_id),
      'usertags': '',
      'custom_accessibility_caption': '',
      'disable_comments': 0,
    }

    response = self.session.post(url, data=data)
    self.checkClaimHeader(response)
    return response

  def configure_to_story(self, upload_id, caption):
    url = 'https://www.instagram.com/create/configure_to_story/'

    self.setClaimHeader()
    self.session.headers['x-ig-app-id'] = self.session.cookies.get('ds_user_id', domain=".instagram.com")
    self.session.headers['accept-encoding'] = 'gzip, deflate, br'
    self.session.headers['content-type'] = 'application/x-www-form-urlencoded'
    self.session.headers['x-requested-with'] =  'XMLHttpRequest'
    self.session.headers['set-fetch-dest'] = 'empty'
    self.session.headers['sec-fetch-mode'] = 'cors'
    self.session.headers['sec-fetch-site'] = 'same-site'

    data = {
      'upload_id': str(upload_id),
      'caption': str(caption),
    }

    response = self.session.post(url, data=data)
    self.checkClaimHeader(response)
    return response

  def login(self):
    url = 'https://www.instagram.com/accounts/login/ajax/'
    self.setClaimHeader()
    self.session.headers['x-ig-www-claim'] = '0'
    data = {
      'username': self.username,
      'enc_password': self.password,
      'queryParams': '{}',
      'optIntoOneTap': False,
      'stopDeletionNonce': '',
      'trustedDeviceRecords': {},
    }
    response = self.session.post(url, data=data)
    self.checkClaimHeader(response)
    self.setClaimHeader()
    self.storeToFile()
    return response

  def like(self, post_id):
    url = f"https://www.instagram.com/web/likes/{post_id}/like/"
    self.setClaimHeader()
    self.session.headers['x-ig-app-id'] = self.session.cookies.get('ds_user_id', domain=".instagram.com")
    response = self.session.post(url)
    return response

  def unlike(self, post_id):
    url = f"https://www.instagram.com/web/likes/{post_id}/unlike/"
    self.setClaimHeader()
    self.session.headers['x-ig-app-id'] = self.session.cookies.get('ds_user_id', domain=".instagram.com")
    response = self.session.post(url)
    return response

  def comment(self, post_id, comment_text, reply_id=''):
    url = f"https://www.instagram.com/web/comments/{post_id}/add/"
    self.setClaimHeader()
    self.session.headers['x-ig-app-id'] = self.session.cookies.get('ds_user_id', domain=".instagram.com")
    data = {
      'comment_text': comment_text,
      'replied_to_comment_id': reply_id,
    }
    response = self.session.post(url, data=data)
    return response

  def follow(self, user_id):
    url = f"https://www.instagram.com/web/friendships/{user_id}/follow/"
    self.setClaimHeader()
    self.session.headers['x-ig-app-id'] = self.session.cookies.get('ds_user_id', domain=".instagram.com")
    response = self.session.post(url)
    return response

  def unfollow(self, user_id):
    url = f"https://www.instagram.com/web/friendships/{user_id}/unfollow/"
    self.setClaimHeader()
    self.session.headers['x-ig-app-id'] = self.session.cookies.get('ds_user_id', domain=".instagram.com")
    response = self.session.post(url)
    return response

  def recentSearches(self):
    url = "https://www.instagram.com/web/search/recent_searches/"
    self.setClaimHeader()
    self.session.headers['x-ig-app-id'] = self.session.cookies.get('ds_user_id', domain=".instagram.com")
    self.session.headers['x-requested-with'] =  'XMLHttpRequest'
    response = self.session.get(url)
    return response

  def search(self, query):
    rank_token = 0.8187201068442573
    url = f"https://www.instagram.com/web/search/topsearch/?context=blended&query={query}&rank_token={rank_token}&include_reel=true"

    self.setClaimHeader()
    self.session.headers['x-ig-app-id'] = self.session.cookies.get('ds_user_id', domain=".instagram.com")
    self.session.headers['x-requested-with'] =  'XMLHttpRequest'

    data = {
      'context': 'blended',
      'query': str(query),
      'rank_token': rank_token,
      'include_reel': 'true',
    }

    response = self.session.get(url, data=data)
    return response

  def getUserInfo(self, username):
    url = f"https://www.instagram.com/{username}/?__a=1"

    self.setClaimHeader()
    self.session.headers['x-ig-app-id'] = self.session.cookies.get('ds_user_id', domain=".instagram.com")
    self.session.headers['x-requested-with'] =  'XMLHttpRequest'

    response = self.session.get(url)
    return response

  def getPostInfo(self, shortcode):
    url = f"https://www.instagram.com/p/{shortcode}/?__a=1"

    self.setClaimHeader()
    self.session.headers['x-ig-app-id'] = self.session.cookies.get('ds_user_id', domain=".instagram.com")
    self.session.headers['x-requested-with'] =  'XMLHttpRequest'

    response = self.session.get(url)
    return response

  def removePost(self, post_id):
    url = f"https://www.instagram.com/create/{post_id}/delete/"

    self.setClaimHeader()
    self.session.headers['x-ig-app-id'] = self.session.cookies.get('ds_user_id', domain=".instagram.com")
    self.session.headers['x-requested-with'] =  'XMLHttpRequest'

    response = self.session.post(url)
    return response

  # redirects to request with html code response
  def getPostLikes(self, shortcode):
    url = f"https://www.instagram.com/p/{shortcode}/liked_by/?__a=1"

    self.setClaimHeader()
    self.session.headers['x-ig-app-id'] = self.session.cookies.get('ds_user_id', domain=".instagram.com")
    self.session.headers['x-requested-with'] =  'XMLHttpRequest'

    response = self.session.get(url)
    return response

  def getUserFollowers(self, user_id, count, max_id):
    #url = f"https://i.instagram.com/api/v1/friendships/{user_id}/followers/?count={count}&max_id={max_id}&search_surface=follow_list_page"
    url = f"https://i.instagram.com/api/v1/friendships/{user_id}/followers/?count={count}&search_surface=follow_list_page"

    self.setClaimHeader()
    self.session.headers['x-ig-app-id'] = self.session.cookies.get('ds_user_id', domain=".instagram.com")
    self.session.headers['x-requested-with'] =  'XMLHttpRequest'

    response = self.session.get(url)
    return response

  def inbox(self):
    url = "https://i.instagram.com/api/v1/news/inbox/"

    self.setClaimHeader()
    self.session.headers['x-ig-app-id'] = self.session.cookies.get('ds_user_id', domain=".instagram.com")
    self.session.headers['x-requested-with'] =  'XMLHttpRequest'

    response = self.session.post(url)
    return response
