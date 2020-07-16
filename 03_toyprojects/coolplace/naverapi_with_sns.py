import requests
from pprint import pprint
from decouple import config

naver = 'https://openapi.naver.com/v1/search/local.json?query='
naver += '광화문'
naver += '&display=5&sort=comment'
h = {
    'X-Naver-Client-Id':config('nav_client_id'),
    'X-Naver-Client-Secret':config('nav_client_secret')
}
# res_naver = requests.get(naver, headers=h)
# pprint(res_naver.json())
s = '둔산동 맛집'
blog = 'https://openapi.naver.com/v1/search/blog.json?query='
blog += s
blog += '&display=10&sort=sim&start=1'
res = requests.get(blog, headers=h)
pprint(res.json())


trend = 'https://openapi.naver.com/v1/datalab/search'
b = {
    'startDate':'2020-07-10',
    'endDate':'2020-07-16',
    'timeUnit':'date',

}