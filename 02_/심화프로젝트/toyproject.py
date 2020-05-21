import requests, json

url = 'http://127.0.0.1:5000/heartrate'
data = {'outer': {'inner': 'value'}}

res = requests.post(url, data=json.dumps(data))
res = requests.post(url, data={'test':'case1'})

print(res.json())