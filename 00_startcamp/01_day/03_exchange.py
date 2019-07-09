import requests
from bs4 import BeautifulSoup

html = requests.get('https://finance.naver.com/marketindex/').text
# 주소를 요청하고 html정보를 html변수에 저장
soup = BeautifulSoup(html, 'html.parser')
#beautifulsoup을 이용해서 변수를 가공한다. 
exchage = soup.select_one('#exchangeList > li.on > a.head.usd > div > span.value').text
#.text의 유무를 통해 html주소 또는 환전정보만 나오게 할 수있다. 
print(exchage)