from IPython import embed
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from .models import Article, Comment

# Create your views here.
def index(request):
######          READ와 관련
    # articles = Article.objects.all() 
    articles = Article.objects.order_by('-pk') # 역순 - DB가 변경 <권장>
    # articles = Article.objects.all()[::-1] # python이 변경
    context = {'articles': articles, }
    return render(request, 'articles/index.html', context)

def create(request):
    if request.method == 'POST':
        # CREATE
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = request.FILES.get('image')
        article = Article(title=title, content=content, image=image)
        article.full_clean()
        article.save()

        return redirect(article) 
    else:
        # NEW
        return render(request, 'articles/create.html')
  
def detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    comments = article.comment_set.all()
    context = {'article':article,'comments':comments,}
    return render(request, 'articles/detail.html', context)

def delete(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == 'POST':
        article.delete()
        return redirect('articles:index')
    else:
        return redirect(article)

def update(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == 'POST':
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.image = request.FILES.get('image')
        article.save()
        return redirect(article)
    else:
        context = {'article':article,}
        return render(request, 'articles/update.html', context)

def commnets_create(request, article_pk):
    # 댓글을 달 게시글
    article = Article.objects.get(pk=article_pk)
    if request.method == 'POST':
        #form에서 넘어온 댓글 정보
        content = request.POST.get('content')
        # 댓글 생성 및 저장
        comment = Comment(article=article, content=content)
        comment.save()
        return redirect(article)
        # return redirect('articles:detail' article.pk) get_absolute를 구현 못했다면 
    else:
        return redirect(article)

def comments_delete(request, article_pk, comment_pk):
    # article = Article.objects.get(pk=article_pk)   시간이 길어질수 있기 때문에 
    # return redirect(article) 이 문장 하나만을 위해서 위의 문장을 쓸필요가 없다. 
    comment = Comment.objects.get(pk=comment_pk)
    if request.method == 'POST':
        comment.delete()
    return redirect('articles:detail', article_pk)