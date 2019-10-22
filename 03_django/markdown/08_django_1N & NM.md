# 1:N & N:M

### 1. user : article

1:N- (Article : Comment)

​	  - (User : Article)

articles/models.py

```python
from django.conf import settings
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        ordering = ('-pk',)
    

```



**django 가 서버가 켜질때 초기화 순서**

1. `INSTALLED_APPS`의 각 항목을 imports합니다. (위에서 아래로)

   - 이 과정에서 직간접적으로 모델을 import해선 안된다. 

   - 1번 단계에서 app을 import하는 동안에 불필요한 제약들을 피하기위해 이 단계에서는 모델을 가져오지 않는다. 

2. 각 어플리케이션의 models를 import한다.

   - **2단계가 완료가 되면**, `get_model()`과 같은 모델에서 작동하는 APls를 사용할 수 있게 된다. 

3. `AppConfig`의 `ready()`메서드를 실행한다. 



1. 1단계에서 articles 부터 import시작
2. 2단계에서 articles 부터 model을 import시작
3. 2단계에서 accounts 에서 model을 import 시작
   - 2단계가 완료된 후에야 `get_user_model()`을 사용할 수 있는데 아직 accounts app 이 INSTALLED_APP의 작성 순서 때문에 아직 IMPORT 가 완료 되지 않은 상황이라 `get_user_model()`이 어떤 User model 을 return 해야 하는지 django가 알수 없는 상태이다. 

`get_user_model()`

- return 값이 `class`
- models.py를 예외한 모든 곳에서 user를 불러올때 사용이 가능함

`settings.AUTH_USER_MODEL`

- return 값이 `str`
- models.py에서만 사용

#### 결론

- 모든 곳에서 User model을 호출 할때는 `get_user_model()`
- models.py 에서만 `settings.AUTH_USER_MODEL`



### 2. user

##### 게시글에 작성자 이름 나타내기.

```python

```





##### user 판단 update/delete : 자신의 글이 아니면 수정/삭제 불가능

```python
@login_required
def update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.user == article.user:
        if request.method == 'POST':
            form = ArticleForm(request.POST, instance=article)
            #instance : 전에 있는 내용을 채워주는것
            if form.is_valid():
                article = form.save()
                return redirect(article)
        else:
            form = ArticleForm(instance=article)
    else:
        return redirect('articles:index')
    # 1. POST :  검증에 실패한 form(오류 메세지도 포함된 상태)
    # 2. GET : 초기하된 form 
    context = {'form':form,'article':article,}
    return render(request, 'articles/form.html',context)

@require_POST
def delete(request, article_pk):
    if request.user.is_authenticated:#로그인 판단 decorator를 사용하면 405에러가 발생
        article = get_object_or_404(Article, pk=article_pk)
        if request.user==article.user:
            article.delete()
        else:
            return redirect(article)
    return redirect('articles:index')
```



### 3. user : comment

```python
class Comment(models.Model):
    #1:N article:comment
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=140)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-pk', )

    def __str__(self):
        return self.content 
```



#### gravatar : 프로필 이미지

- Model Form Custom.
- Custom template tags and filters



## Model relationships

1.  Many to one -- 1:N
2. Many to Many

#### user : article = M:N

- user는 여러개의 article에 like 할 수 있고
- article은 여러 user로 부터 like를 받을 수 있다. 

##### **모델링은 현실 세계를 최대한 유사하게 반영하도록 해야한다.**

ex) 환자와 의사의 예약 시스템을 구축하라는 프로젝트 

1. 1:N 의 한계(1번 환자는 다른 의사로 바꿀려면 새로 레코드를 만들어야함.).이를 해결하기위해 2번.

2. 중개모델 생성

   ```python
   class Reservation(models.Model):
       doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
       patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
       
       def __str__(self):
           return f'{self.doctor_id}번 의사의 {self.patient_id}번 환자.'
       
   reservation_set.all()
   ```

3. 중개모델을 직접 거치지 않고 바로 가져 올수는 없을까?

   - `Through` option
   - M to M 필드는 실제 물리적인 필드가 db에 생기는 것은 아니다. 

4. Doctor도  patients로 참조 할수 없을까 

- `related_name`

  ```python
  class Patient(models.Model):
      name = models.TextField()
      # N:M 은 항상 복수형으로
      doctors =models.ManyToManyField(Doctor, through='Reservation',related_name='patients')
  ```

  - 참조되는 대상이 참조하는 대상을 찾을때(역참조), 어떻게 불러올지에 대해 정의한다. 
  - 필수 적으로 사욯하는 건 아니지만, 필수적인 상황이 발생할 수 있다. 

**중개 모델은 필요없는가?**

- 예약한 시간 정보를 담는다거나 하는 경우(==추가 적인 필드가 필요한 경우) 에는 반드시 중개모델을 만들어서 진행을 해야되는 상황도 있다. 다만 그럴 필요가 없는 경우 위와 같이 해결 할수 있다.



## LIKE

- user는 여러 article에 좋아요를 누를수 있고
- article은 여러 user로 부터 좋아요를 받을 수 있다.



`article.user` : 게시글을 작성한 유저  -1:N

`article.like_users` : 게시글을 좋아요한 유저 -N:M

`user.like_articles` 유저가 조하요 누른 게시글 (역참조, related_name으로 설정--설정안하면 `artilce_set`으로 자동설정됨) -N:M

`user.article_set` : 유저가 작성한 게시글(역참조) -1:N