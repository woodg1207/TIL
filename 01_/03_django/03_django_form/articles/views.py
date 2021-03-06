import hashlib
from IPython import embed
from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, Comment, Hashtag
from .forms import ArticleForm, CommentForm
from django.http import Http404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    ##gravatar  필터(accounts/templatetags/gavatar.py)로 대체됨. 필요없어짐
    # if request.user.is_authenticated:
    #     gravatar_url = hashlib.md5(request.user.email.encode('utf-8').lower().strip()).hexdigest()
    #     # gravatar_url = None
    # else:
    #     gravatar_url = None



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
 
    articles = Article.objects.all()
    context = {'articles':articles, 'visits_num': visits_num, }
    return render(request, 'articles/index.html', context)

@login_required
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        # form 이 유효한지 체크한다. 
        if form.is_valid(): #유효성 검사
            # ModelsForm으로 간결해짐
            article = form.save(commit=False)
            # 저장을 하지는 않음 commit
            # article.user_id = request.user.pk 같은 표현
            article.user = request.user
            article.save()
            ## hashtag는 이미 저장 된 아티클의 내용을 이용해야한다.
            #### hashtag 시작점
            for word in article.content.split(): # content를 공백기준으로 list로 변경
                if word.startswith('#'):# '#'으로 시작하는 요소만 선택
                    hashtag, created = Hashtag.objects.get_or_create(content=word) 
                    #tuple형식으로 온다.
                    # word와 같은 해시태그를 찾는데 있으면 기존 객체(.get), 없으면 새로운 객체 생성(.create)
                    article.hashtags.add(hashtag) # created를 사용하지 않았다면 hashtag[0]으로 작성

            return redirect(article)
    else:
        form = ArticleForm()
    # 상황에 따라 context에 넘어가는 2가지 form
    # 1. GET : 기본 form
    # 2. POST : 검증에 실패 후의 form(is_valid == False 일 경우)
    context = {'form' : form,}
    return render(request, 'articles/form.html', context)

def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    # person = get_object_or_404(get_user_model(), pk=article.user.pk)
    person = get_object_or_404(get_user_model(), pk=article.user_id) # user_id 외래키
    comments = article.comment_set.all() # article 의 모든 댓글 
    comment_form = CommentForm() # 댓글 폼


    context = {'article': article,'comment_form':comment_form, 'comments':comments, 'person':person,}
    return render(request, 'articles/detail.html', context)


@require_POST
def delete(request, article_pk):
    if request.user.is_authenticated:#로그인 판단 decorator를 사용하면 405에러가 발생
        article = get_object_or_404(Article, pk=article_pk)
        if request.user==article.user:
            article.delete()
        else:
            return redirect(article)
    return redirect('articles:index')

@login_required
def update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.user == article.user:
        if request.method == 'POST':
            form = ArticleForm(request.POST, instance=article)
            #instance : 전에 있는 내용을 채워주는것
            if form.is_valid():
                article = form.save()
                ## hash
                article.hashtags.clear() # 해당 article의 hashtag 전체 삭제
                for word in article.content.split(): 
                    if word.startswith('#'):
                        hashtag, created = Hashtag.objects.get_or_create(content=word) 
                        article.hashtags.add(hashtag)
                return redirect(article)
        else:
            form = ArticleForm(instance=article)
    else:
        return redirect('articles:index')
    # 1. POST :  검증에 실패한 form(오류 메세지도 포함된 상태)
    # 2. GET : 초기하된 form 
    context = {'form':form,'article':article,}
    return render(request, 'articles/form.html',context)

#이미 POST만 들어오기 때문에  조건문이 사라진다. 

@require_POST
def comments_create(request, article_pk):
    if request.user.is_authenticated:#로그인 판단 decorator를 사용하면 405에러가 발생
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            # commit : 객체를 Create하지만, DB에 레코드는 작성하지 않는다.
            comment = comment_form.save(commit=False)
            comment.article_id = article_pk
            comment.user = request.user
            comment.save()
    return redirect('articles:detail',article_pk)

# @login_required
@require_POST
def comments_delete(request, article_pk, comment_pk):
    if request.user.is_authenticated:#로그인 판단 decorator를 사용하면 405에러가 발생
        comment = get_object_or_404(Comment, pk=comment_pk)
        if request.user == comment.user:    
            comment.delete()
        return redirect('articles:detail', article_pk)
    return HttpResponse('You are Unauthorized :(', status=401) # 시멘틱 표현

@login_required
def like(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)

    # 1.
    # # pk 가 없어도 상관이 없는 filter를 사용.(get()대신)
    if article.like_users.filter(pk=request.user.pk).exists():
        article.like_users.remove(request.user)
    else:
        article.like_users.add(request.user)
    # 2. 
    # # 해당 게시글에 좋아요를 누른 사람들 중에서 현재 접속 유저가 있다면 좋아요를 취소
    # if request.user in article.like_users.all():
    #     article.like_users.remove(request.user) # 좋아요 취소
    # else:
    #     article.like_users.add(request.user) # 좋아요 
    return redirect('articles:index')

def follow(request, article_pk, user_pk):
    person = get_object_or_404(get_user_model(), pk=user_pk)

    user = request.user
    # 내(request.user)가 게시글 유저(poson) 팔로워 목록에 이미 존재 한다면,
    # if user in person.followers.all(): 조건문을 이걸로도 가능
    if person.followers.filter(pk=user.pk).exists():
        person.followers.remove(user)
    else:
        person.followers.add(user)
    return redirect('articles:detail', article_pk)

def hashtag(request, hash_pk):
    hashtag = get_object_or_404(Hashtag, pk=hash_pk)
    articles = hashtag.article_set.order_by('-pk')# 역참조, 최신글 순서
    context = {'hashtag': hashtag, 'articles':articles, }
    return render(request, 'articles/hashtag.html', context)