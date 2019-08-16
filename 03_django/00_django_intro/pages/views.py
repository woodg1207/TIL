# django imports style guide
# 1. standard library
# 2. third-party
# 3. Django
# 4. local django
import random
from datetime import datetime
from django.shortcuts import render
from pprint import pprint
import requests

# Create your views here.
def index(request): # 첫번째 인자는 반드시 request
    return render(request, 'pages/index.html') # render() 의 첫번째 인자도 반드시 request


def introduce(request, name, age):
    context = {'name': name, 'age': age,}
    return render(request, 'pages/introduce.html', context)


def dinner(request):
    menu = ['족발', '햄버거', '치킨', '초밥']
    pick = random.choice(menu)
    context = {'pick': pick,}
    return render(request, 'pages/dinner.html', context)


def image(request):
    return render(request, 'pages/image.html')


def hello(request, name):
    menu = ['족발', '햄버거', '치킨', '초밥']
    pick = random.choice(menu)
    context = {'name': name, 'pick': pick,}
    return render(request, 'pages/hello.html', context)


def times(request, num1, num2):
    num3 = num1 * num2
    context = {'num3': num3, 'num1': num1, 'num2': num2,}
    return render(request, 'pages/times.html', context)


def area(request, r):
    area = (r ** 2) * 3.14
    context = {'r': r, 'area': area,}
    return render(request, 'pages/area.html', context)


def template_language(request):
    menus = ['짜장면', '탕수육', '짬뽕', '양장피',]
    my_sentence = 'Life is short, you need python'
    messages = ['apple', 'banana', 'cucumber', 'bean',]
    datetimenow = datetime.now()
    empty_list = []
    context = {
        'menus': menus,
        'my_sentence': my_sentence,
        'messages': messages,
        'datetimenow': datetimenow,
        'empty_list': empty_list,
    }
    return render(request, 'pages/template_language.html', context)


def isitgwangbok(request):
    today = datetime.now()
    if today.month == 8 and today.day == 15:
        result = True
    else:
        result = False
    context = {'result': result,}
    return render(request, 'pages/isitgwangbok.html', context)

def throw(request):
    return render(request, 'pages/throw.html')

def catch(request):
    # pprint(request.scheme)
    # pprint(request.path)
    # pprint(request.method)
    # pprint(request.GET)
    pprint(request.META)
    message = request.GET.get('message') # key 값을 갖고 온다.
    context = {'message': message,} 
    return render(request, 'pages/catch.html', context)

def art(request):
    return render(request, 'pages/art.html')

def result(request):
    # 1. art에서 form으로 보낸 데이터를 받는다. 
    word = request.GET.get('word')
    
    # 2. ATRII API 폰트리스트로 요청을 보내 응답을 text로 받는다. 
    fonts = requests.get('http://artii.herokuapp.com/fonts_list').text
    # 3. str을 list로 바꾼다.
    fonts = fonts.split('\n')
    # 4. fontlist안에 들어있는 요소중 하나를 선택해서 변수에 저장
    font = random.choice(fonts)
    # 5. 위에서 만든 word와 font를 가지고 다시 요청을 만들어서 보내 응답결과를 받는다. 
    response = requests.get(f'http://artii.herokuapp.com/make?text={word}&font={font}').text

    context = {'response': response,}
    return render(request, 'pages/result.html', context)

def user_new(request):
    return render(request, 'pages/user_new.html')

def user_create(request):
    # csrf 사이트간 요청위조
    #웹 어플리케이션 취약점 중 하나로 사용자가 자신의 의도와 무관하게
    # 공격자가 의도한 행동을 해서 특정 웹페이지의 보안을 무력화 시키거나, 수정, 삭제 등의 강제적인
    #작업을 하게 하는 공격 방법.
    # django는 최소한의 안전장치를 위해 자신이 부여한 랜덤 hash값을 token으로 부여한다.
    # 이 token값이 없는 요청은 잘못된 요청이라고 판단하여 접근을 거부한다. (403 error)
    name = request.POST.get('name')
    pwd = request.POST.get('pwd')
    context = {'name':name, 'pwd': pwd,}
    return render(request, 'pages/user_create.html', context)

def static_example(request):
    return render(request, 'pages/static_example.html')
    