import requests, json

data_list = []
for i in range(20):
    url = 'https://api.themoviedb.org/3/movie/now_playing?api_key={}&language=ko-KR&page={}'.format(key, i+1)
    response = requests(url).json()['results']
    data_list.extend(response)