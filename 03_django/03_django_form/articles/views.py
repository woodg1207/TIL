from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, Comment
from django.http import Http404
from django.views.decorators.http import require_POST
from .forms import ArticleForm, CommentForm
from IPython import embed

# Create your views here.
def index(request):
    articles = Article.objects.all()
    # articles = get_list_or_404(Article)
    context = {'articles':articles}
    return render(request, 'articles/index.html', context)

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
    article = get_object_or_404(Article, pk=article_pk)
    article.delete()
    return redirect('articles:index')


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
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        # 객체를 Create하지만, DB에 레코드는 작성하지 않는다.
        comment = comment_form.save(commit=False)
        comment.article_id = article_pk
        comment.save()
    return redirect('articles:detail',article_pk)

@require_POST
def comments_delete(request, article_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    comment.delete()
    return redirect('articles:detail', article_pk)
