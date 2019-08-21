# 01_django_ORM_crud

## 1. ORM

장점

1. sql 을 몰라도 data base사용이 가능
2. sql의 절차적인 접근이 아닌 객체직향적 접근이 가능
3. 매핑 정보가 명확하여 ERD를 보는것에 대한 의존도를 낯출 수 있다.
4. ORM 은 독립적으로 작성되어있고, 해당 객체들을 재활용할 수있다. 개발자는 개체에 집중함으로써 해당 DB에 종속 될 필요 없이 자유롭게 개발 할 수 있다.  

단점

1. ORM만으로 완전히 거대한 서비스를 구현하기가 어렵다. 
   - 사용하기는 편하지 만, 설계는 매우 신중하게 해야함
   - 프로젝트의 규모가 커질 경우 난이도가 올라가게 된다. 
   - 순수 SQL보다 약간의 속도 저하가 생길 수 있다. 

2. 이미 프로세스가 많은 시스템에서는 ORM으로 대체하기가 어렵다. 

결론

- 생산성을 위해서 사용!

ORM을 사용하여 얻게되는 생산성은 약간의 성능저하나 다른 단점들을 상쇄할 만큼 뛰어나기 때문.

장점으로 인한 생산성 증가가 훨씬 크기 때문에 현대에는 대부분의 프레임워크들이 ORM을 사용하고 있다. 

즉, 우리는 DB를 객체(object)-인스턴스(instance)로 조작하기위해서 ORM을 배운다. 



### 1-1 model의 개념

- 모델은 단일한 데이터에 대한 정보를 갖고 있다.
- 필수적인 필드(컬럼, 열)와 데이터(레코드, 행)에 대한 정보를 포함한다. 일반적으로 각각의 모델(클래스)은 단일한 데이터베이스 테이블과 매핑(연결, 연동)된다.
- 모델은 부가적인 메타데이터를 가직 DB의 구조(layout)를 의미
- 사용자가 저장하는 데이터들의 필수적인 필드 와 동작 (behvior)을 포함



참고 문서

https://docs.djangoproject.com/en/2.2/ref/models/fields/#datefield

#### CharField()

- 길이의 제한이 있는 문자열을 넣을 때 사용
- max_lnegth는 필수 인자다.
- 필드의 최대 길이(문자)이며 DB와 django의 유효성 검사(값을 검증)에서 사용됨.
- 텍스트 의 양이 많을 경우  TextField()로 사용

#### TextField()

- 글의 수가 많을 때 사용
- max_length 옵션을 줄 수 있지만 모델과 실제 DB에는 적용되지 않는다. 길이 제한을 주고 싶다면 CharField()를 사용해야한다. 

#### DataTimeField()

- 시간과 날짜를 기록하기 위한 필드
- auto_now_add=True
  - djangoORM이 최초 INSERT(테이블에 데이터 입력)시에만 현재 날짜와 시간 작성
  - **최초생성일자**

- auto_now=True
  - django ORM이 SAVE를 할 때마다 현재 날짜와 시간 작성 
  - **최종 수정 일자**

### 1-2 model 로직

- DB컬럼과 어떠한 타입으로 정의할 것인지에 대해 django.db 모듈의 models의 상속을 받아서 적용된다.
- 각 모델은 django.db.models.Model 클래스의 서브 클래스로 표현된다. (자식 클래스 )
- 모든 필드는 기본적으로 NOT NULL조건이 붙는다. (NULL 값이 드어갈 수 없다.)
- 각각의 클래스 변수들은 모델의 데이터베이스 필드를 나타낸다. 



#### Migrations

1. migrations

   ```
   $ python manage.py makemigrations
   ```

   - make migrations 명령어는 모델(model.py)을 작성/변경한 사항을 django에게 알리는 작업.(ORM  에 보낼 python 코드설계도를 작성)

   - 테이블에 대한 설계도(django ORM이 만들어 줌)를 생성

2. migrate

   ```bash
   $ python manage.py migrate
   ```

   - migrations 로 만든 설계도를 기반으로 실제 DB테이블(db.sqlite3 DB에 반영)을 만듦.
   - 모델에서의 변경사항들과 DB스키마가 동기화를 이룬다. 



#### 추가사항

```bash
$ python manage.py sqlmigrate app_name 0001
```

- 해당 설계도가 SQL 문으로 어떻게 해석되어서 동작할지 미리 볼 수있다. 

````bash
$ python manage.py showmigrations
````

- migrations 설계도가 migrate됐는지 안됐는지 확인.

#### model 변경시 작성 순서

1. models.py : 작성 및 변경(생성/ 수정)
2. makemigrations : migrations 파일 만들기 (설계도)
3. migrate : 실제 DB 에  적용 및 동기화 (테이블 생성)
4.  아무것도 안될때 [db.sqlite3], [0001등의 숫자 파일]을 지우고 처음부터 시작한다. 

테이블의 이름은 app 이름과 model에 작성한 class이름이 조합되어져서 자동으로 만들어진다. (**모두 소문자**)

