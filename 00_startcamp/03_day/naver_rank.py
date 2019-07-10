import requests
from bs4 import BeautifulSoup

url = 'https://www.naver.com/'
#요청 보내서 html 파일 받고
html = requests.get(url).text
#뷰숲으로 정제
soup = BeautifulSoup(html, 'html.parser')
#slect메서드로 사용해서 list를 얻어낸다. 
sites = soup.select('#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_list.PM_CL_realtimeKeyword_list_base > ul > li> a.ah_a > span.ah_k')
#뽑은 list를 with구문으로 잘 작성

with open('example.txt', 'w', encoding = 'utf-8') as f:
    for site in sites:
        f.write(f'{site.text}\n')
