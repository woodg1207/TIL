# 04_django_

## 1.RDB

### 1.foreignkey(참조키, 외래키)

개념

- 외래 키는 참조하는 테이블에서 1개의 키(속성 또는 속성의 집합), 참조하는 측의 변수는 참조되는 측의 테이블의 키를 가리킨다. 
- 하나(또는 복수)의 다른 테이블의 기본 키 필드를 가리키는 데이터의 참조 무결성을 확인 하기위하여 사용

특징

- 외래키의 값으로는 부모테이블에 존재하는 키의 값만 넣을 수 있다.
- 외래 키를 사용하여 **부모테이블의 유일한 값**을 참조한다. (부모 테이블의 기본키, 참조 무결성)

models.py

```python
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    .....
```

`models.ForeignKey()` 의 `on_delete`

- `FroeignKey` 의 필수인자이며, 참조하고있는 부모객체가 사라졌을때 어떻게 처리할 것인지 정의

1. `CASCADE` : 부모객체가 삭제시 이를 참조하는 객체도 삭제
2. `PROTECT`: 참조가 되어있는 경우 오류가 발생
3. `SET_NULL`: 부모객체가 삭제되었을 때 참조하는 모든 값을 NULL로 치환(DB 상에 NOT NULL 조건이 있다면 불가능)
4. `SET_DEAFAULT`: 모든 값이 DEFAULT로 설정한 값으로 치환(DB상에 DEFAULT 조건이 있어야함. )
5. `SET()`: 특정 함수를 호출(직접 만든 함수나 내장 함수)
6. `DO_NOTHING`: 아무것도 하지 않음(단, DB 상에 필드에 대한 `ON_DELETE`제한 조건을 따로 설정해야 한다.)



#### Relationship Fields

1. ForeignKey  -- 1: N
2. ManyToManyField -- M:N
3. OneToOneField -- 1:1

```python
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE) 
    # n:m 관계에선 related_name='comments'을 사용 
    #1:n에선 사용을 권장하지 않음'article_id'를 그대로 사용
```

#### Metadata

- `class Meta`와 같이 선언하여 모델에 대한 모델-레벨의 메타데이터를 선언 할 수있다.

- 유용한 기능들 중 하나는 쿼리할 때 반환되는 기본 레코드 순서를 제어하는 것이다. (`ordering`)

  ```python
  class Meta:
      #알파벳 순으로 content를 정렬한 후
      # 작성일(created_at) 별로 가장 나중에 작성된 것 부터 정렬
      ordering = ['content','-created_at']
  ```

- META : 데이터에 대한 데이터

### 2. 1:N 관계 활용하기

1. 1에서 N을 참조(역참조)
   - `article.comment`형태로는 가져올 수 없다. 게시글에 몇 개의 댓글이 있는지 django ORM이 보장 할 수 없기 때문.(본질적으로  Article 모델에 Comment와의 관계에 대해 작성된 것이 존재 하지 않는다. )
   - `article.comment_set`으로 접근할 수 있다. 
2. N 쪽에서 1을 참조하는 경우
   - 댓글의 입장에서 `comment.article`이 가능한 이유는 어떠한 댓글이든 반드시 시간이 참조하는 article이 있으므로 이와같이 접근할 수 있다. 



1:N 에서 N 쪽에서 1을 참조하는건 어렵지 않음

```python
comment.article
comment.article_id
...
```

역참조(1 에서 N을 참조하는 경우)

```python
article.comment ## error
```

#### comment 관련 추가사항

1. 댓글 개수 출력

   ```html
   1.<p><b>{{ comments|length }}개의 댓글</b></p>
   2.<p><b>{{ article.comment_set.all|length }}개의 댓글</b></p>
   3.<p><b>{{ comments.count }}개의 댓글</b></p>
   ```

   - 3번은 count 메서드가 호출 되면서 comment모델 쿼리를 한번더 DB에 보내기 때문에 매우 작은 차이지만 더 느리다. 

2.  댓글이 없는 경우 대체 문장 출력

   ```html
   <!-- 댓글 수  -->
   <p><b>{{ comments|length }}개의 댓글</b></p>
   <!-- 댓글을 읽어오는 곳 -->
   {% for comment in comments %}
   <p>댓글:{{comment.content}}</p>
   <p>{{comment.created_at}}</p>
   <form action=" {% url 'articles:comments_delete' article.pk comment.pk %} " method="POST">
     {% csrf_token %}
     <input type="submit" value="삭제">
   </form>
   
   {% empty %}
   <p><b>댓글이 없어요...</b></p>
   ```

   

   