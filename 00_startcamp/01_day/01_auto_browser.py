import webbrowser
import random
# # 1. need list
# # 2. for >> webbroser.open_new()

# #web = ['www.naver.com', 'www.google.com', 'www.op.gg']
# idols = ['bts', 'nrg', 'hot', 'babyvox']
# url = 'https://search.naver.com/search.naver?query='

# # for i in range(3):
# #     webbrowser.open(web[i]) 
#     # web list 를 차례대로 해주기위해서 i사용

# for idol in idols: #idols내용이 idol에 들어가서 입력이된다 
#     #배열이 끝날때까지 반복처리 된다. 
#     webbrowser.open_new(url+idol)
import requests
#정보 스크랩하기 할때 사용된다. 
response = requests.get('https://www.naver.com/').status_code
print(response)
from bs4 import BeautifulSoup
# bs4에서 일부분만 갖고 오기위해서 from을 사용