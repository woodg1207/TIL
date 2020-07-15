import requests
from decouple import config

naver = 'https://openapi.naver.com/v1/search/local.json'
# res = requests.get()
print(config('nav_client_secret'))