import requests
from pprint import pprint
import json
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}
d = {
    "nickname":"대전 2반 우동균",
    "yourAnswer" : "1"
}
##1
url = 'http://13.125.222.176/quiz/alpha'
r = requests.post('http://13.125.222.176/quiz/alpha', headers=headers, data=json.dumps(d))
pprint(r.json()) 
## 2
nextUrl = r.json()['nextUrl']
url = f'http://13.125.222.176/quiz/{nextUrl}'
d['yourAnswer']='86'
r = requests.post(url, headers=headers, data=json.dumps(d))
pprint(r.json())
## 3
nextUrl = r.json()['nextUrl']
url = f'http://13.125.222.176/quiz/{nextUrl}'
d['yourAnswer']='ssafycial'
r = requests.post(url, headers=headers, data=json.dumps(d))
pprint(r.json())
## 4
nextUrl = r.json()['nextUrl']
url = f'http://13.125.222.176/quiz/{nextUrl}'
d['yourAnswer']='protocol'
r = requests.post(url, headers=headers, data=json.dumps(d))
pprint(r.json())
## 5
nextUrl = r.json()['nextUrl']
url = f'http://13.125.222.176/quiz/{nextUrl}'
d['yourAnswer']='json'
r = requests.post(url, headers=headers, data=json.dumps(d))
pprint(r.json())
## 6 
nextUrl = r.json()['nextUrl']
url = f'http://13.125.222.176/quiz/{nextUrl}'
d['yourAnswer']='singleton'
r = requests.post(url, headers=headers, data=json.dumps(d))
pprint(r.json())
## 7
nextUrl = r.json()['nextUrl']
url = f'http://13.125.222.176/quiz/{nextUrl}'
d['yourAnswer']='cookie'
r = requests.post(url, headers=headers, data=json.dumps(d))
pprint(r.json())
## 8
nextUrl = r.json()['nextUrl']
url = f'http://13.125.222.176/quiz/{nextUrl}'
d['yourAnswer']='Redis'
r = requests.post(url, headers=headers, data=json.dumps(d))
pprint(r.json())
## 9
nextUrl = r.json()['nextUrl']
url = f'http://13.125.222.176/quiz/{nextUrl}'
d['yourAnswer']='mvvm'
r = requests.post(url, headers=headers, data=json.dumps(d))
pprint(r.json())
## 10
nextUrl = r.json()['nextUrl']
url = f'http://13.125.222.176/quiz/{nextUrl}'
d['yourAnswer']='pandas'
r = requests.post(url, headers=headers, data=json.dumps(d))
pprint(r.json())
## 11 
nextUrl = r.json()['nextUrl']
url = f'http://13.125.222.176/quiz/{nextUrl}'
d['yourAnswer']='bluetooth'
r = requests.post(url, headers=headers, data=json.dumps(d))
pprint(r.json())
## 12
nextUrl = r.json()['nextUrl']
url = f'http://13.125.222.176/quiz/{nextUrl}'
d['yourAnswer']='fittymon'
r = requests.post(url, headers=headers, data=json.dumps(d))
pprint(r.json())

## 13
nextUrl = r.json()['nextUrl']
url = f'http://13.125.222.176/quiz/{nextUrl}'
d['yourAnswer']='memoization'
r = requests.post(url, headers=headers, data=json.dumps(d))
pprint(r.json())
## 14
nextUrl = r.json()['nextUrl']
url = f'http://13.125.222.176/quiz/{nextUrl}'
d['yourAnswer']='ioc'
r = requests.post(url, headers=headers, data=json.dumps(d))
pprint(r.json())
## 15
nextUrl = r.json()['nextUrl']
url = f'http://13.125.222.176/quiz/{nextUrl}'
d['yourAnswer']='docker'
r = requests.post(url, headers=headers, data=json.dumps(d))
pprint(r.json())
## 16
nextUrl = r.json()['nextUrl']
url = f'http://13.125.222.176/quiz/{nextUrl}'
d['yourAnswer']='dfs'
r = requests.post(url, headers=headers, data=json.dumps(d))
pprint(r.json())
## 17
nextUrl = r.json()['nextUrl']
url = f'http://13.125.222.176/quiz/{nextUrl}'
d['yourAnswer']='bloom'
r = requests.post(url, headers=headers, data=json.dumps(d))
pprint(r.json())
## 18
nextUrl = r.json()['nextUrl']
url = f'http://13.125.222.176/quiz/{nextUrl}'
d['yourAnswer']='a'
r = requests.post(url, headers=headers, data=json.dumps(d))
pprint(r.json())
## 19
nextUrl = r.json()['nextUrl']
url = f'http://13.125.222.176/quiz/{nextUrl}'
d['yourAnswer']='quick'
r = requests.post(url, headers=headers, data=json.dumps(d))
pprint(r.json())
## 20
nextUrl = r.json()['nextUrl']
url = f'http://13.125.222.176/quiz/{nextUrl}'
d['yourAnswer']='kubernetes'
r = requests.post(url, headers=headers, data=json.dumps(d))
pprint(r.json())

