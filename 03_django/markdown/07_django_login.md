# 회원가입 & 정보 수정

### 쿠키 & 세션

----

1. 비연결 지향
2. 상태정보 유지 안함(stateless, 무상태): 연결이 끊어지는 순간 클라이언트와 서버간의 통신이 끝남(각각 완벽하게 독립적.)

**쿠키(cookie)**

- 클라이언트의 로컬에 저장되는 키-값의 작은 데이터 파일
- 웹페이지에 접속하면 요청한 웹페이지를 서버로부터 받고 쿠키를 로컬에 저장하고, 클라이언트가 재요청시 웹페이지 요청과 함께 쿠키 값도 함께 전송
- 아이디 자동완성/ 공지메세지 하루 안보기/ 팝업안보기 체크/ 비로그인 장바구니에 담기 등 편의를 위하되 지워지거나 유출되어도 큰 일은 없을 정보들을 저장

**세션(session)**

- 사이트와 특정 브라우저(클라이언트)사이의 상태를 유지 시키는 것 
- 일정 시간동안 같은 브라우저로부터 들어오는 일련의 요구를 하나의 상태로 보고 상태를 유지하는 기술
- 클라이언트가 서버에 접속하면 서버가 특정 session id를 발급하고, 클라이언트는 session id를 쿠키를 사용해 저장. 클라이언트가 다시 서버에 접속하면 해당 쿠키(session id 가 담긴)를 이용해 서버에 session id를 전달한다.
- Django 는 특정 session id를 포함하는 쿠키를 사용해서 각각의 브라우저와 사이트가 연결된 세션을 알아낸다. 실질적인 session 의 database에 기본 설정 값으로 저장된다.(이는 쿠키 안에 데이터를 저장하는 것보다  더 보안에 유리하고, 쿠키는 악의 적인 사용자들에게 취약하기 때문.)
- session을 남발하면 사용자가 많은 서버일 경우 서버 부하가 발생합니다.
- 쿠키를 지우면 로그아웃은 왜??? --> 서버에서는 session에 사용자 로그인 정보를 갖고 있지만, 그것이 내 것이라는 걸 증명할 session id가 쿠키에서 사라졌기 때문.

**차이**

- 쿠키 : 클라이언트 로컬에 파일로 저장
- 세션 : 서버에 저장(이때 session id 는 쿠키의 형태로 클라이언트의 로컬에 저장)

**캐시(cache)**

- 가져오는데 비용이 드는 데이터를 한 번 가져온 뒤에는 임시로 저장
- 사용자의 컴퓨터 또는 중간 역할을 하는 서버에 저장.



방문기록 체크  views.py

```python
def index(request):
    # session 에 visits_num 키로 접근해 값을 가져온다.
    # 기본적으로 존재하지 않는 키이기 때문에 키가 없다면(방문한 적이 없다면) 
    # 0값을 가져오도록 한다.
    visits_num = request.session.get('visits_num',0)
    # 그리고 가져온 값을 session에 visits_num 에 매번 1씩 증가한 값으로 할당한다.
    # user의 다음 방문을 위해
    request.session['visits_num'] = visits_num + 1
    # session data 안에 있는 새로운 정보를 수정 했다면 django 는 수정한 사실을
    # 알아채지 못하기 때문에 다음과 같이 설정.
    request.session.modified = True
```

![](C:\Users\student\Desktop\TIL\03_django\markdown\img\1.JPG)

settings.py

```python
# 모든곳에서 request.session.modified = True 를 기본값으로 사요하고 싶다면
#다음과 같이 설정
SESSION_SAVE_EVERY_REQUEST = True
```

### 1. sign_up

----

- user를 create

- Authentication(인증) - 신원확인
  - 자신이 누구라고 주장하는 사람의 신원을 확인하는 것
- Authorization(권한, 허가) - 권한 부여
  - 가고싶은 곳으로 가도록 혹은 원하는 정보를 얻도록 허용하는 과정

accounts app

views.py

```python
from IPython import embed
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = UserCreationForm()
    context = {'form':form, }
    return render(request, 'accounts/signup.html', context)
```



accounts / signup.html

```html
{% extends 'articles/base.html' %}
{% load bootstrap4 %}
{% block content %}
  <h1>회원 가입</h1>
  <form action="" method="POST">
    {% csrf_token %}
    {% bootstrap_form form %}
    {% buttons submit='회원가입' reset="Cancel" %}{% endbuttons %}
  </form>
{% endblock content %}
```



### 2. login

---

- session 을 create

accounts / views.py

```python
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
#...
from django.contrib.auth import login as auth_login
##...
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('articles:index')
    else:
        form = AuthenticationForm()
    context = {'form':form, }
    return render(request, 'accounts/login.html', context)
```

html은 signup.html과 비슷하다.



articles / base.html

```html
    <h3>Hello, {{ user.username }}</h3>
```

- 화면에서 로그인 한 사용자의 id가 나온다.



### 3.logout

----

- session을 delete

