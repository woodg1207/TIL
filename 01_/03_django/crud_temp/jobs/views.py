from django.shortcuts import render, redirect
from .models import Job
from faker import Faker
from decouple import config
import requests
from pprint import pprint

# Create your views here.
def index(request):
    return render(request, 'jobs/index.html')

def past_life(request):
    # 사용자로부터 이름 데이터를 받으 ㅁ
    name = request.POST.get('name')
    
    # db에 매칭되는 name 갖고 오기
    # Job.objects.get(name=name)
    # .get() 이 더 간단하지만 해당 값이 없을 경우 에러가 발생하기 때문.
    # filter 한개 또는 0개 상관없이 무조건 쿼리셋으로 갖고옴 (리스트 형식)
    person = Job.objects.filter(name=name).first()
    
    #db에 person이 있는지 없는지 확인 해야한다. 
    if person:
        past_job = person.past_job
    else: #db에 기존이름 이 없다면
        faker = Faker()
        past_job = faker.job()
        person = Job(name=name, past_job=past_job) #새로운 레코드를 추가한ㄷ. 
        person.save()
   

    #GIPHY (past_job을 API에 요청을 보내서 응답을 받음)
    GIPHY_API_KEY = config('GIPHY_API_KEY')
    url = f'http://api.giphy.com/v1/gifs/search?api_key={GIPHY_API_KEY}&q={past_job}&limit=1'
    data = requests.get(url).json()
    try:

        image = data.get('data')[0].get('images').get('original').get('url')
    except IndexError:
        image = None
    context = {
        'person':person,
        'image':image
    }
    return render(request, 'jobs/past_life.html', context)