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
    res = requests.get(f'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={numbers}')
    #json형태로 바꿔준다. (우리가 크롬에서 보고있는 결과와 동일한 모습)
    lotto = res.json()
    #당첨번호 6개 갖고오기
    winner = []
    for i in range(i,7):
        winner.append(lotto[f'drwNo{i}'])#append()를 이용하면 하나씩 넣는다.
    
    # 내번호 리스트 만들기 
    numbers = []
    for num in request.args.get('numbers').split():
        numbers.append(int(num))

    #등수 가리기(몇개 맞았는지 교집합이 필요하다.)
    matched = 0
    # 내 번호 요소를 뽑아서 당첨번호 리스트에 있는지 확인.
    for num in numbers:
        if num in winner: #winner 안에 있는지 판단
            matched += 1
    if matched == 6:
        result ='1등입니다.'
    elif matched == 5 :
        if lotto['bnusNo'] in numbers:
            result = '2등입니다.'
        else:
            result = '3등입니다.'
    elif matched == 4:
        result = '4등'
    elif matched ==3:
        result = '3등'
    else:
        result = '꼬ㅓㅏㅇ'
    return render_template('lotto_result.html',
                            winner = winner,
                            numbers = numbers,
                             result = result)
    


