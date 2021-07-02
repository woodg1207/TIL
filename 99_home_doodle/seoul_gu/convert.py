import json

with open('./seoul.json', 'r', encoding='UTF-8') as f:
    json_data = json.load(f)

# print(json.dumps(json_data))
# print(len(json_data['info']))
result = []
for data in json_data['info']:
    gu = data["properties"]['SIG_KOR_NM']
    print(gu)
    path = []
    for latlon in data['geometry']['coordinates'][0]:
        s = f'new kakao.maps.LatLng({latlon[1]},{latlon[0]})'
        path.append(s)
    result.append({
        'name' : gu,
        'path': path
    })


# with open('./conver.json', 'w',encoding='utf-8') as f:
#     json.dump(result, f, indent=2)