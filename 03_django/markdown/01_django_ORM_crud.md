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

   - 테이블에 대한 설계도(django ORm이 만들어 줌)를 생성

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

테이블의 이름은 app 이름과 model에 작성한 class이름이 조합되어져서 자동으로 만들어진다. (**모두 소문자**)

모델의 클래스 변수들은 반드시 소문자로 작성한다. 