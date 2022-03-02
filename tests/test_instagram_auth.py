import pytest
import unittest
import json
from instagram_magic.instagramauth import InstagramAuth

class TestInstagramAuth(unittest.TestCase):
  def test_get_initial_cookies(self):
    auth_manager = InstagramAuth()
    auth_manager.getInitialCookies()
    assert(auth_manager.session.headers.get('x-csrftoken'))

  def test_attempt_success(self):
    config = {
        'email': 'gasdflkj@sdjsf.ru',
        'password': '#PWD_INSTAGRAM_BROWSER:10:1646157249:AedQAGcxmpyDHo8T4t8Ibiiz9muYzrT5KDxoinjO8ec+UslgJGwN/KsLrFycODgwa17+dU7a146S8pNbg+Gp6Xk2Vvan6ky35vJ4ALlGRC76XnxeKYzPCqdPBQUFBp4tlGCjAms76CcLRYVUZ0nqte0=',
        'username': 'sldkjfsd',
        'first_name': 'sdlkjsjkdf ldkjfds'
    }
    auth_manager = InstagramAuth(config)
    assert(auth_manager.attempt() == True)

  def test_attempt_fail(self):
    config = {
        'email': 'gashilovdmitry@yandex.ru',
        'password': 'sdljsdfjk',
        'username': 'sldkjfsd',
        'first_name': 'sdlkjsjkdf ldkjfds'
    }

    with pytest.raises(Exception):
        auth_manager = InstagramAuth(config)
        auth_manager.attempt()

  def test_send_verify_email(self):
    # random email, works even with already registered emails
    config = {
        'email': 'sdkjlkdsfj@sdkjdfls.ru',
        'password': '#PWD_INSTAGRAM_BROWSER:10:1646157249:AedQAGcxmpyDHo8T4t8Ibiiz9muYzrT5KDxoinjO8ec+UslgJGwN/KsLrFycODgwa17+dU7a146S8pNbg+Gp6Xk2Vvan6ky35vJ4ALlGRC76XnxeKYzPCqdPBQUFBp4tlGCjAms76CcLRYVUZ0nqte0=',
        'username': 'sldkjfsd',
        'first_name': 'sdlkjsjkdf ldkjfds'
    }
    auth_manager = InstagramAuth(config)
    auth_manager.attempt()
    assert(auth_manager.sendVerifyEmail() == True)