```python
from django.contrib.auth import logout as auth_logout
...

def logout(request):
    # user.delete()  회원 자체 삭제
    auth_logout()
    return redirect('articles:index')
```



articles/base.html

```html
    <h3>
      Hello, {{ user.username }}
      <a href="{% url 'accounts:logout' %}">[로그 아웃]</a>
    </h3>
```



#### 로그인 사용자에 대한 접근 제한

- django 는 세션과 미들웨어를 통해 인증 시스템을 request객체에 연결한다.
- request 는 현재 사용자를 나타내는 모든 요청에서 `request.user`를 제공한다.

`is_authenticated`

- user model의 속성(attributes)들 중 하나.
- 사용자가 인증 되었는지 알 수 있는 방법
- User에는 항상 True / AnonymousUser 에 대해서만 항상 False
- 단 , 이것은 권한(permission)과는 관련이 없으며. 사용자가 활동중(Active)이거나 유효한 세션(valid session)을 갖고 있는지도 확인하지 않는다.
-  일반적으로 `request.user`에서 이 속성을 사요하여 미들웨어의    `'django.contrib.auth.middleware.AuthenticationMiddleware',`를 통과 했는지 확인한다.

```python
def signup(request):
    # user 가 인증된 상태면 안들어가 지도록
    if request.user.is_authenticated:
        return redirect('articles:index')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            #form.save()를 통해 반환된 User 클래스의 인스턴스를
            # auth_login의 인자로 전달
            #회원 가입 후 자동으로 로그인 되어진다. 
            user = form.save()
            auth_login(request, user)
            return redirect('articles:index')
```

##### docorator

`next` query srting parameter

- @login_required 데코레이터가 기본적으로 인증 성공 후 사용자를 리다이렉트 할 경로를 next라는 무자열 매개 변수에 저장한다.
- 우리가 url로 접그하려고 했던 그 주소가 로그인 하지 않으면 볼 수 없는 곳이라서, django가 로그인 페이지로 강제로 리다이렉트 했는데, 로그인을 다시 정상적으로 하고 나면 원래 요청 했던 주소로 보내주기위해 keep해둠

**ex**) 

1. @required_POST 가 있는 함수에 @login_required가 설정된다면 로그인 후 "next"매개 변수를 따라 해당함수로 다시 redirect (GET방식으로 진행된다.) 되면서 @required_POST 때문에 405error발생

```python
#@login_required  사용하면 에러 발생
@require_POST
def comments_create(request, article_pk):
    if request.user.is_authenticated:#로그인 판단 decorator를 사용하면 405에러가 발생
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            # 객체를 Create하지만, DB에 레코드는 작성하지 않는다.
            comment = comment_form.save(commit=False)
            comment.article_id = article_pk
            comment.save()
    return redirect('articles:detail',article_pk)
```



### 4. 회원 탈퇴

`request.user.delete()`

---

### 5. 회원 수정

---

##### `get_user_model()`

- User 를 직접 참조하는 대신 `django.contrib.auth.get_user_model()`를 사용하여 User model을 참조해야한다.
- 이 함수는 현재 활성화(Active)된 User model 을 return한다. 

### 6. 비밀 번호 변경

----

- 비밀 번호 변경후 로그아웃됨

- 비밀 번호 변경되면서 기존 세션과 회원인증 정보가 일치하지 않게 되었기 때문.

  ```python
  def change_password(request):
      if request.method == 'POST':
          # data보다 user가 먼저 들어감
          form = PasswordChangeForm(request.user, request.POST) 
          if form.is_valid():
              form.save()
              return redirect('articles:index')
      else:
          form = PasswordChangeForm(request.user)
      context = {'form': form,}
      return render(request, 'accounts/change_password.html', context)
  ```

- 현재 사용자의 인증세션이 무효화 되는 것을 막고, 세션을 유지한 상태로 업데이트

- `update_session_auth_hash`

  ```python
  from django.contrib.auth import update_session_auth_hash
  ...
  def change_password(request):
      if request.method == 'POST':
  		...
          if form.is_valid():
              form.save()
              update_session_auth_hash(request, form.user)
              return redirect('articles:index')
      ...
  ```



##### @@ 각기능들의  html들은 user form을 사용해서 양식이 같다 이를 위해서 하나로 합치는것이 가능하다.

accounts / auth_form.html

```django
{% extends 'articles/base.html' %}
{% load bootstrap4 %}

{% block content %}
  
{% if request.resolver_match.url_name == 'signup' %}
<h1>회원 가입</h1>
{% elif  request.resolver_match.url_name == 'login' %}
<h1>로그인</h1>
{% elif  request.resolver_match.url_name == 'update' %}
<h1>회원정보 수정</h1>
{% else %}
<h1>비밀 번호 변경</h1>
{% endif %}
  
  <form action="" method="POST">
    {% csrf_token %}
    {% bootstrap_form form %}
    {% buttons submit='회원가입' reset="Cancel" %}{% endbuttons %}
  </form>
{% endblock content %}
```



