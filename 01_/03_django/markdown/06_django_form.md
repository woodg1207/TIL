# 06_django_form



## 1.form

#### **기본 형식**

forms.py

```python
from django import forms

class ArticleForm(forms.Form):
    title = forms.CharField(max_length=10)
    content = forms.CharField() ## models와의 차이점 textfield가 없는대신 사용.
```

views.py -- create함수

```python
def create(request):
    if request.method == 'POST':
        # form 인스턴스를 생성하고, 요청에 의한 데이터를 인자로 받는다. (binding)작업
        # 이 처리과정은 binding 이라고 불리며 유효성 체크를 할 수 있도록 해준다. 
        form = ArticleForm(request.POST)
        # form 이 유효한지 체크한다. 
        if form.is_valid(): #유효성 검사
            # form.clean_data 로 정제된 데이터를 받는다. 
            title = form.cleaned_data.get('title')  #정제된 데이터
            content = form.cleaned_data.get('content')
            article = Article.objects.create(title=title, content= content)
            return redirect(article)
    else:
        form = ArticleForm()
    # 상황에 따라 context에 넘어가는 2가지 form
    # 1. GET : 기본 form
    # 2. POST : 검증에 실패 후의 form(is_valid == False 일 경우)
    context = {'form' : form,}
    return render(request, 'articles/create.html', context)
```

create.html

```html
<h1>CREATE</h1>
<form action="" method="POST">
  {% csrf_token %}
  {{form.as_p}}
  <input type="submit" value="CREATE">
</form>
```

```html
{{form.as_p}}를 각각으로 꾸밀때 
###1
<form action="" method="POST">
  {% csrf_token %}
  {{form.title.label_tag}}
  {{form.title}}
  {{form.content.label_tag}}
  {{form.content}}
  <input type="submit" value="CREATE">
</form>
###2
  {% for field in form %}
    {{field.label_tag}}
    {{field}}
  {% endfor %}
```

`{# 주석처리할때 #}`

- input, label tag를 사용안해도 된다. 
- `.as_p`각각의 태그가 p태그로 표시된다. 

`is_valid`

- Form  객체의 유효성 검사를 하는데 가장 중요한 역할
- Form 객체가 생성되면, 유효성 검사를 하고 유효한지 아닌지 여부를 boolean으로 반환.

`cleaned_data`

- 유효성 검사 후 깔끔하고 정제된 dict 형태에서 데이터를 가져오는 방법
- `request.POST.get('title')`은 이제 절대 추천하지 않는다. (보안 상의 문제)

**Forms as HTML**

- `as_p()` : 각 필드가 단락(paragraph)으로 렌더링
- `as_ul()` : 각 필드가 목록 항목(list item)으로 렌더링
- `as_table()` : 각 필드가 테이블 행으로 렌더링

```idl
In [9]: form.as_p()
Out[9]: '<p><label for="id_title">Title:</label> <input type="text" name="title" value="24" maxlength="10" required id="id_title"></p>\n<p><label for="id_content">Content:</label> <input type="text" name="content" value="2424" required id="id_content"></p>'

In [10]: form.as_table()
Out[10]: '<tr><th><label for="id_title">Title:</label></th><td><input type="text" name="title" value="24" maxlength="10" required id="id_title"></td></tr>\n<tr><th><label for="id_content">Content:</label></th><td><input type="text" name="content" value="2424" required id="id_content"></td></tr>'

In [11]: form.as_ul()
Out[11]: '<li><label for="id_title">Title:</label> <input type="text" name="title" value="24" maxlength="10" required id="id_title"></li>\n<li><label for="id_content">Content:</label> <input type="text" name="content" value="2424" required id="id_content"></li>'
```

**widget**

- django form 을 사용하면 기본적으로 field에 맞는 default widget을 사용한다.

- 그런데 다른 widget을 사용하고 싶다면 `widget`인자를 통해 field를 새로 정의할 수 있다. 

