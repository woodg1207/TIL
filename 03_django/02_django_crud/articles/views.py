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


###       CREATE와 관련 new(),create()
def new(request):
    return render(request, 'articles/new.html')

def create(request):
    try:
        title = request.POST.get('title')
        content = request.POST.get('content')

    #1  인스턴스로 >> Article() import해야함
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()

    #2
        article = Article(title=title, content=content)
        article.full_clean()
        
    except ValidationError:
        raise ValidationError('error')
    else:
        article.save()
        return redirect(f'/articles/{article.pk}/') 
    #3 검증을 못함 
    # Article.objects.create(title=title, content=content)

    # 글이 보이지 않는 이유는 페이지 자체는 index가 맞지만 url은 아직 create에 머물어있다.
    #
    # return render(request, 'articles/create.html')
    # return redirect(f'/articles/{article.pk}/') 

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {'article':article,}
    return render(request, 'articles/detail.html', context)

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('/articles/')

def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {'article':article,}
    return render(request, 'articles/edit.html', context)

def update(request, pk):
    article = Article.objects.get(pk=pk)
    
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()

    return redirect(f'/articles/{article.pk}/')
