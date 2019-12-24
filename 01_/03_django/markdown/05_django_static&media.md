# 05_django_static&media

## 1. static &media

참고 링크

https://docs.djangoproject.com/en/2.2/howto/static-files/

-  정적파일

`app_name/templates/app_name/index.html`

`app_name/static/app_name/sample.png`

templates와 namespace는 같다.

### 1.1 index.html 이미지 올리기

```html
...
{% load static %}
<!--load를 써야 갖고 올수 있다. extends아래에 위치해야한다.-->
...
  <img src="{% static 'articles/images/a.jpg'%}" alt="minion.jpg">
...
```

### 1.2 settings.py 에 경로 설정

실제 파일이나 디렉토리가 아니고, URL로만 존재하는 단위

```python
....
#실제 파일이나 디렉토리가 아니고, URL로만 존재하는 단위
STATIC_URL = '/static/'

# 개발 단계에서 사용하는 실제 정적 파일이 위치한 경로를 지정하는 설정.
# 보통 boothsrap, 외부 템플릿을 저장하기 위해 경로를 만듦
STATICFILES_DIRS = [
    os.path.join(BASE_DIR,'crud','assets'),
]
```

### 1.3 upload

- DB에 images를 추가 할때 기존에는 not null이였지만 `balnk=True`를 설정해서 null값도 가능하게 함 

models.py

```python
class Article(models.Model):
    ...
    image = models.ImageField(blank=True)
    ...
```

##### NULL

- 기본값 : False

- DB와 관련이 있다. (databased-related)
- 주어진 컬럼이 null값을 가질 것인지 결정

##### blank

- 기본값 : False

- 데이터 유효성과 관련이 있따. (Validation-related)
- `full_clean()`/`is_valid()`처럼 유효성 검사 메서드가 호출될 때 유효성 검사에 사용된다.

`null=True, blank=False`

- DB내에서는 해당필드가 NULL을 사용하지만, 웹사이트 에서는 HTML INPUT 태그에 `requited`속성이 필요하다라는 것을 의미함

##### 주의사항

- 문자열 기반 필드( CharField, TextField...)에서는 `null=True`금지
- 이렇게 정의하게 되면 문자열 기반 필드는 `데이터없음`에 대한 값이 2가지가 된다. None과 빈 문자열을 갖게 된다. 
- 데이터 없음에 대한 조건이 2가지면 중복이기 때문에 문자열 기반 필드는 NULL이 아닌 빈 문자열을 사용하는게 장고의 컨벤션이다. 

```python
class Person(models.Model):
    name = models.TextField(blank=True) #null=True는 금지
    birth = models.DateField(null=True, blank=True)
    #문자열 기반 필드가 아닌 숫자 필드이기 때문에 가능.
```

###### Pillow

- image필드를 사요할 때 필수로 필요한 패키지
- `pip install Pillow`

"image" varchar(100) NOT NULL  - DB상에는 이미지 경로가 들어가게 된다. 

views.py

```python
def create(request):
    ...
    image = request.FILES.get('image')
    article = Article(title=title, content=content, image=image)
    ...
```

create.html

```html
<form action="" method="POST" enctype="multipart/form-data">
    ...
    <label for="image">IMAGE</label>
    <input type="file" name="image" id="image" accept="image/*">
    ...
```



### 2.1media

settings.py

```python
....
# STATIC_URL 와 비슷한 역할
#업로드 된 파일의 URL주소를 만들어 주는 역할.
#STATIC_URL과 값이 달라진다.
MEDIA_URL = '/media/'
# STATICFILES_DIRS 와 비슷한 역할을 한다.
#실제 파일이 업로드 되면 어디에 저장될지 정하는 실제 경로.
# STATICFILES_DIRS와 값이 달라야 한다. 
# 개발 단계에서 사용하는 경로이므로, 실제 배포 단계에서는 다른 경로 설정을 해야한다. 
MEDIA_ROOT = os.path.join(BASE_DIR,'mdeia')
...
```

