from flask import Flask, render_template, request
import requests
from decouple import config

app = Flask(__name__)

api_url = 'https://api.telegram.org'
token = config('TELEGRAM_BOT_TOKEN')
chat_id = config('CHAT_ID')
naver_config_id = config('NAVER_CLIENT_ID')
naver_config_secret = config('NAVER_CLIENT_SECRET')

@app.route('/')
def hello():
    return 'Hi there'


@app.route('/write')
def write():
    return render_template('write.html')


@app.route('/send')
def send():
    text = request.args.get('message')#write에서 갖고온다.
    requests.get(f'{api_url}/bot{token}/sendMessage?chat_id={chat_id}&text={text}')
    ##get방식
    return render_template('send.html')


@app.route(f'/{token}', methods = ['POST'])
def telegram():
    #1 데이터 구조 프린트 해보기
    from_telegram = request.get_json()
    if from_telegram.get('message') is not None:
       
        chat_id = from_telegram.get('message').get('from').get('id')
        text = from_telegram.get('message').get('text')
        #한글 키워드 받기 

        #/번역 으로 입력이 시작되면 파파고로 번역이 동작한다. 
        if text[0:4] == '/한영 ':
            headers = {
                'X-Naver-Client-Id': naver_config_id,
                'X-Naver-Client-Secret': naver_config_secret
            }
            data = {
                'source': 'ko',
                'target': 'en',
                'text': text[4:]
            }            
            papago_res = requests.post('https://openapi.naver.com/v1/papago/n2mt', headers = headers, data = data)#포스트방식
            text = papago_res.json().get('message').get('result').get('translatedText') #여기에 한영 번역텍스트가 있다.
        if text[0:4] == '/한불 ':
            headers = {
                'X-Naver-Client-Id': naver_config_id,
                'X-Naver-Client-Secret': naver_config_secret
            }
            data = {
                'source': 'ko',
                'target': 'fr',
                'text': text[4:]
            }            
            papago_res = requests.post('https://openapi.naver.com/v1/papago/n2mt', headers = headers, data = data)#포스트방식
            text = papago_res.json().get('message').get('result').get('translatedText') #여기에 한영 번역텍스트가 있다.
        
            #회차번호를 받아와야한다. 
    
        if text[0:4] == f'/로또 ':
            num = text[4:]
            #동행복권에 요청을 보내 응답을 받는다. 
            res = requests.get(f'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={num}')
            #json형태로 바꿔준다. (우리가 크롬에서 보고있는 결과와 동일한 모습)
            lotto = res.json()  #딕셔너리형태
            #당첨번호 6개 갖고오기
            winner = []
            for i in range(1,7):
                winner.append(lotto[f'drwtNo{i}'])
            bonus_num = lotto['bnusNo']
            text = f'{num}회차 : {winner} : 보너스 번호는 {bonus_num}'
        
        
        requests.get(f'{api_url}/bot{token}/sendMessage?chat_id={chat_id}&text={text}')


    return '', 200