- ```python
  # forms.py
  class ArticleForm(forms.Form):
      title = forms.CharField(
          max_length=10, 
          label='제목',
          widget=forms.TextInput(
              attrs={
                  'class':'my-title',
                  'placeholder':'Enter the title',
              }
          )
      )
      ## models와의 차이점 textfield가 없는대신 사용.
      content = forms.CharField(
          widget=forms.Textarea(
              attrs={
                  'class':'my-content',
                  'placeholder':'Enter the content',
                  'row': 5,
                  'cols':40,
              }
          ),
          label='내용'
      ) 
  ```

**예외 처리**

views.py

```python
def detail(request, article_pk):
    try:
        article = Article.objects.get(pk=article_pk)
    except Article.DoesNotExist:
        raise Http404('No Article matches the given query')
    .... # 많은 예외처리가 존재하게 됨.  >> 숏컷이 존재함
    context = {'article': article,}
    return render(request, 'articles/detail.html',context)
```

```python
def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    context = {'article': article,}
    return render(request, 'articles/detail.html',context)
```

`get_object_or_404()/get_list_or_404()`

- 해당 객체가 있다면`objects.get()`을 실행, 없으면 ObjectsDoesNotExist 예외가 아닌 Http404(HttpResponseNotFound)를 raise한다. 

##### 왜 404error가 나올 상황에 django는 500error를 발생 시켰을까?

- `.get()` 메서드는 조건에 맞는 데이터가 없는 경우 에러를 뿜게 설계되었다. 코드단계에서 발생한 에러에 대해서는 브라우저는 500 InternalServerError로 인식.
- 클라이언트 입장에서 `서버에 오류가 발생하여 요청을 수행할 수 없다.(500)` 라는 원인이 정확하지 않은 에러를 마주하기 때문에 **올바른 에러를 예외처리하고 발생 시키는 것 또한 개발에서 중요한 요소중 하나**이다.

```python
def update(request, article_pk):
...
    if request.method == 'POST':
...
    else:
        form = ArticleForm(initial={
            'title':article.title, 
            'content':article.content
            }
        )
        #같은 표현
        # form = ArticleForm(initial=article.__dict__)

...
```

`initial`

- form 나타날때 해당 필드의 초기 값
- HTML input 태그의 `value`속성을 사용했던 것과 동일
- 초기 값을 설정하는 인수는 `딕셔너리 자료형` 이다. 



## 2. django ModelForm

- 일반 form과 다르게 Model로 부터 Form을 자동으로 생성하는 기능 
- form class 안에 Meta 클래스를 정의하고, Meta클래스 안에  Model 속성에 해당하는 모델클래스를 지정한다.  즉, 어떤 모델을 기반으로 form을 작성할 것인지 지정하는 것이다. 
- 일반 form 에 비해 모델 정의를 다시 하지 않아서 쉽고 간결하게 작성 가능하다. 
- django 가 해당 모델에서 양식에 필요한 대부분의 정보를 이미 정의하게 된다. 
- 어떤 모델의 레코드를 만들어야 할지 이미 알고 있으므로 유효성 검사후 바로저장`save()`이 가능하다.

forms.py

```python
    
    ###1
    class Meta:
...
        widgets = {
            'title': forms.TextInput(attrs={
                'class':'my-title'
            })
        }
    ...
    ###2
    class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        max_length=10,
        widget=forms.TextInput(
            attrs={
                'class':'my-title',
                'palceholder':'endter the title'
            }
        )
    )
    class Meta:
        model = Article
```



ModelForm으로 views.py가 간결해짐

```python
def create(request):
    if request.method == 'POST':
        ...
        if form.is_valid(): #유효성 검사
            ...
            article = form.save()
            return redirect(article)
```

```python
# 이것도 간결해진다. initial >> instance로 변환
def update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect(article)
    else:
        form = ArticleForm(instance=article)
```

- Form class를 반드시 forms.py 에 작성할 필요는 없다. 하지만 코드가 길어지면 관리가 힘들어짐.
- 간혹 models.py에 작성하는 사람도 있다. 
- 하지만 되도록 해당 app 폴더 안에 `froms.py`에 작성하는것이 바람직하다.

**bootstrap 4** 

https://django-bootstrap4.readthedocs.io/en/latest/index.html

를통해서  form형식에서 bootstrap을 적용할 수 있다. 