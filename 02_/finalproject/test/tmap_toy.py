import time, datetime
import requests
from pprint import pprint
import csv
import sys; sys.stdin=open('g.txt','r')

start = time.process_time()

sk = ''
gps_data=''
for i in range(12):
    lat, lon = input().split('|')
    gps_data += f'{lon},{lat}|'
url = 'https://apis.openapi.sk.com/tmap/road/matchToRoads?version={}&appKey={}'.format(1,sk)

payload = {
    'responseType':1,
    'coords':gps_data
}

response = requests.post(url, params=payload)
# pprint(response.json())
data = response.json()
f = open('gps.csv','w',encoding='utf-8')
wr = csv.writer(f)
for gps_dict in data['resultData']['matchedPoints']:
    wr.writerow([gps_dict['matchedLocation']['latitude'],gps_dict['matchedLocation']['longitude']])
f.close()

print(time.process_time()-start)
# sec = time.time()-start
# times = str(datetime.timedelta(seconds=sec)).split('.')
# print(times[0])