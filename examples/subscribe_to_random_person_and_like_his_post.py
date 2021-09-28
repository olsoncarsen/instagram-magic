from instagram_magic.instagrambot import InstagramBot 

import requests
import logging
import json

if __name__ == '__main__':
  logging.basicConfig(filename='init.log', encoding='utf-8', level=logging.DEBUG) 

  bot = InstagramBot()

  bot.loadFromFile(file_path='yourfilename.json')
  res = bot.getUserFollowers('18900337', 12, 12)
  logging.debug("GET USER FOLLOWERS ACTION -- response: " + res.content.decode('utf-8'))

  decoded_content = json.loads(res.content)
  if decoded_content['users'][0]['is_private']:
    logging.debug('user is private')
    
  res = bot.follow(decoded_content['users'][0]['pk'])
  logging.debug("FOLLOW USER ACTION -- response: " + res.content.decode('utf-8'))
  
  res = bot.getUserInfo(decoded_content['users'][0]['username'])
  logging.debug("GET USER INFO ACTION -- response: " + res.content.decode('utf-8'))

  decoded_content = json.loads(res.content)

  if decoded_content['graphql']['user']['edge_owner_to_timeline_media']['count']:
    res = bot.like(decoded_content['graphql']['user']['edge_owner_to_timeline_media']['edges'][0]['node']['id'])
    logging.debug("LIKE ACTION -- response: " + res.content.decode('utf-8'))
