[TOC]



# 02_day

## 1. 스크랩핑

### 1.1 실시간 검색어 리스트

#code name.py -> gitbash를 이용한 파이썬파일생성

리스트형식

```python
.select_one('경로')
.select('경로') # 리스트로 나오는 경우  
# 리스트로 오기때문에 .text가 안나온다. 
```

ex1) 실시간 검색어 뽑기

```python
import requests
from bs4 import BeautifulSoup
url = 'https://www.naver.com/' #더 좋은 표현

html = requests.get(url).text 
#url을 받고 text형식으로 뽑는다. 

soup = BeautifulSoup(html, 'html.parser')

sites = soup.select('#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_list.PM_CL_realtimeKeyword_list_base > ul > li > a.ah_a > span.ah_k')
#ul:nth-child(6) > li:nth-child(1) 한개 지정(등수)으로 되어있다.
##ul> li로 바꿔줌 >> 리스트로 뽑기위해서 
for site in sites:
    print(site.text) # 
```

## 2.git

### 2.1 (분산)버전 관리시스템

  과거버전으로 복원 변경 비교 분석이 가능 

버전 1과 2의 차이를 알수있다. 수정이유를 남길수 있다. 

### 2.2github

**git** **setting**

git config --global user.name "woodg1207"

git config --global user.email woodg1207@gmail.com

**check**

git config --global --list

git status     #git 상태확인

**add**

git add 00_startcamp  #index에 추가 

**commit**

git commit -m "firts commit"

// commit check

​		git log

**push**

​	git remote add origin https://github.com/woodg1207/TIL.git

 		//check

​		git remote -v