from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'This is ssafy world!!'

@app.route('/ssafy')
def ssafy():
    return 'This is ssafy'


