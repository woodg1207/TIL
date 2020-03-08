# 1. parsing



```python
import requests
from bs4 import BeautifulSoup

# HTML 코드 받아오기
response = requests.get("https://workey.codeit.kr/music/index")

# BeautifulSoup 타입으로 변환
soup = BeautifulSoup(response.text, 'html.parser')

# "popular__order" 클래스를 가진 태그에 중첩된 모든 <li> 태그 선택
li_tags = soup.select(".popular__order li")

# 빈 리스트 생성
popular_artists = []

# 텍스트 추출해서 리스트에 담기
for li in li_tags:
    popular_artists.append(li.text.strip())

# 결과 출력
print(popular_artists)
```







# 2. 웹페이지를 데이터프레임으로

데이터 가져오기의 마지막 단계에 도착했습니다.
우리가 원하는 데이터를 DataFrame으로 만들면 앞서 배웠던 시각화나 분석 등 다양하게 활용할 수 있겠죠?

[이케아](https://www.ikea.com/kr/ko/)의 검색 결과를 아래와 같은 DataFrame으로 만들어 봅시다.

![img](https://i.imgur.com/clYTU9j.png)

## DataFrame을 만드는 방법

어떻게 하면 DataFrame을 만들 수 있을까요?
DataFrame을 만드는 방법에는 여러 가지가 있고, 그중 하나는 리스트를 담은 리스트였습니다.
기억이 잘 안 나시는 분은 [이전 레슨](https://business.codeit.kr/assignments/998)을 참고해 보세요.

우리는 웹 페이지에서 상품의 정보를 파싱한 뒤, 리스트를 담은 리스트 형태로 저장할 겁니다.

## DataFrame 설계하기

먼저 하나의 레코드(row)에 대한 설계를 합니다.
column이 `"이름"`, `"가격"`, `"이미지 주소"` 총 세 개니까, 다음과 같은 형태로 만들면 되겠네요.

```python
["이름 1", "가격 1", "이미지 주소 1"]
```

그리고 이 레코드가 여러 개 모이면, DataFrame을 만들 수 있겠죠?
우리가 결국 원하는 형태는 이런 형태입니다.

```python
[["이름 1", "가격 1", "이미지 주소 1"], 
["이름 2", "가격 2", "이미지 주소 2"], 
["이름 3", "가격 3", "이미지 주소 3"]]
```

## 파싱하기

이제 방법을 알았으니, 데이터를 파싱해서 DataFrame으로 만들어 봅시다.

```python
import requests
from bs4 import BeautifulSoup

# 빈 리스트 생성
records = []

# 시작 페이지 지정
page_num = 1

while True:
    # HTML 코드 받아오기
    response = requests.get("https://www.ikea.com/kr/ko/search/?query=desk&pageNumber=" + str(page_num))

    # BeautifulSoup 타입으로 변형하기
    soup = BeautifulSoup(response.text, 'html.parser')

    # "prodName" 클래스가 있을 때만 상품 정보 가져오기
    if len(soup.select('.prodName')) > 0:
        product_names = soup.select('.prodName')
        product_prices = soup.select('.prodPrice')
        product_urls = soup.select('.prodImg')
        page_num += 1

        # 여기에 각 상품의 정보를 하나의 레코드로 저장하는 코드 추가

    else:
        break
```

페이지에 있는 모든 상품 이름은 `product_names`에, 상품 가격은 `product_prices`에, 이미지 링크는 `product_urls`에 저장했습니다.

이제 각 상품의 정보를 하나의 레코드로 만들고, 리스트에 순서대로 추가합니다.
(이미지 주소는 "https://www.ikea.com" 이후부터 나오기 때문에, "https://www.ikea.com"를 붙여 줍니다.)

```python
import requests
from bs4 import BeautifulSoup

# 빈 리스트 생성
records = []

# 시작 페이지 지정
page_num = 1

while True:
    # HTML 코드 받아오기
    response = requests.get("https://www.ikea.com/kr/ko/search/?query=desk&pageNumber=" + str(page_num))

    # BeautifulSoup 타입으로 변형하기
    soup = BeautifulSoup(response.text, 'html.parser')

    # "prodName" 클래스가 있을 때만 상품 정보 가져오기
    if len(soup.select('.prodName')) > 0:
        product_names = soup.select('.prodName')
        product_prices = soup.select('.prodPrice')
        product_urls = soup.select('.prodImg')
        page_num += 1
        
        # 상품의 정보를 하나의 레코드로 만들고, 리스트에 순서대로 추가하기
        index = 0
        for name in product_names:
            record = []
            record.append(product_names[index].text)
            record.append(product_prices[index].text.strip())
            record.append("https://www.ikea.com" + product_urls[index].get('src'))
            records.append(record)
            index += 1
    else:
        break

# 결과 출력
print(len(records))
print(records)
```

## DataFrame 만들기

이제 DataFrame 형태로 만들어주면 됩니다. pandas의 문법은 익숙하죠?

```python
import pandas as pd

# DataFrame 만들기
df = pd.DataFrame(data = records, columns = ["이름", "가격", "이미지 주소"])

# DataFrame 출력
df.head()
```

![img](https://i.imgur.com/clYTU9j.png)

완성된 전체 코드는 다음과 같습니다.

```python
import pandas as pd
import requests
from bs4 import BeautifulSoup

# 빈 리스트 생성
records = []

# 시작 페이지 지정
page_num = 1

while True:
    # HTML 코드 받아오기
    response = requests.get("https://www.ikea.com/kr/ko/search/?query=desk&pageNumber=" + str(page_num))

    # BeautifulSoup 타입으로 변형하기
    soup = BeautifulSoup(response.text, 'html.parser')

    # "prodName" 클래스가 있을 때만 상품 정보 가져오기
    if len(soup.select('.prodName')) > 0:
        product_names = soup.select('.prodName')
        product_prices = soup.select('.prodPrice')
        product_urls = soup.select('.prodImg')
        page_num += 1
        
        # 상품의 정보를 하나의 레코드로 만들고, 리스트에 순서대로 추가하기
        index = 0
        for name in product_names:
            record = []
            record.append(product_names[index].text)
            record.append(product_prices[index].text.strip())
            record.append("https://www.ikea.com" + product_urls[index].get('src'))
            records.append(record)
            index += 1
    else:
        break

# DataFrame 만들기
df = pd.DataFrame(data = records, columns = ["이름", "가격", "이미지 주소"])

# DataFrame 출력
df.head()
```