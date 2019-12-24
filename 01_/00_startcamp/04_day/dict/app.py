import requests
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/lotto_check')
def lotto_check():
    return render_template('lotto_check.html')


@app.route('/lotto_result')
def lotto_result():  
    #회차번호를 받아와야한다. 
    num = request.args.get('num')
    #동행복권에 요청을 보내 응답을 받는다. 
    res = requests.get(f'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={num}')
    #json형태로 바꿔준다. (우리가 크롬에서 보고있는 결과와 동일한 모습)
    lotto = res.json()  #딕셔너리형태
    #당첨번호 6개 갖고오기
    winner = []
    for i in range(1,7):
        winner.append(lotto[f'drwtNo{i}'])
        #append()를 이용하면 하나씩 넣는다.
    
    # 내번호 리스트 만들기 
    numbers = []
    for num in request.args.get('numbers').split():
        #공백을 잘라 리스트로 만드는 과정   .split()
        numbers.append(int(num))# 아직 문자였기때문에 int()로 형변환

    #등수 가리기(몇개 맞았는지 교집합이 필요하다.)
    matched = 0
    # 내 번호 요소를 뽑아서 당첨번호 리스트에 있는지 확인.
    for num in numbers:
        #내번호리스트를 돌면서 winner내의 값과 비교를 한다. 
        if num in winner: #winner 안에 있는지 판단
            matched += 1
    if len(numbers) == 6:
        if matched == 6:
            result ='1등입니다.'
        elif matched == 5 :
            #보너스 번호가 내 번호 리스트에 존재하면 if문을 수행
            if lotto['bnusNo'] in numbers:
                result = '2등입니다.'
            else:
                result = '3등입니다.'
        elif matched == 4:
            result = '4등'
        elif matched ==3:
            result = '5등'
        else:
            result = '꼬ㅓㅏㅇ'
    else:
        result = '번호의 수가 6개가 아닙니다.'
    return render_template('lotto_result.html',
                            winner = winner,
                            numbers = numbers,
                             result = result)