모델의 클래스 변수들은 반드시 소문자로 작성한다. 

### 2. CRUD(DB API 조작)

1. Django Shell
   - django 프로젝트 설정이 로딩된 파이썬 shell
   - 일반 파이썬 shell로는 django환경에 접근 불가
   - 즉, django 프로젝트 환경에서 파이썬 shell을 활용한다고 생각 

```sqlite
from articles.models import Article  # 킬때마다 해줘야함
Article.objects.all()  # SELECT * FROM articles_article;  테이블내용을 전부 조회(READ)
```

- DB 에 쿼리를 날려서 인스턴스 객체 전부를 달라고 하는 뜻
- 만약 레코드가 하나라면, 인스턴스 단일 객체로 반환 
- 두개 이상이면 QuerySet형태로 반환

#### CREATE

**QuerySet 기본개념**

- 전달받은 객체의 목록
  - QuerySet :  쿼리 set 객체
  - Query : 단일 객체 

- DB로 부터 데이터를 읽고, 필터를 걸거나 정렬 등을 수행
- Query 를 던지는 Language(django ORM)를 활용해서 DB에게 데이터에 대한 조작을 요구한다. 

QuerySet

- objects를 사용하여 다수의 데이터를 가져오는 함수를 사용할때 반환되는 객체
- 단일한 객체를 반환(return)할때는 테이블(class)의 인스턴스로 return됨

'objects'

- Model Manager와 Django Model 사이의 Query연산의 인터네핑스 역할을 해주는 친구
- 즉, models.py 에 설정한 클래스(테이블)를 불러와서 사용할때 DB와의 인터페이스 역할(Query를 날려주는 역할 )하는 매니저이다.
- 쉽게 이해하려면 ORM의 역할이라고 생각하면 된다. 
- DB -------- objects --------- Python Class(models.py)

- Manager(objects) 를 통해 특정 데이터를 조작(메서드)할 수 있다. 

##### 데이터 객체를 만드는(생성, CREATE)하는 3가지 방법

1. 첫번째 방식

   ```python
   $ sqlite3 db.sqlite3 # 
   $ pip install ipython  # 설치
   $ python manage.py shell
   #SQL : 특정 테이블에 새로운 레코드(행)를 추가하여 데이터 추가
   # INSERT INTO table (column1, column2,....) VALUES(value1, ...)
   # INSERT INTO articles_article (title, content) VASLUES('first', 'django!')
   >>> article = Article()
   >>> article.title = 'first' # 인스턴스 변수에 값을 할당
   >>> article.content = 'django!' # 인스턴스 변수에 값을 할당
   
   # save를 하지 않으면 아직 DB에 값이 저장되지 않음
   >>> article
    <Article: Article object (None)>
   >>> article.objects.all()
    <QuerySet []>
   
   # save를 하고 확인해보면 저장 확인 가능
   >>> article.save()
   >>> article
   <Article: Article object (1)>
   >>> Article.objects.all()
   <QuerySet [<Article: Article object (1)>]>
   # 인스턴스 article을 활용하여 변수에 접근이 가능(저장된 값 확인)
   >>> article.title
   'first'
   >>> article.content
   'django!'
   >>> article.created_at
 datetime.datetime(2019, 8, 21, 2, 43, 57, 390667, tzinfo=<UTC>)
   >>> article.pk # id값을 볼수있다.
   ```
   
   

2. 두번째 방식

   ```python
   >>> article = Article(title='second', content='django!!')
   >>> article.save()
   
   >>>Article.objects.all()
   <QuerySet [<Article: Article object (1)>, <Article: Article object (2)>]>
   ```

3. 세번째 방식

   - create() 를 사용하면 쿼리셋 객체를 생성하고 저장하는 로직이 한번의 스텝으로 끝난다. 
   - 유효성 검증을 할 수가 없어 주로 1, 2번을 사용한다.

   ```python
   >>> Article.objects.create(title='third', content='django!!!')
   ```

   

##### 유효성 검사 

- save 전에 full_clean() 메서드를 통해 article이라는 인스턴스 객체가 검증(validation)에 적합한지 알아 볼 수 있다. 
- models.py 에 필드 속성과 옵션에 따라 검증을 진행한다. 

```python
>>>article = Article()
>>>article.title = 'life is short, you need python'
>>>article.full_clean()
ValidationError: {'title': ['이 값이 최대 10 개의 글자인지 확인하세요(입력값 30 자).'], 'content': ['이 필드는 빈 칸으로 둘 수 없습니다.']}
```



#### READ

