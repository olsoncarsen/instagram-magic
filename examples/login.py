from instagram_magic.instagrambot import InstagramBot 

import logging
import json

if __name__ == '__main__':

    logging.basicConfig(filename='init.log', encoding='utf-8', level=logging.DEBUG) 
     
    bot = InstagramBot()
    bot.loadFromFile(file_path='yourfilename.json')
    res = bot.login()
    logging.debug("LOGIN ACTION -- response: " + res.content.decode('utf-8'))
    bot.storeAllData(file_path='yourfilename.json')
    res = bot.igSsoUsers()
    logging.debug("IG SSO USERS ACTION -- response: " + res.content.decode('utf-8'))
    bot.storeAllData(file_path='yourfilename.json')
