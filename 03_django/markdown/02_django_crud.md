# 02_django_crud

## 1.CRUD

### 1.1 CREATE

views.py

```python
###       CREATE와 관련 new(),create()
def new(request):
    return render(request, 'articles/new.html')

def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    
    #1  인스턴스로 >> Article() import해야함
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()

    #2
    article = Article(title=title, content=content)
    article.save()

    #3 검증을 못함 
    # Article.objects.create(title=title, content=content)

    # 글이 보이지 않는 이유는 페이지 자체는 index가 맞지만 url은 아직 create에 머물러있다.
    # return render(request, 'articles/create.html')
    return redirect('/articles/') # 메인페이지
```



### 1.2 READ

views.py

```python
def index(request):
######          READ와 관련
    # articles = Article.objects.all() 
    articles = Article.objects.order_by('-pk') # 역순 - DB가 변경 <권장>
    # articles = Article.objects.all()[::-1] # python이 변경
    context = {'articles': articles, }
    return render(request, 'articles/index.html', context)
```



**get >> post**

글을 작성 할때 GET이 아닌 POST를 쓰는 3가지 이유

1. 사용자는 django에게 HTML파일을 줘!(GET)가 아니라 ~~한 레코드(글)을 생성 해줘!(POST) 이기 때문에 GET보다는 POST요청이 더 알맞다.
2. 데이터는 URL에 노출되면 안된다. (우리가 URL에 접근하는 방식은 모두 GET). query의 형태를 통해 DB schema를 유추할 수있게 되고 이는 보안의 측면에서 매우 취약하게 된다. 
3. 모델(DB를 조작하는 친구는) GET 이 아닌 POST 요청!! DB를 수청하는건 매우 중요한 일이고 그에 따른 최소한의 신원 확인이 필요하다! (GET으로 동작하게 된다면 악성사용자가 URL만으로 글을 작성, 수정, 삭제 할수 있게 된다. )



**Redirect**

- post요청은 html문서를 render하는게 아니라 ~~좀 처리해줘(요청)의 의미이기 때문에 요청을 처리하고 나서의 결과를 보기위한 페이지로 넘겨줘야 한다. 



**POST 요청으로 변경 후 변화 하는것**

- form을 통해 전송한 데이터를 받을때도 `request.POST`로 받아야한다.
- 글이 작성되면 실제로 URL에 데이터가 나타나지 않게 된다.
- html문서를 요청 하는게 아니기 때문에 html문서를 받아볼 수 있는 다른 페이지로 redirect하게 된다. 



**DETAIL**

detail.html

```html
{% extends 'base.html' %}

{% block content %}
  <h1 class="text-center">DETAIL</h1>
  <h2>NO. {{ article.pk}}</h2>
  <hr>
  <p>제목 : {{article.title}}</p>
  <p>내용 : {{article.content}}</p>
  <p>작성 시간 : {{article.created_at}}</p>
  <p>수정 시간 : {{article.updated_at}}</p>
  <hr>
  <a href="/articles/">{back}</a>
{% endblock content %}

```



**유효성 검증(옵션 검증)** full_clean()

views.py

```
def create(request):
    try:
        title = request.POST.get('title')
        content = request.POST.get('content')
        article = Article(title=title, content=content)
        article.full_clean()  # 유효성 검증이다. 
    except ValidationError:
        raise ValidationError('error')
    else:
        article.save()
        return redirect(f'/articles/{article.pk}/') 
```

During handling of the above exception ({'title': ['이 필드는 빈 칸으로 둘 수 없습니다.'], 'content': ['이 필드는 빈 칸으로 둘 수 없습니다.']}), another exception occurred:

- models.py에서의 제한사항을 검증한다. 
- 위에처럼 안하면 빈칸이나 제목이 20칸이 넘어가도 정상적으로 만들어진다. 



### 1.3 DELETE



views.py

```python
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('/articles/')
```









### 1.4 UPDATE

1. 수정하는 페이지 view (edit)
2. 직접 모델에 수정 요청을 보내는 view (update)

views.py

```python
def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {'article':article,}
    return render(request, 'articles/edit.html', context)

def update(request, pk):
    article = Article.objects.get(pk=pk)
    
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()

    return redirect(f'/articles/{article.pk}/')
```

