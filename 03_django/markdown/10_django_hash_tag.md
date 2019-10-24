# # hash tag

## 1. hashtag

##### modles.py

```python
class Hashtag(models.Model):
    ## article model 보다 상위에 존재해야 한다.
    content = models.TextField(unique=True)

    def __str__(self):
        return self.content

class Article(models.Model):
    ...
    # blank=True : 빈 값도 허용을 시켜줌. 
    hashtag = models.ManyToManyField(Hashtag, blank=True)
    ...
```

**`unique`**

- True인 경우 이 필드는 테이블 전체에서 고유한 값이어야 한다.
- 유효성 검사 단계에서 실행되며 중복값이 있는 모델을 저장하려고 하면 .save() 메서드로 인해 `IntegrityError`가 발생한다.
- `ManyToManyField`및 `OneToOneField`를 제외한 모든 필드 유형에서 유효하다.

##### views.py

```python
@login_required
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid(): #유효성 검사
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            ## hashtag는 이미 저장 된 아티클의 내용을 이용해야한다.
            #### hashtag 시작점
            for word in article.content.split(): # content를 공백기준으로 list로 변경
                if word.startswith('#'):# '#'으로 시작하는 요소만 선택
                    hashtag, created = hashtag.objects.get_or_create(content=word) 
                    #tuple형식으로 온다.
                    # word와 같은 해시태그를 찾는데 있으면 기존 객체(.get), 
                    #없으면 새로운 객체 생성(.create)
                    article.hashtags.add(hashtag) 
                    # created를 사용하지 않았다면 hashtag[0]으로 작성
            return redirect(article)
    else:
        form = ArticleForm()
    context = {'form' : form,}
    return render(request, 'articles/form.html', context)
```

###### `get_or_create(defaults=None, **kwargs)`

- 주어진 kwargs  객체를 찾으며 필요한 경우 하나를 만든다
- `(object, created)` 형태의 튜플을 리턴한다.
- object는 검색 또는 생성된 객체이고, created는 새 객체 생성 여부를 지정하는 boolean 값이다.(새로 만들어진 object 라면 True, 기존에 존재하던 object 라면 False)
-  단, 이 메서드는 DB가 키워드 인자의 `unique`옵션을 강제하고 있다고 가정하고 실행한다.(혹시모를 중복 오브젝트를 방지하기 위함)
- 이는 요청이 병렬로 작성 될때 및 중복 코드에 대한 문제 방지로 중복 오브젝트가 작성되는 것을 예방한다. 

#### 해시태그 정보

##### hashtag.html

```django
{% extends 'articles/base.html' %}
{% block content %}
<div class="jumbotron jumbotron-fluid text-center my-2 text-white bg-dark">
  <div class="container">
    <h1 class="display-4">{{  hashtag.content }}</h1>
    <p class="lead">{{ articles|length }} 개의 게시글</p>
  </div>
</div>
<hr>
<h3 class="text-center">{{hashtag.content}} 를 태그한 글</h3>
<div class="row">
  {% for article in articles %}
{% with  likes=article.like_users.all comments=article.comment_set.all  %}
  <div class="col-4 my-2">
    <div class="card">
      <div class="card-body">
        <h5 class="card-title">{{article.title}}</h5>
        <p class="card-text">{{likes|length}} 명이 좋아요</p>
        <p class="card-text">{{ comments|length }} 개의 댓글</p>
        <a href="{% url 'articles:detail' article.pk %}" class="btn btn-success">go</a>
      </div>
    </div>
  </div>
  {% endwith %}
  {% endfor %}
</div>
{% endblock content %}
```

##### views.py

```python
def hashtag(request, hash_pk):
    hashtag = get_object_or_404(Hashtag, pk=hash_pk)
    articles = hashtag.article_set.order_by('-pk')# 역참조, 최신글 순서
    context = {'hashtag': hashtag, 'articles':articles, }
    return render(request, 'articles/hashtag.html', context)
```

##### make_link.py || custom 필터만들기

```python
from django import template

register = template.Library()

@register.filter
def hashtag_link(word):
    # word 는 artcle 객체가 들어갈건데
    # article의 content 들만 모두 가져와서 그 중 해시태그에만 링크를 붙인다. 
    content = word.content + ' '
    hashtags = word.hashtags.all()

    for hashtag in hashtags:
        content = content.replace(
            hashtag.content+' ', 
            f'<a href="/articles/{hashtag.pk}/hashtag">{hashtag.content}</a> '
            )  # 마지막 공백 주의 
        # content = .replace(과거내용, 바꿀내용)
    
    return content
```

##### detail.html

```html
...
<p>{{article.pk}}</p>
<p>{{article.title}}</p>
<p>{{article|hashtag_link|safe}}</p>
<!-- 참고) 내장 필터인 safe 필터를 사용하여, tag escape를 방지할 수 있다. -->
...
```



## 2.소셜계정

### 카카오 계정 연동 : OAuth

django allauth : https://django-allauth.readthedocs.io/en/latest/installation.html

$ source venv/Scripts/activate