```python
#1. SELECT*FROM articles_article;
#1. DB에 있는 모든 글 가져오기
>>> Article.objects.all()
<QuerySet []>

# 2. DB에 저장된 글 중에서 title이 first인 글만 가져오기
#2. SELECT*FROM articles_article WHERE title='first';
>>> Article.objects.filter(title='first')


In [3]: Article.objects.all()
Out[3]: <QuerySet [<Article: 1 번글 - first : django!>, <Article: 2 번글 - second 
글 - fourth : django!!!!>]>

In [4]: Article.objects.create(title='fifth', content='django!!!!!')
Out[4]: <Article: 5 번글 - fifth : django!!!!!>

In [5]: articles = Article.objects.filter(title='first')

In [6]: articles
Out[6]: <QuerySet [<Article: 1 번글 - first : django!>]>

In [7]: type(articles)
Out[7]: django.db.models.query.QuerySet

In [8]: Article.objects.create(title='first', content='django!!!!!!!')
Out[8]: <Article: 6 번글 - first : django!!!!!!!>

In [9]: Article.objects.filter(title='first')
Out[9]: <QuerySet [<Article: 1 번글 - first : django!>, <Article: 6 번글 - first : django!!!!!!!>]>

In [10]: Article.objects.filter(title='first').first()
Out[10]: <Article: 1 번글 - first : django!>

In [11]: Article.objects.filter(title='first').last()
Out[11]: <Article: 6 번글 - first : django!!!!!!!>

In [12]: article = Article.objects.get(pk=1)

In [13]: article
Out[13]: <Article: 1 번글 - first : django!>

In [14]: type(article)
Out[14]: articles.models.Article

In [15]: Article.objects.get(pk=10)
---------------------------------------------------------------------------
DoesNotExist                              Traceback (most recent call last)
<ipython-input-15-0dfc467affe8> in <module>
----> 1 Article.objects.get(pk=10)

~\Desktop\TIL\03_django\01_django_orm_crud\venv\lib\site-packages\django\db\models\manager.py in manager_method(self, *args, **kwargs)
     80         def create_method(name, method):
     81             def manager_method(self, *args, **kwargs):
---> 82                 return getattr(self.get_queryset(), name)(*args, **kwargs)
     83             manager_method.__name__ = method.__name__
     84             manager_method.__doc__ = method.__doc__

~\Desktop\TIL\03_django\01_django_orm_crud\venv\lib\site-packages\django\db\models\query.py in get(self, *args, **kwargs)
    406             raise self.model.DoesNotExist(
    407                 "%s matching query does not exist." %
--> 408                 self.model._meta.object_name
    409             )
    410         raise self.model.MultipleObjectsReturned(

DoesNotExist: Article matching query does not exist.

In [16]: Article.objects.get(title='first')
---------------------------------------------------------------------------
MultipleObjectsReturned                   Traceback (most recent call last)
<ipython-input-16-d1fbb51d7cde> in <module>
----> 1 Article.objects.get(title='first')

~\Desktop\TIL\03_django\01_django_orm_crud\venv\lib\site-packages\django\db\models\manager.py in manager_method(self, *args, **kwargs)
     80         def create_method(name, method):
     81             def manager_method(self, *args, **kwargs):
---> 82                 return getattr(self.get_queryset(), name)(*args, **kwargs)
     83             manager_method.__name__ = method.__name__
     84             manager_method.__doc__ = method.__doc__

~\Desktop\TIL\03_django\01_django_orm_crud\venv\lib\site-packages\django\db\models\query.py in get(self, *args, **kwargs)
    410         raise self.model.MultipleObjectsReturned(
    411             "get() returned more than one %s -- it returned %s!" %
--> 412             (self.model._meta.object_name, num)
    413         )
    414

MultipleObjectsReturned: get() returned more than one Article -- it returned 2!

In [17]: Article.objects.filter(pk=10)  #없는 pk여도 에러가 X
Out[17]: <QuerySet []>
        
>>> Article.objects.order_by('-pk')  #역순
Out[18]: <QuerySet [<Article: 6 번글 - first : django!!!!!!!>, <Article: 5 번글 - fifth : django!!!!!>, <Article: 4 번글 - fourth : django!!!!>, <Article: 3 번글 - third : django!!!>, <Article: 2 번글 - second : django!!>, <Article: 1 번글 - first : django!>]>
  
>>> articles = Article.objects.all()[1:3]  #슬라이싱 가능
In [20]: articles
Out[20]: <QuerySet [<Article: 2 번글 - second : django!!>, <Article: 3 번글 - third : django!!!>]>
    
        
In [22]: articles = Article.objects.filter(title__startswith='fir')

In [23]: articles
Out[23]: <QuerySet [<Article: 1 번글 - first : django!>, <Article: 6 번글 - first : django!!!!!!!>]>

In [24]: articles = Article.objects.filter(title__contains='fir')

In [25]: articles
Out[25]: <QuerySet [<Article: 1 번글 - first : django!>, <Article: 6 번글 - first : django!!!!!!!>]>

In [26]: articles = Article.objects.filter(content__endswith='!')
<QuerySet [<Article: 1 번글 - first : django!>, <Article: 2 번글 - second : django!!>, <Article: 3 번
글 - third : django!!!>, <Article: 4 번글 - fourth : django!!!!>, <Article: 5 번글 - fifth : django!!!!!>, <Article: 6 번글 - first : django!!!!!!!>]>
```

