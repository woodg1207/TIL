가상환경 환경 최적화?

```bash
$ pip freeze > requirements.txt

$ pip install -r requirements.txt
```

# 03_django_

## 1. url Namespace

### 1. 하드코딩 URL 제거

urls.py

`name='url name'`

```python
urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'), 
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:pk>/update/', views.update, name='update'),
]
```

detail.html

```html
  <a href="{% url 'edit' article.pk %}">[edit]</a>
  <a href="{% url 'delete' article.pk %}">[delete]</a>
  <a href="{% url 'index'%}">{back}</a>
{% endblock content %}
```

**app 이 여러개가 되면, 단순히 url name만 가지고 어떤 app의 url인지 알수 없다. **

urls.py 에서 `app_name = 'articles'`

이후 html에 설정

```html
  <a href="{% url 'articles:edit' article.pk %}">[edit]</a>
  <a href="{% url 'articles:delete' article.pk %}" onclick="return confirm('지울꺼야?')">[delete]</a>
  <a href="{% url 'articles:index'%}">{back}</a>
{% endblock content %}

```

 views.py에서도 가능

`    return redirect('articles:detail', article.pk)`



### 2. URI & URL

URI = URN + URL

#### 2-1.URI

- 인터넷에 자원을 나타내는 유일한 주소
- 인터넷에서 요구되는 기본적으로서 http에 항상 붙어 다닌다.

#### 2-2.URL

- 인터넷 상에서 자원이 어디 있는지 알려주기 위한 규약

##### ex)

1.

https://google.com

- 서버 주소 (URL이면서 URI)

2.

https://github.com/woodg1207/TIL/tree/master/01_python

- 주소 + 디렉토리 파일의 주소(자원의 위치)
- URL이면서 URI

3.

https://www.google.com/search?q=삼성

- 주소 + 특정 문자열 (query string)(search?q=)
- search 까지가 URL+q=삼성 이라는 식별자가 필요하므로 URI이지만 URL은 아니다. 

### 3. RESTfull

GET/POST   /   PATCH/DELETE

실제로 HTTP에서는 공식적으로  GET,POST만 지원한다. 

#### 3-1.  (new [GET] + create [POST])

같은 주소로 들어가는데 GET 이냐 POST냐에 따라 행동을 다르게 할것이다. 

urls.py

```python
app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),  # NEW(GET) + CREATE(POST)
    path('<int:pk>/', views.detail, name='detail'),
```

views.py

```python
def create(request):
    if request.method == 'POST':
        # CREATE
        title = request.POST.get('title')
        content = request.POST.get('content')
        article = Article(title=title, content=content)
        article.full_clean()
        article.save()
        return redirect('articles:detail',article.pk) 
    else:
        # NEW
        return render(request, 'articles/new.html')
```

GET articles/create/ 글을 작성하는 페이지

POST articles/create/ 글을 실제로 작성

new.html >>> create.html

```html
{% block content %}
  <h1 class="text-center">CREATE</h1>
  <form action="" method="POST">
    {% csrf_token %}  
    {% comment %} 토큰값을 같이 붙여서 보내줘야한다. {% endcomment %}
```

form tag 에 action이 없다면, 현재 머물고 있는 URL로 요청을 보낸다. 

### 4. Model Instance Method

#### 1. `get_absolute_url() `

models.py

```python
from django.urls import reverse
### ... 
class Article(models.Model):
### ... 
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # return reverse('articles:detail', args=[self.pk]) 같은 것,,, reverse는 문자열로 나온다. 
        return reverse('articles:detail', kwargs={'pk':self.pk}) #views.py에 있는 함수의 pk를 키값으로
    #주의사항
    #reverse 함수에 args랑 kwargs를 동시에 인자로 보낼 수 없다. 
```

URL Reverse를 수행하는 함수들

`reverse()`

- 리턴값 : string

  ```python
  reverse('articles:indx') ## article
  ```

`redirect()`

- 리턴값 : HttpResponseRedirect(객체)

- 내부적으로 `resolve_url()`을 사용

- view함수에서 특정 url로 돌려보내고자 할 때 사용

  ```python
  redirct('articles:article')
  # <HttpResponseRedirect status_code =200, "text/html;" 
  ```

`url template tag({% url %})`

- return 값으로 내부적으로 `reverse()`를 사용한다. 

