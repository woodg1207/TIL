import requests
from pprint import pprint
from decouple import config

naver = 'https://openapi.naver.com/v1/search/local.json?query='
naver += '청주복대동맛집'
naver += '&display=10&sort=comment'
h = {
    'X-Naver-Client-Id':config('nav_client_id'),
    'X-Naver-Client-Secret':config('nav_client_secret')
}
res = requests.get(naver, headers=h)
pprint(res.json())