crud/urls.py

```python
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('jobs/', include('jobs.urls')),
    path('articles/', include('articles.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# 첫번째 인자(settings.MEDIA_URL) : 어떤 URL을 정적으로 추가 할지 (media file url)
# 두번째 인자(document_root=) : 실제 해당 미디어 파일이 어디에 존재하는지
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 같은 의미
```



`article.image.url` == `/media/sample.jpg`

- 이미지도 edit을 통해 새로운 이미지로 수정 할 수 있지만, text와는 다르게 수정할 때 이미지를 무조건 업로드 하지 않으면 에러가 발생한다. (글만 수정하면 안된다. )
- 이미지는 바이너리 데이터(하나의 덩어리)라서 텍스트 처럼 **일부만 수정하는게 불가능** 그렇기 때문에 html input태그에 value속성으로 수정하는 방식이 아니고, 새로운 사지으로 덮어 씌우는 방법을 사용.
- `<input type= "file"`가 `value=""`를 지원하지 않는다.
- 정말 글만 수정 하고 싶다면 이전과 똑같은 이미지를 업로드하면 된다. 

<hr>

#### 문제 : 이미지 필드 설정 이전에 작성했던 게시글의 detail페이지가 동작하지 않는다. (article.image.url을 불러오지 못하기 때문)

1. static 파일로 이미지가 없을 때 대신 사용할 이미지를 미리 넣어둠

   ```html
   {% if article.image %}
       <img src="{{article.image.url}}" alt="">
   {% else %}
       <img src="{% static 'articles/images/no.png'%}" alt="">
   {% endif %}
   ```

2. 템플릿에서 `{%if%}` 문으로 article.image가 존재하는 경우만 이미지를 출력하도록 함.

   ```html
   {% if article.image %}
       <img src="{{article.image.url}}" alt="">
   
   {% endif %}
   ```

### 2.2image resizing

- Pillow
- pilkit : Pillow를 쉽게 쓸 수 있도록 도와주는 라이브러리
- django-imagekit : 이미지 helper를 제공하는 django app

###### 주의 사항 : 설치 순서가 중요

1. html태그로 직접 사이즈 조정

   - 원본은 그대로 저장되어 있고 보여지는 사이즈만 조정하기 때문에 근본적인 해결책이 아니다.

2. 업로드 할 때 이미지 자체를 resizing

   2.1 원본x / 썸네일o

   models.py

   ```python
   from imagekit.models import ProcessedImageField
   from imagekit.processors import Thumbnail
   ...
   class Article(models.Model):
   ...
   	# ProcessedImageField()에 인자로 들어가 잇는 값들은 migrations이후에
       # 추가되거나 수정되더라도 makemigrations 를 하지 않아도 된다.
       image = ProcessedImageField(
           processors=[Thumbnail(200,300)], # 처리할 작업 목록
           format='JPEG', # 저장 포맷
           options={'quality':90}, # 추가 옵션들
           upload_to='articles/images', # 저장위치 (MEDIA_ROOT/articles/images)
       )
   ```

   

   2.2 원본o / 썸네일o

   ```python
   from imagekit.models import ProcessedImageField, ImageSpecField
   from imagekit.processors import Thumbnail
   
   class Article(models.Model):
   ...
       image = models.ImageField(blank=True)
       image_thumbnail = ImageSpecField(  #새로운 필드지만 DB에는 없다.
           source='image',#위의 image를 기반으로
           processors=[Thumbnail(200,300)],
           format='JPEG',
           options={'quality':90}
       )
   ...
   ```

#### 이미지업로드 경로 커스텀

`instance.pk`는 처음 레코드가 작성되는 순간에는 pk값이 없기때문

`media/articles/None/images` 로 저장

- 실제 개발에선 로그인을 통해 유저 정보를 받고, `instance.user.pk`또는 `instance.user.username`처럼 업로드한 정보를 