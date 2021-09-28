# instagram-magic

[![Unit Tests](https://github.com/olsoncarsen/instagram-magic/actions/workflows/test.yml/badge.svg)](https://github.com/olsoncarsen/instagram-magic/actions/workflows/test.yml)

Instagram web-api package that uses only requests (in development)

## Features

- [x] Registration
- [x] Log in 
- [x] Like/unlike
- [x] Follow/unfollow 
- [x] Upload comment
- [x] Upload stories 
- [x] Upload/delete posts 
- [x] Search 
- [x] Get users posts/info/followers
- [x] Get inbox (recommendations)
- [ ] Direct (chat) 

## Installation

```bash
git clone https://gitnub.com/olsoncarsen/instagrambot
python3 -m pip install -r requirements.txt

# or install package from testpypi (versions can be different from github and tespypi) 
python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps instagram_magic --upgrade
```

## Run tests 

Don't need addition data as confirmation code or real email address 

```bash
python3 -m pytest
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
