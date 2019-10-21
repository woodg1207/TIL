from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, Comment
from django.http import Http404, HttpResponse
from django.views.decorators.http import require_POST
from .forms import ArticleForm, CommentForm
from IPython import embed
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    # embed()
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
    context = {'articles':articles, 'visits_num': visits_num}
    return render(request, 'articles/index.html', context)

@login_required
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        # form 이 유효한지 체크한다. 
        if form.is_valid(): #유효성 검사
            # ModelsForm으로 간결해짐
            article = form.save()
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
    comments = article.comment_set.all() # article 의 모든 댓글 
    comment_form = CommentForm() # 댓글 폼
    context = {'article': article,'comment_form':comment_form, 'comments':comments, }
    return render(request, 'articles/detail.html', context)


@require_POST
def delete(request, article_pk):
    if request.user.is_authenticated:#로그인 판단 decorator를 사용하면 405에러가 발생
        article = get_object_or_404(Article, pk=article_pk)
        article.delete()
    return redirect('articles:index')

@login_required
def update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect(article)
    else:
        form = ArticleForm(instance=article)
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
            # 객체를 Create하지만, DB에 레코드는 작성하지 않는다.
            comment = comment_form.save(commit=False)
            comment.article_id = article_pk
            comment.save()
    return redirect('articles:detail',article_pk)

# @login_required
@require_POST
def comments_delete(request, article_pk, comment_pk):
    if request.user.is_authenticated:#로그인 판단 decorator를 사용하면 405에러가 발생
        comment = get_object_or_404(Comment, pk=comment_pk)
        comment.delete()
        return redirect('articles:detail', article_pk)
    return HttpResponse('You are Unauthorized :(', status=401) # 시멘틱 표현

