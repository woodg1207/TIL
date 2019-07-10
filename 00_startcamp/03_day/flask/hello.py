from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'This is ssafy world!!'

@app.route('/ssafy') #마지막 주소의 /ssafy로 들어가면 어떤걸 할지 결정하도록함
def ssafy():  ##함수를 정의하는 방법 
    return 'This is ssafy!'
@app.route('/ss')
def bye():
    return 'this'

