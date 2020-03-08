import requests

rating_pages = []
for Y in range(2010, 2019):
    for M in range(1,13):
        for W in range(5):
            url = f'https://workey.codeit.kr/ratings/index?year={Y}&month={M}&weekIndex={W}'
            res = requests.get(url)
            rating_pages.append(res.text)


# print(len(rating_pages)) # 가져온 총 페이지 수 
# print(rating_pages[0]) # 첫 번째 페이지의 HTML 코드

import requests

response = requests.get("https://workey.codeit.kr/ratings/index")
rating_page = response.text
    
# 출력 코드
print(rating_page)