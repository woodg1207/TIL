from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from .models import Article
from django.http import Http404
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
    context = {'article': article,}
    return render(request, 'articles/detail.html',context)

def delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        article.delete()
        return redirect('articles:index')
    else:
        return redirect(article)

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

def comments_create(request, article_pk):
    article = get_object_or_404(Article,pk=article_pk)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            article = comment_form.save()
            return redirect(article)
    else:
        comment_form = ArticleForm()
    context = {'comment_form':comment_form}
    return render(request, 'articles/form.html', context)