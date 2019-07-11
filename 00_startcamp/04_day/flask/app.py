from flask import Flask, render_template, request
from datetime import datetime
import random

app = Flask(__name__)
#render template으로 
@app.route('/')
def hello():
    # return 'Hello World!'
    return render_template('index.html')
    ##flask규칙 app.py위치에 templates라는 폴더를 만들고 안에 문서를 넣어야한다.
    # !+tab을 하면 html 기본서식을 만들어준다.

@app.route('/ssafy')
def ssafy():
    return 'Hello World Wide Web!'


@app.route('/dday')
def dday():
    #오늘날짜
    today_time = datetime.now()
    #수료날짜
    endgame = datetime(2019, 11, 29)
    #수료날짜 - 오늘날짜
    dday = endgame - today_time
    return f'{dday.days} 일 남았습니다.'


@app.route('/html')
def html():
    return '<h1>This is HTML TAG</h1>'


@app.route('/html_line')
def html_line():
    return """
    <h1>여러줄을 보내 봅시다.</h1>
    <ul>
        <li>숫자가 안붙어요</li>
        <li>숫자가 안붙어요</li>
    </ul>
    <ol>
        <li>숫자가 붙어요</li>
        <li>sfjslkfdjlkj</li>
    </ol>
    """


@app.route('/greeting/<name>') ##기본값이라서 원래는 <string:name> 
#다른변수를 받아올때는?
def greeting(name): #name이라는 변수를 받아오기위해서 
    # return f'반갑습니다.!{name}'
    return render_template('greeting.html',html_name = name) #name 변수값을 옮겨주는것이중요

@app.route('/cube/<int:number>') #int 형변환
def cube(number):
    #여기서 모든 연산을 끝내고 변수만 html로 넘긴다.
    num = number**3 #pow(number,3) 제곱은 number**
    #return f'{number}의 세제곱은 {num}'
    return render_template('cube.html', html_num = num, html_number = number)


@app.route('/lunch/<int:number>')
def lunch(number):
    #여러메뉴중에서 인원수 만큼의 메뉴를 응답한다. 
    ##order = random.sample(menu,number) 결과는 리스트형식으로 나온다.return값으로 올수없어서 
    # str(order) 형식으로 형변환을 해줘야한다. 
    menu = ['한우불고기', '코코넛 머시기', '도시락', '삼계탕', '볶음밥']
    boxes = []
    for i in range(number):
        boxes.insert(i,random.choice(menu))
    return f'여러분의 점심메뉴는{boxes}입니다.'


# render template(html파일 등) 매칭해서 보여주는 작업


@app.route('/movie')
def movie():
    movies = ['토이스토리4', '알라딘', '기생충', '스파이더맨', '엔드게임']
    return render_template('movie.html',movies = movies)


@app.route('/ping')
def ping():
    return render_template('ping.html')


@app.route('/pong')
def pong():
    print(request.args)
    name = request.args.get('data') #안녕하세요
    return render_template('pong.html', name = name)


#https://search.naver.com/search.naver?where=nexearch&query=
@app.route('/naver')
def naver():
    return render_template('naver.html')


@app.route('/google')
def google():
    return render_template('google.html')


@app.route('/bonbon')
def input_name():
    return render_template('bonbon.html')


@app.route('/bonbonpong')
def result_char():
    personality = ['돈복', '외모', '운', '인성', '민첩', '힘', '지능']
    ran = range(1,11)
    j = 0
    name_bon = request.args.get('data')
    personality_random = random.sample(personality,3)
    ran_random = random.sample(ran, 3)
    return render_template('bon.html', name = name_bon, personality = personality_random, ran = ran_random, j = j)