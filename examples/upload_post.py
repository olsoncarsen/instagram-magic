from instagram_magic.instagrambot import InstagramBot 

import requests
import logging
import json

if __name__ == '__main__':

    logging.basicConfig(filename='init.log', encoding='utf-8', level=logging.DEBUG) 
     
    response = requests.get("https://picsum.photos/1080/1080")       
    file = open("sample_image.jpg", "wb")
    file.write(response.content)
    file.close()

    bot = InstagramBot()
    bot.loadFromFile(file_path='yourfilename.json')
    res = bot.uploadPost('sample_image.jpg', 'your caption')
    logging.debug("UPLOAD POST ACTION -- response: " + res.content.decode('utf-8'))

    decoded_content = json.loads(res.content)
    upload_id = decoded_content['upload_id']

    res = bot.configure(upload_id, 'your caption')
    logging.debug("CONFIGURE ACTION -- response: " + res.content.decode('utf-8'))
