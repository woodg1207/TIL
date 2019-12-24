import requests
from bs4 import BeautifulSoup
# bs4에서 일부분만 갖고 오기위해서 from을 사용
#정보 스크랩!

#1. 원하는 주소로 요청을 보내 응답을 저장한다. 
html = requests.get('https://finance.naver.com/sise/').text
#요구를 해준다
soup = BeautifulSoup(html, 'html.parser')#정보 가공
# print(type(soup))#문서의 타입을 알수있음
# print(type(html))
kospi = soup.select_one('#KOSPI_now').text
print(kospi)