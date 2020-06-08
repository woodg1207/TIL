import time, datetime
import requests
from pprint import pprint
import csv
from decouple import config
import sys; sys.stdin=open('g.txt','r')

start = time.process_time()

sk = config('TMAP_API_KEY')
gps_data=''
for i in range(12):
    lat, lon = input().split('|')
    gps_data += f'{lon},{lat}|'
url = 'https://apis.openapi.sk.com/tmap/road/matchToRoads?version={}&appKey={}'.format(1,sk)
url1 = 'https://apis.openapi.sk.com/tmap/geo/reversegeocoding?version=1&lat=34.87782572&lon=128.53116011333333&coordType=WGS84GEO&addressType=A00&appKey={}'.format(sk)

payload = {
    'responseType':1,
    'coords':gps_data
}

res = requests.get(url1).json()
# print(res.json())
print(res['addressInfo']['fullAddress'])


# response = requests.post(url, params=payload)
# pprint(response.json())
# data = response.json()
# f = open('gps.csv','w',encoding='utf-8')
# wr = csv.writer(f)
# for gps_dict in data['resultData']['matchedPoints']:
#     wr.writerow([gps_dict['matchedLocation']['latitude'],gps_dict['matchedLocation']['longitude']])
# f.close()

print(time.process_time()-start)
# sec = time.time()-start
# times = str(datetime.timedelta(seconds=sec)).split('.')
# print(times[0])