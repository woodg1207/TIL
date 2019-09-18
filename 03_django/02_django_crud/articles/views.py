from IPython import embed
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from .models import Article

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
        article = Article(title=title, content=content)
        article.full_clean()
        article.save()
        return redirect(article) 
    else:
        # NEW
        return render(request, 'articles/create.html')
  
def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {'article':article,}
    return render(request, 'articles/detail.html', context)

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('articles:index')
    else:
        return redirect(article)

def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.save()
        return redirect(article)
    else:
        context = {'article':article,}
        return render(request, 'articles/update.html', context)