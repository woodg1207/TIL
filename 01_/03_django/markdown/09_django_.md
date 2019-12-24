# N : M >> Follow

### profile

1. 유저가 작성한 게시글 목록
2. 유저가 작성한 댓글 목록
3. 정렬은 모두 최근에 작성한 것 부터
4. 각 게시글의 부가정보까지(좋아요, 댓글 몇개 달렸는지.)

account/views.py

```python
def profile(request, username):
    person = get_object_or_404(get_user_model(), username=username)
    # html에서 with 구문을 사용하면 조회를 하는 횟수가 줄어든다. markdown 참조
    articles = person.article_set.all()
    comments = person.comment_set.all()
    context = {'person': person,'articles': articles, 'comments':comments,}
    return render(request, 'accounts/profile.html', context)
```

`with`template tag

- 복잡한 변수를 더 간단한 이름으로 저장(캐시)하며, 여러번 DB를 조회할 때 (특히 비용이 많이 드는 )유용하게 사용이 가능하다.

```html
<div class="row">
  {% with articles=person.article_set.all %} <!-- 캐시에 저장시킴.  -->
  {% for article in articles %}
  <div class=:"col-12 my-2">
    <div class="card">
      <div class="card-body">
        <h5 class="card-title">{{ article.title }}</h5>
        <p class="card-text">{{ article.like_users.count }} 명이 좋아하는 글</p>
...
```

**하지만 조기 최적화는 프로그래밍에서 악의 근원**

코드는 코드 자체적으로도 빨라야 하지만 더 중요한 것은 다른 개발자들이 읽기 쉬워야 한다. 

## 1. follow

https://docs.djangoproject.com/ko/2.2/topics/auth/customizing/#substituting-a-custom-user-model

user: user

myform / settings.py

```python
AUTH_USER_MODEL = 'accounts.User'
```



### static 다시 정리

```python
STATICFILES_DIRS = [
    os.path.join(BASE_DIR,'crud','assets'),
]
#### 10.23 새로운 필기
#### 기본적으로 app_name/static/ *.img를 읽어온다.
# 설정해 주는 이유는 프로젝트에서 이미지를 받고 싶을때 사용해주는것으로 경로를 추가해주는것이다.
# 여러 앱이 존재할때 각각의 앱에는 static 폴더가 존재하게된다.
# 만약 이름 같은 이미지 파일 등이 있다면 어떤 파일인지 모르는 충돌이 발생하고
# 이를 방지하기 위해서 static/app_name/a.img 형식으로 앱이름의 폴더를 추가로 만들어 준다.
#이름표 같은 역할이다.
```































